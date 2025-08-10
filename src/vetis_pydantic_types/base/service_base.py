from contextlib import suppress
from importlib import import_module
from types import ModuleType
from typing import Dict, Optional, Type, Tuple

from vetis_pydantic_types.base.application_base import ApplicationRequest, ApplicationResponse
from vetis_pydantic_types.base.operations_base import ReceiveApplicationResultOperation, RegistryOperation, \
    SubmitApplicationRequestOperation
from vetis_pydantic_types.base.enum_base import VetisCircuitEnum
from vetis_pydantic_types.constants import TYPES_PACKAGE


class BaseVetisService:
    def __init__(
        self,
        component_name: str,
        verbose_name: str,
        version: str,
        circuit: VetisCircuitEnum,
        ns_map: Dict[str, str],
        wsdl_uri: str,
        split_circuit_types: bool,
        api_uri: Optional[str] = None,
        api_port: Optional[int] = None,
    ) -> None:
        self.component_name = component_name
        self.verbose_name = verbose_name
        self.version = version
        self.circuit = circuit
        self.ns_map = ns_map
        self.wsdl_uri = wsdl_uri
        self.split_circuit_types = split_circuit_types

        self.api_url = api_uri
        if api_port:
            self.api_url += f':{api_port}'


class VetisAMSService(BaseVetisService):
    """Сервис по работе со системой обработки заявок.

    Для подробного ознакомления см.
    https://help.vetrf.ru/wiki/Подсистема_обработки_заявок_в_Ветис.API
    """

    def __init__(self, *args, service_id: Optional[str] = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.service_id = service_id


class VetisRegistryService(BaseVetisService):
    """Сервис по работе со справочной системой."""

    _operations: Optional[Tuple[Type[RegistryOperation], ...]]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
