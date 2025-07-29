from abc import ABC
from enum import Enum
from typing import Optional, ClassVar, Dict, Type, Tuple

from pydantic import BaseModel


class VetisCircuitEnum(str, Enum):
    """Перечисление для контуров ВетИС.API"""

    TEST = 'pilot'
    PRODUCTIVE = 'production'


class BaseOperation:
    """Операция SOAP-сервиса."""

    style: ClassVar[str]
    location: ClassVar[str]
    transport: ClassVar[str]
    soap_action: ClassVar[str]
    input: ClassVar[BaseModel]
    output: ClassVar[BaseModel]


class SubmitApplicationRequestOperation(BaseOperation):
    """Операция для отправки заявки в заявочную систему."""


class ReceiveApplicationResultOperation(BaseOperation):
    """Операция для получения результата по заявке в заявочной системе."""


class GetDataFromDictionaryServiceOperation(BaseOperation):
    """Операция для получения данных в справочной системе."""


class BaseApplication:
    """Базовый класс для ответа/запроса заявок."""

    @staticmethod
    def _get_doc_str_by(bases: Tuple[Type, ...]) -> Optional[str]:
        """Возвращает докстринг к ответу/заявке.

        Т.к. в xsd-схемах содержится довольно специфичное описание,
        настоящий докстринг может располагаться в базовом классе.
        """

        result = None

        for base in bases:
            if not issubclass(base, BaseApplication) and (doc_str := base.__doc__):
                # пропускаем докстринг pydantic.BaseModel
                if base is not BaseModel:
                    result = doc_str
                    break

        return result


class ApplicationRequest(BaseApplication):
    """Заявка."""

    def __init_subclass__(cls, **kwargs):
        """Динамически модифицирует докстринг класса (если он пуст)
        докстрингом базового класса.
        """
        super().__init_subclass__(**kwargs)

        cls.__doc__ = cls.__doc__ or cls._get_doc_str_by(cls.__bases__)


class ApplicationResponse(BaseApplication):
    """Ответ по заявке."""

    def __init_subclass__(cls, **kwargs):
        """Динамически модифицирует докстринг класса (если он пуст)
        докстрингом базового класса.
        """
        super().__init_subclass__(**kwargs)

        cls.__doc__ = cls.__doc__ or cls._get_doc_str_by(cls.__bases__)


class AbstractVetisService(ABC):
    def __init__(
        self,
        name: str,
        version: str,
        circuit: VetisCircuitEnum,
        ns_map: Dict[str, str],
        wsdl_uri: str,
        api_uri: str,
        api_port: Optional[int] = None,
    ) -> None:
        self._wsdl_types = None

        self.name = name
        self.version = version
        self.circuit = circuit
        self.ns_map = ns_map
        self.wsdl_uri = wsdl_uri
        self.api_uri = api_uri
        self.api_port = api_port

    @property
    def api_url(self) -> str:
        url = self.wsdl_uri

        if self.api_port:
            url = f'{url}:{self.api_port}'

        return url


class VetisAMSService(AbstractVetisService):
    """Сервис по работе со системой обработки заявок.

    Для подробного ознакомления см.
    https://help.vetrf.ru/wiki/Подсистема_обработки_заявок_в_Ветис.API
    """

    def __init__(self, *args, service_id: Optional[str] = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.service_id = service_id


class VetisDictionaryService(AbstractVetisService):
    """Сервис по работе со справочной системой."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
