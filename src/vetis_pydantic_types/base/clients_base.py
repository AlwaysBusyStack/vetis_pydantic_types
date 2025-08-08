import logging
from time import sleep
from typing import Optional, Type, Dict, Union, Coroutine, Any
import asyncio
import xml.etree.ElementTree as ET
import requests
import httpx
from pydantic import BaseModel
from requests.auth import HTTPBasicAuth
from xsdata.models.datatype import XmlDateTime
from xsdata_pydantic.bindings import XmlParser, XmlSerializer, XmlContext

from vetis_pydantic_types.base.exceptions import VetisFaultError, VetisBusinessError, VetisTooManyRequestsError, \
    VetisUnauthorizedError
from vetis_pydantic_types.base.service_base import BaseVetisService, VetisAMSService
from vetis_pydantic_types.base.operations_base import (
    BaseOperation
)
from vetis_pydantic_types.base.application_base import ApplicationRequest, ApplicationResponse
from vetis_pydantic_types.constants import MILLISECONDS_PER_SECOND


class VetisClient:
    """Базовый клиент VetIS."""

    def __init__(
        self,
        service: BaseVetisService,
        auth: HTTPBasicAuth,
        timeout: Optional[int] = None,
    ):
        self.service = service
        self.auth = auth
        self.timeout = (timeout or 10 * MILLISECONDS_PER_SECOND) / MILLISECONDS_PER_SECOND

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
        component = self_cls.__module__.split('.')[-1]
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

    def _process_http_error(self, response: Union[httpx.Response, requests.Response]):
        """Рейзит ошибку уровня HTTP-протокола.

        Raises:
            VetisUnauthorizedError: Авторизационные данные неверны.
            requests.HTTPError: Ошибка синхронного запроса.
            httpx.HTTPStatusError: Ошибка асинхронного запроса.
        """

        if response.status_code == 401:
            raise VetisUnauthorizedError(
                f'Ошибка авторизации в системе ВетИС.API '
                f'({self.service.verbose_name} '
                f'контур - {self.service.circuit.value}), '
                f'проверьте ваши данные для авторизации'
            )
        else:
            response.raise_for_status()

    def sync_send(
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
            self._xml_to_str(ET.XML(xml_payload)),
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
            self._xml_to_str(ET.XML(response.content.decode('utf-8'))),
        )

        self._process_http_error(response)
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
            self._xml_to_str(ET.XML(xml_payload)),
        )

        async with httpx.AsyncClient(
            auth=(self.auth.username, self.auth.password),
            timeout=self.timeout
        ) as client:
            response = await client.post(uri, content=xml_payload, headers=headers)
            self._process_http_error(response)

            content = response.content

        self.logger.debug(
            '[ASYNC] Получен ответ от ВетИС.API:\n%s',
            self._xml_to_str(ET.XML(response.content.decode('utf-8'))),
        )

        result = self.parser.from_bytes(content, output_type, self.service.ns_map)
        self._check_fault(result)
        return result

    def send(
        self,
        uri: str,
        payload: BaseModel,
        headers: Dict[str, str],
        output_type: Type[BaseModel],
    ) -> Union[ApplicationResponse, Coroutine[Any, Any, ApplicationResponse]]:
        if asyncio.get_event_loop().is_running():
            result = self.async_send(uri, payload, headers, output_type)
        else:
            result = self.sync_send(uri, payload, headers, output_type)

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
        submit_operation_type: Type[BaseOperation],
        receive_operation_type: Type[BaseOperation],
        receive_timeout: Optional[int] = None,
        timeout: Optional[int] = None,
    ):
        super().__init__(service, auth, timeout)
        self.service = service
        self.api_key = api_key
        self.auth = auth

        self.submit_operation = submit_operation_type(self)
        self.receive_operation = receive_operation_type(self)
        self.default_receive_timeout = receive_timeout or MILLISECONDS_PER_SECOND

    def _check_business_errors(self, application_result: BaseModel) -> None:
        """Проверяет бизнес-ошибки."""
        if errors := getattr(application_result, 'errors', None):
            raise VetisBusinessError(f"Business errors: {errors}")

    def _process_http_error(self, response: Union[httpx.Response, requests.Response]):
        """Рейзит ошибку HTTP-протокола.

        Raises:
            VetisUnauthorizedError: Авторизационные данные неверны.
            VetisTooManyRequestsError: Достигнут лимит запросов в секунду.
            requests.HTTPError: Ошибка синхронного запроса.
            httpx.HTTPStatusError: Ошибка асинхронного запроса.
        """
        # По личным тестам на легкой заявочной операции на момент
        # 08.08.2025г. одновременно можно отправить около 12 операций
        # Справочные сервисы таких ограничений не имеют
        if response.status_code == 429:
            raise VetisTooManyRequestsError(
                'Достигнут лимит запросов в секунду к сервису, '
                'попробуйте снова позже'
            )
        else:
            super()._process_http_error(response)

    def sync_submit_application(
        self,
        application: ApplicationRequest,
        issuer_id: str,
        issue_date: Optional[XmlDateTime] = None,
        **headers,
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

        return self.submit_operation.send(request_data, **headers)

    async def async_submit_application(
        self,
        application: ApplicationRequest,
        issuer_id: str,
        issue_date: Optional[XmlDateTime] = None,
        **headers,
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
        response = await self.submit_operation.send(request_data, **headers)

        return response

    def sync_receive_application_result(self, application_id: str, issuer_id: str, **headers) -> BaseModel:
        """Получает результат заявки."""
        request_data = {
            'api_key': self.api_key,
            'issuer_id': issuer_id,
            'application_id': application_id,
        }
        response = self.receive_operation.send(request_data, **headers)

        return response

    async def async_receive_application_result(self, application_id: str, issuer_id: str, **headers) -> BaseModel:
        """Асинхронно получает результат заявки."""
        request_data = {
            'api_key': self.api_key,
            'issuer_id': issuer_id,
            'application_id': application_id,
        }

        response = await self.receive_operation.send(request_data, **headers)

        return response

    def sync_submit_and_wait_for_result(
        self,
        application: ApplicationRequest,
        issuer_id: str,
        receive_timeout: Optional[int] = None,
        issue_date: Optional[XmlDateTime] = None,
        **headers,
    ) -> ApplicationResponse:
        """Отправляет заявку и ждёт результат."""
        app_id = self.sync_submit_application(
            application, issuer_id, issue_date, **headers
        ).application.application_id

        while True:
            result = self.sync_receive_application_result(app_id, issuer_id, **headers)

            if result.application.status.value in self.finished_application_statuses:
                break

            timeout = (receive_timeout or self.default_receive_timeout) / MILLISECONDS_PER_SECOND
            sleep(timeout)

        self._check_business_errors(result)

        return getattr(result.application.result, 'any_element', None)

    async def async_submit_and_wait_for_result(
        self,
        application: ApplicationRequest,
        issuer_id: str,
        receive_timeout: Optional[int] = None,
        issue_date: Optional[XmlDateTime] = None,
        **headers,
    ) -> ApplicationResponse:
        """Асинхронно отправляет заявку и ждёт результат."""
        app_id = (
            await self.async_submit_application(
                application, issuer_id, issue_date, **headers,
            )
        ).application.application_id

        while True:
            result = await self.async_receive_application_result(app_id, issuer_id, **headers)

            if result.application.status.value in self.finished_application_statuses:
                break

            timeout = (receive_timeout or self.default_receive_timeout) / MILLISECONDS_PER_SECOND
            await asyncio.sleep(timeout)

        self._check_business_errors(result)

        return getattr(result.application.result, 'any_element', None)

    def submit_and_wait_for_result(
        self,
        application: ApplicationRequest,
        issuer_id: str,
        receive_timeout: Optional[int] = None,
        issue_date: Optional[XmlDateTime] = None,
        **headers,
    ) -> Union[
        ApplicationResponse,
        Coroutine[Any, Any, ApplicationResponse],
    ]:
        if asyncio.get_event_loop().is_running():
            result = self.async_submit_and_wait_for_result(
                application,
                issuer_id,
                receive_timeout,
                issue_date,
                **headers,
            )
        else:
            result = self.sync_submit_and_wait_for_result(
                application,
                issuer_id,
                receive_timeout,
                issue_date,
                **headers,
            )

        return result


class VetisRegistryClient(VetisClient):
    """Клиент для справочной системы."""
