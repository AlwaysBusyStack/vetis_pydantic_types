import uuid
from typing import Optional, Union, Coroutine, Any

from requests.auth import HTTPBasicAuth
from xsdata.models.datatype import XmlDateTime

from vetis_pydantic_types.base import VetisAMSClient, VetisCircuitEnum, VetisRegistryClient
from vetis_pydantic_types.mercury.types import ApplicationManagementServicePortTypeReceiveApplicationResult, \
    ApplicationManagementServicePortTypeSubmitApplicationRequest, GetApplicableUserAuthorityListRequest, \
    GetApplicableUserAuthorityListResponse
from vetis_pydantic_types.mercury.services import ams_test_service, ams_productive_service, enterprise_test_service, \
    enterprise_productive_service
from requests.auth import HTTPBasicAuth
import asyncio

from vetis_pydantic_types.mercury.types.registry_ws_definitions_v2_1 import GetActivityLocationListRequest, \
    GetActivityLocationListResponse


class MercuryAMSClient(VetisAMSClient):
    def __init__(
        self,
        circuit: VetisCircuitEnum,
        api_key: str,
        auth: HTTPBasicAuth,
        timeout: Optional[int] = None,
        receive_timeout: Optional[int] = None,
    ):
        super().__init__(
            service=(
                ams_test_service
                if circuit == VetisCircuitEnum.TEST
                else ams_productive_service
            ),
            api_key=api_key,
            auth=auth,
            # submit_operation_type=[pilot|production][.]ApplicationManagementServicePortTypeSubmitApplicationRequest,
            # receive_operation_type=[pilot|production][.]ApplicationManagementServicePortTypeReceiveApplicationResult,
            timeout=timeout,
            receive_timeout=receive_timeout,
        )

        self.circuit = circuit

    def get_applicable_user_authority_list_request(
        self,
        data: GetApplicableUserAuthorityListRequest,
        issuer_id: str,
        issue_date: Optional[XmlDateTime] = None,
        receive_timeout: Optional[int] = None,
        **headers,
    ) -> Union[
        GetApplicableUserAuthorityListResponse,
        Coroutine[Any, Any, GetApplicableUserAuthorityListResponse],
    ]:
        return self.submit_and_wait_for_result(
            application=data,
            issuer_id=issuer_id,
            issue_date=issue_date,
            receive_timeout=receive_timeout,
            **headers,
        )

# Стандарт
from vetis_pydantic_types.mercury.types import enterprise_service_v2_1_production as enterprise_production
from vetis_pydantic_types.mercury.types import enterprise_service_v2_1_pilot as enterprise_pilot
# Для SPLIT_TYPES == True
# from vetis_pydantic_types.mercury.types.production import enterprise_service_v2_1_production as enterprise_production
# from vetis_pydantic_types.mercury.types.pilot import enterprise_service_v2_1_pilot as enterprise_pilot

class EnterpriseClient(VetisRegistryClient):
    def __init__(
        self,
        circuit: VetisCircuitEnum,
        auth: HTTPBasicAuth,
        timeout: Optional[int] = None,
    ):
        super().__init__(
            service=(
                ams_test_service
                if circuit == VetisCircuitEnum.TEST
                else ams_productive_service
            ),
            auth=auth,
            timeout=timeout,
        )

        self.circuit = circuit
        self.GetActivityLocationListOperation = (
            enterprise_pilot.EnterpriseServicePortTypeGetActivityLocationList
            if self.circuit == VetisCircuitEnum.TEST
            else enterprise_production.EnterpriseServicePortTypeGetActivityLocationList
        )

    def get_activity_location_list(
        self,
        data: GetActivityLocationListRequest,
        **headers,
    ) -> Union[
        GetActivityLocationListResponse,
        Coroutine[Any, Any, GetActivityLocationListResponse],
    ]:
        return self.GetActivityLocationListOperation(self).send(
            request=data,
            **headers,
        )

test = DictionaryServicePortTypeGetDiseaseByGuid
