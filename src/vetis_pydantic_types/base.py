from abc import ABC
from enum import Enum
from typing import Optional


class VetisCircuitEnum(str, Enum):
    """Перечисление для контуров ВетИС.API"""

    TEST = 'pilot'
    PRODUCTIVE = 'production'


class AbstractVetisService(ABC):
    def __init__(
        self,
        name: str,
        version: str,
        circuit: VetisCircuitEnum,
        wsdl_uri: str,
        api_uri: str,
        api_port: Optional[int] = None,
    ) -> None:
        self._wsdl_types = None

        self.name = name
        self.version = version
        self.circuit = circuit
        self.wsdl_uri = wsdl_uri
        self.api_uri = api_uri
        self.api_port = api_port

    @property
    def api_url(self) -> str:
        url = self.wsdl_uri

        if self.api_port:
            url = f'{url}:{self.api_port}'

        return url

    @property
    def wsdl_types(self):
        """Импортирует и кэширует в инстансе модуль с типами и операциями,
        определенными в WSDL.
        """

        # TODO:


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
