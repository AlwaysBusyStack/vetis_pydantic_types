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

        self._types = None

    @property
    def types(self) -> Optional[ModuleType]:
        if not self._types:
            with suppress(ImportError):
                package_parts = [
                    self.__module__.rsplit('.', maxsplit=2)[0],
                    self.component_name,
                ]
                if self.split_circuit_types:
                    package_parts.append(self.circuit.value)

                self._types = import_module(
                    f'.{TYPES_PACKAGE}',
                    '.'.join(package_parts)
                )

        return self._types


class VetisAMSService(BaseVetisService):
    """Сервис по работе со системой обработки заявок.

    Для подробного ознакомления см.
    https://help.vetrf.ru/wiki/Подсистема_обработки_заявок_в_Ветис.API
    """

    _application_data_to_result_map: Dict[ApplicationRequest, ApplicationResponse]
    submit_operation_type: Optional[Type[SubmitApplicationRequestOperation]]
    receive_operation_type: Optional[Type[ReceiveApplicationResultOperation]]

    def __init__(self, *args, service_id: Optional[str] = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.service_id = service_id

        if self.types:
            self.submit_operation_type = getattr(
                self.types, 'ApplicationManagementServicePortTypeSubmitApplicationRequest'
            )
            self.receive_operation_type = getattr(
                self.types, 'ApplicationManagementServicePortTypeReceiveApplicationResult'
            )

        self._application_data_to_result_map = None

    @property
    def application_data_to_result_map(self) -> Dict[ApplicationRequest, ApplicationResponse]:
        if not self._application_data_to_result_map and self.types:
            application_data_types = list(filter(
                lambda cls: issubclass(cls, ApplicationRequest),
                self.types.__dir__(),
            ))
            application_result_types = list(filter(
                lambda cls: issubclass(cls, ApplicationResponse),
                self.types.__dir__(),
            ))

            self._application_data_to_result_map = dict(zip(
                application_data_types,
                application_result_types,
            ))

        return self._application_data_to_result_map


class VetisDictionaryService(BaseVetisService):
    """Сервис по работе со справочной системой."""

    _operations: Optional[Tuple[Type[RegistryOperation], ...]]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @property
    def operations(self) -> Tuple[Type[RegistryOperation], ...]:
        if not self._operations:
            self._operations = tuple()

        return self._operations
