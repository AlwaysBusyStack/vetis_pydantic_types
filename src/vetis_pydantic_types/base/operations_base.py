from typing import ClassVar, Type, Optional, Tuple, Union, Dict, Any

from pydantic import BaseModel
from xsdata_pydantic.fields import field, FieldInfo

from vetis_pydantic_types.base import ApplicationRequest, ApplicationResponse


class BaseIOOperation:
    """Примешивается к типам, которые являются операциями ввода-вывода"""

    def __init__(self, **kwargs):
        super().__init__()

    # ВетИС.API сервер может отвечать содержимым, в котором заполнены
    # заголовки - это удовлетворяет протоколу SOAP, но библиотека этого
    # не учла, поэтому нужно примешивать этот класс ко всем типам,
    # описыващим запросы/ответы к ВетИС.API
    header: Optional[object] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    # Для запросов/ответов определено это поле.
    body: BaseModel


class BaseOperation:
    """Операция SOAP-сервиса."""

    style: ClassVar[str]
    location: ClassVar[str]
    transport: ClassVar[str]
    soap_action: ClassVar[str]
    input: ClassVar[Type[BaseIOOperation]]
    output: ClassVar[Type[BaseIOOperation]]

    def __init__(self, client):
        self.client = client

    @property
    def real_location(self):
        """Возвращаем настоящий URL до сервиса.

        Некоторые базовые операции не разделены по контурам,
        из-за чего содержат URL до продуктивной версии эндпоинта,
        поэтому приходится подменять URL до сервисов налету.
        """

        return self.location.replace('https://api.vetrf.ru', self.client.service.api_url)

    @property
    def input_info(self) -> Tuple[str, FieldInfo]:
        field_name, request_info = tuple(
            self.input.model_fields['body'].annotation.model_fields.items()
        )[0]

        return field_name, request_info

    @property
    def output_info(self) -> Tuple[str, ApplicationResponse]:
        field_name, response_info = tuple(
            self.output.model_fields['body'].annotation.model_fields.items()
        )[0]

        return field_name, response_info

    def send(
        self,
        request: Union[ApplicationRequest, Dict[str, Any]],
        **headers,
    ) -> BaseModel:
        request_output = self.client.send(
            uri=self.real_location,
            payload=self.input(
                body={
                    self.input_info[0]: request,
                },
            ),
            headers={
                'content-type': 'text/xml',
                'SOAPAction': self.soap_action,
                **headers,
            },
            output_type=self.output,
        )

        return getattr(request_output.body, self.output_info[0])

    async def async_send(
        self,
        request: Union[ApplicationRequest, Dict[str, Any]],
        **headers,
    ) -> ApplicationResponse:
        request_output = await self.client.async_send(
            uri=self.real_location,
            payload=self.input(
                body={
                    self.input_info[0]: request,
                },
            ),
            headers={
                'content-type': 'text/xml',
                'SOAPAction': self.soap_action,
                **headers,
            },
            output_type=self.output,
        )

        return getattr(request_output.body, self.output_info[0])


class SubmitApplicationRequestOperation(BaseOperation):
    """Операция для отправки заявки в заявочную систему."""


class ReceiveApplicationResultOperation(BaseOperation):
    """Операция для получения результата по заявке в заявочной системе."""


class RegistryOperation(BaseOperation):
    """Операция для получения данных в справочной системе."""
