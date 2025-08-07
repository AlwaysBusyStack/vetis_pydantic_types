import logging
from time import sleep
from typing import Optional, Type, Dict, List, TypeVar
import asyncio
import xml.etree.ElementTree as ET
import requests
import httpx
from pydantic import BaseModel
from requests.auth import HTTPBasicAuth
from xsdata.models.datatype import XmlDateTime
from xsdata_pydantic.bindings import XmlParser, XmlSerializer, XmlContext

from vetis_pydantic_types.base.exceptions import VetisFaultError, VetisBusinessError
from vetis_pydantic_types.base.service_base import BaseVetisService, VetisAMSService
from vetis_pydantic_types.base.operations_base import (
    RegistryOperation
)
from vetis_pydantic_types.base.application_base import ApplicationRequest, ApplicationResponse


class VetisClient:
    """Базовый клиент VetIS."""

    def __init__(
        self,
        service: BaseVetisService,
        auth: HTTPBasicAuth,
        timeout: int = 10,
    ):
        self.service = service
        self.auth = auth
        self.timeout = timeout

        # Настройка логгера с иерархическим именем
        self.logger = logging.getLogger(self._get_logger_name())

        # Настройка XML
        context = XmlContext()
        self.parser = XmlParser(
            context=context,
        )
        self.serializer = XmlSerializer(context=context)

    def _get_logger_name(self):
        """Геттер имени логгера. Строится по принципу:
        [Имя компонента ВетИС.API].[pilot/production].[Имя класса]
        """
        self_cls = type(self)
        component = self_cls.__package__.split('.')[-1]
        circuit = self.service.circuit.value
        class_name = self_cls.__name__

        return f'{component}.{circuit}.{class_name}'

    def _xml_to_str(self, xml, pretty=True, encoding='utf-8'):
        if pretty:
            ET.indent(xml, space='    ')

        return ET.tostring(xml, encoding=encoding).decode(encoding)

    def _prepare_payload(self, payload: BaseModel) -> str:
        """Сериализует payload в XML."""
        return self.serializer.render(payload, self.service.ns_map)

    def _check_fault(self, response: BaseModel) -> None:
        """Проверяет SOAP Fault в ответе."""
        if fault := getattr(response, 'fault', None):
            raise VetisFaultError(f"SOAP Fault: {fault}")

    def send(
        self,
        uri: str,
        payload: BaseModel,
        headers: Dict[str, str],
        output_type: Type[BaseModel],
    ) -> BaseModel:
        """Синхронный запрос."""
        xml_payload = self._prepare_payload(payload)

        self.logger.debug(
            '[SYNC] Отправлен запрос в ВетИС.API:\n%s',
            self._xml_to_str(xml_payload),
        )

        response = requests.post(
            url=uri,
            data=xml_payload,
            headers=headers,
            auth=(
                self.auth.username,
                self.auth.password,
            ),
            timeout=self.timeout
        )

        self.logger.debug(
            '[SYNC] Получен ответ от ВетИС.API:\n%s',
            self._xml_to_str(response.content.decode('utf-8')),
        )

        response.raise_for_status()
        content = response.content

        result = self.parser.from_bytes(content, output_type, self.service.ns_map)
        self._check_fault(result)
        return result

    async def async_send(
        self,
        uri: str,
        payload: BaseModel,
        headers: Dict[str, str],
        output_type: Type[BaseModel],
    ) -> BaseModel:
        """Асинхронный запрос."""
        xml_payload = self._prepare_payload(payload)

        self.logger.debug(
            '[ASYNC] Отправлен запрос в ВетИС.API:\n%s',
            self._xml_to_str(xml_payload),
        )

        async with httpx.AsyncClient(
            auth=(self.auth.username, self.auth.password),
            timeout=self.timeout
        ) as client:
            response = await client.post(uri, content=xml_payload, headers=headers)
            response.raise_for_status()

            content = response.content

        self.logger.debug(
            '[ASYNC] Получен ответ от ВетИС.API:\n%s',
            self._xml_to_str(response.content.decode('utf-8')),
        )

        result = self.parser.from_bytes(content, output_type, self.service.ns_map)
        self._check_fault(result)
        return result


class VetisAMSClient(VetisClient):
    """Клиент для заявочной системы."""

    finished_application_statuses = (
        'COMPLETED',
        'REJECTED',
    )

    def __init__(
        self,
        service: VetisAMSService,
        auth: HTTPBasicAuth,
        api_key: str,
        **kwargs,
    ):
        super().__init__(service, auth, **kwargs)
        self.service = service
        self.api_key = api_key
        self.auth = auth

        self.submit_operation = self.service.submit_operation_type(self)
        self.receive_operation = self.service.receive_operation_type(self)

    def _check_business_errors(self, application_result: BaseModel) -> None:
        """Проверяет бизнес-ошибки."""
        if errors := getattr(application_result, 'errors', None):
            raise VetisBusinessError(f"Business errors: {errors}")

    def submit_application(
        self,
        application: ApplicationRequest,
        issuer_id: str,
        issue_date: Optional[XmlDateTime] = None,
    ) -> BaseModel:
        """Отправляет заявку и возвращает ID."""
        request_data = {
            'api_key': self.api_key,
            'application': {
                'service_id': self.service.service_id,
                'issuer_id': issuer_id,
                'issue_date': issue_date or XmlDateTime.now(),
                'data': {'any_element': application},
            },
        }

        return self.submit_operation.send(request_data)

    async def async_submit_application(
        self,
        application: ApplicationRequest,
        issuer_id: str,
        issue_date: Optional[XmlDateTime] = None,
    ) -> BaseModel:
        """Асинхронно отправляет заявку."""
        request_data = {
            'api_key': self.api_key,
            'application': {
                'service_id': self.service.service_id,
                'issuer_id': issuer_id,
                'issue_date': issue_date or XmlDateTime.now(),
                'data': {'any_element': application},
            },
        }
        response = await self.submit_operation.async_send(request_data)

        return response

    def receive_application_result(self, application_id: str, issuer_id: str) -> BaseModel:
        """Получает результат заявки."""
        request_data = {
            'api_key': self.api_key,
            'issuer_id': issuer_id,
            'application_id': application_id,
        }
        response = self.receive_operation.send(request_data)

        return response

    async def async_receive_application_result(self, application_id: str, issuer_id: str) -> BaseModel:
        """Асинхронно получает результат заявки."""
        request_data = {
            'api_key': self.api_key,
            'issuer_id': issuer_id,
            'application_id': application_id,
        }

        response = await self.receive_operation.async_send(request_data)

        return response

    def submit_and_wait_for_result(
        self,
        application: ApplicationRequest,
        issuer_id: str,
        receive_timeout: int = 1000,
        issue_date: Optional[XmlDateTime] = None,
    ) -> Optional[ApplicationResponse]:
        """Отправляет заявку и ждёт результат."""
        app_id = self.submit_application(
            application, issuer_id, issue_date
        ).application.application_id

        while True:
            result = self.receive_application_result(app_id, issuer_id)

            if result.application.status.value in self.finished_application_statuses:
                break

            sleep(receive_timeout / 1000)

        self._check_business_errors(result)

        return getattr(result.result, 'any_element', None)

    async def async_submit_and_wait_for_result(
        self,
        application: ApplicationRequest,
        issuer_id: str,
        receive_timeout: int = 1000,
        issue_date: Optional[XmlDateTime] = None,
    ) -> Optional[ApplicationResponse]:
        """Асинхронно отправляет заявку и ждёт результат."""
        app_id = (
            await self.async_submit_application(
                application, issuer_id, issue_date
            )
        ).application.application_id

        while True:
            result = await self.async_receive_application_result(app_id, issuer_id)

            if result.status.value not in ('ACCEPTED', 'IN_PROCESS'):
                break

            await asyncio.sleep(receive_timeout / 1000)

        self._check_business_errors(result)

        return getattr(result.result, 'any_element', None)


class VetisRegistryClient(VetisClient):
    """Клиент для справочной системы."""

    def __init__(
        self,
        service: BaseVetisService,
        auth: HTTPBasicAuth,
        operations: List[Type[RegistryOperation]],
        **kwargs,
    ):
        super().__init__(service, auth, **kwargs)

        self.operations = [
            op(self)
            for op in operations
        ]

    def send(
        self,
        uri: str,
        payload: ApplicationRequest,
        headers: Dict[str, str],
        output_type: Type[BaseModel],
    ) -> ApplicationResponse:
        """Синхронный запрос."""
        result = super().send(uri, payload, headers, output_type)

        return result

    async def async_send(
        self,
        uri: str,
        payload: ApplicationRequest,
        headers: Dict[str, str],
        output_type: Type[BaseModel],
    ) -> ApplicationResponse:
        """Асинхронный запрос."""
        result = await super().async_send(uri, payload, headers, output_type)

        return result
