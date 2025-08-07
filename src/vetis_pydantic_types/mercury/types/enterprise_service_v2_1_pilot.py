from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict

from vetis_pydantic_types.base import BaseIOOperation, RegistryOperation
from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.mercury.types.base_ws_definitions_v2_0 import (
    EntityNotFoundFault,
    IncorrectRequestFault,
    InternalServiceFault,
    OffsetOutOfRangeFault,
)
from vetis_pydantic_types.mercury.types.registry_ws_definitions_v2_1 import (
    GetActivityLocationListRequest,
    GetActivityLocationListResponse,
    GetBusinessEntityByGuidRequest,
    GetBusinessEntityByGuidResponse,
    GetBusinessEntityByUuidRequest,
    GetBusinessEntityByUuidResponse,
    GetBusinessEntityChangesListRequest,
    GetBusinessEntityChangesListResponse,
    GetBusinessEntityListRequest,
    GetBusinessEntityListResponse,
    GetBusinessMemberByGlnrequest,
    GetBusinessMemberByGlnresponse,
    GetEnterpriseByGuidRequest,
    GetEnterpriseByGuidResponse,
    GetEnterpriseByUuidRequest,
    GetEnterpriseByUuidResponse,
    GetForeignEnterpriseChangesListRequest,
    GetForeignEnterpriseChangesListResponse,
    GetForeignEnterpriseListRequest,
    GetForeignEnterpriseListResponse,
    GetRussianEnterpriseChangesListRequest,
    GetRussianEnterpriseChangesListResponse,
    GetRussianEnterpriseListRequest,
    GetRussianEnterpriseListResponse,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/registry/enterprise/service/v2"


class EnterpriseServicePortTypeGetActivityLocationListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_activity_location_list_request: GetActivityLocationListRequest = field(
        metadata={
            "name": "getActivityLocationListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetActivityLocationListOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetBusinessEntityByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_business_entity_by_guid_request: GetBusinessEntityByGuidRequest = field(
        metadata={
            "name": "getBusinessEntityByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityByGuidOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    entity_not_found_fault: Optional[EntityNotFoundFault] = field(
        default=None,
        metadata={
            "name": "entityNotFoundFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetBusinessEntityByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_business_entity_by_uuid_request: GetBusinessEntityByUuidRequest = field(
        metadata={
            "name": "getBusinessEntityByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityByUuidOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    entity_not_found_fault: Optional[EntityNotFoundFault] = field(
        default=None,
        metadata={
            "name": "entityNotFoundFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetBusinessEntityChangesListInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_business_entity_changes_list_request: GetBusinessEntityChangesListRequest = field(
        metadata={
            "name": "getBusinessEntityChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityChangesListOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetBusinessEntityListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_business_entity_list_request: GetBusinessEntityListRequest = field(
        metadata={
            "name": "getBusinessEntityListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityListOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetBusinessMemberByGlnInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_business_member_by_glnrequest: GetBusinessMemberByGlnrequest = field(
        metadata={
            "name": "getBusinessMemberByGLNRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetBusinessMemberByGlnOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    entity_not_found_fault: Optional[EntityNotFoundFault] = field(
        default=None,
        metadata={
            "name": "entityNotFoundFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetEnterpriseByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_enterprise_by_guid_request: GetEnterpriseByGuidRequest = field(
        metadata={
            "name": "getEnterpriseByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetEnterpriseByGuidOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    entity_not_found_fault: Optional[EntityNotFoundFault] = field(
        default=None,
        metadata={
            "name": "entityNotFoundFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetEnterpriseByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_enterprise_by_uuid_request: GetEnterpriseByUuidRequest = field(
        metadata={
            "name": "getEnterpriseByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetEnterpriseByUuidOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    entity_not_found_fault: Optional[EntityNotFoundFault] = field(
        default=None,
        metadata={
            "name": "entityNotFoundFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetForeignEnterpriseChangesListInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_foreign_enterprise_changes_list_request: GetForeignEnterpriseChangesListRequest = field(
        metadata={
            "name": "getForeignEnterpriseChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetForeignEnterpriseChangesListOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetForeignEnterpriseListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_foreign_enterprise_list_request: GetForeignEnterpriseListRequest = field(
        metadata={
            "name": "getForeignEnterpriseListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetForeignEnterpriseListOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetRussianEnterpriseChangesListInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_russian_enterprise_changes_list_request: GetRussianEnterpriseChangesListRequest = field(
        metadata={
            "name": "getRussianEnterpriseChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetRussianEnterpriseChangesListOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetRussianEnterpriseListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_russian_enterprise_list_request: GetRussianEnterpriseListRequest = field(
        metadata={
            "name": "getRussianEnterpriseListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetRussianEnterpriseListOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    internal_service_fault: Optional[InternalServiceFault] = field(
        default=None,
        metadata={
            "name": "internalServiceFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    incorrect_request_fault: Optional[IncorrectRequestFault] = field(
        default=None,
        metadata={
            "name": "incorrectRequestFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class EnterpriseServicePortTypeGetActivityLocationListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetActivityLocationListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetActivityLocationListOutputBodyFault(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetActivityLocationListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBusinessEntityByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityByGuidOutputBodyFault(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetBusinessEntityByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBusinessEntityByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityByUuidOutputBodyFault(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetBusinessEntityByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBusinessEntityChangesListInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class EnterpriseServicePortTypeGetBusinessEntityChangesListOutputBodyFault(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetBusinessEntityChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBusinessEntityListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityListOutputBodyFault(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetBusinessEntityListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetBusinessMemberByGlnInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBusinessMemberByGlnInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetBusinessMemberByGlnOutputBodyFault(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetBusinessMemberByGlnOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetEnterpriseByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetEnterpriseByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetEnterpriseByGuidOutputBodyFault(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetEnterpriseByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetEnterpriseByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetEnterpriseByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetEnterpriseByUuidOutputBodyFault(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetEnterpriseByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetForeignEnterpriseChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetForeignEnterpriseChangesListInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class EnterpriseServicePortTypeGetForeignEnterpriseChangesListOutputBodyFault(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetForeignEnterpriseChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetForeignEnterpriseListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetForeignEnterpriseListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetForeignEnterpriseListOutputBodyFault(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetForeignEnterpriseListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetRussianEnterpriseChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetRussianEnterpriseChangesListInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class EnterpriseServicePortTypeGetRussianEnterpriseChangesListOutputBodyFault(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetRussianEnterpriseChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetRussianEnterpriseListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetRussianEnterpriseListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetRussianEnterpriseListOutputBodyFault(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    faultactor: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detail: EnterpriseServicePortTypeGetRussianEnterpriseListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetActivityLocationListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_activity_location_list_response: Optional[
        GetActivityLocationListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getActivityLocationListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetActivityLocationListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetBusinessEntityByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_business_entity_by_guid_response: Optional[
        GetBusinessEntityByGuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getBusinessEntityByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetBusinessEntityByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetBusinessEntityByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_business_entity_by_uuid_response: Optional[
        GetBusinessEntityByUuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getBusinessEntityByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetBusinessEntityByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetBusinessEntityChangesListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_business_entity_changes_list_response: Optional[
        GetBusinessEntityChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getBusinessEntityChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetBusinessEntityChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetBusinessEntityListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_business_entity_list_response: Optional[
        GetBusinessEntityListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getBusinessEntityListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetBusinessEntityListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetBusinessMemberByGlnOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_business_member_by_glnresponse: Optional[
        GetBusinessMemberByGlnresponse
    ] = field(
        default=None,
        metadata={
            "name": "getBusinessMemberByGLNResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetBusinessMemberByGlnOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetEnterpriseByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_enterprise_by_guid_response: Optional[GetEnterpriseByGuidResponse] = (
        field(
            default=None,
            metadata={
                "name": "getEnterpriseByGuidResponse",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
            },
        )
    )
    fault: Optional[
        EnterpriseServicePortTypeGetEnterpriseByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetEnterpriseByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_enterprise_by_uuid_response: Optional[GetEnterpriseByUuidResponse] = (
        field(
            default=None,
            metadata={
                "name": "getEnterpriseByUuidResponse",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
            },
        )
    )
    fault: Optional[
        EnterpriseServicePortTypeGetEnterpriseByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetForeignEnterpriseChangesListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_foreign_enterprise_changes_list_response: Optional[
        GetForeignEnterpriseChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getForeignEnterpriseChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetForeignEnterpriseChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetForeignEnterpriseListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_foreign_enterprise_list_response: Optional[
        GetForeignEnterpriseListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getForeignEnterpriseListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetForeignEnterpriseListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetRussianEnterpriseChangesListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_russian_enterprise_changes_list_response: Optional[
        GetRussianEnterpriseChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getRussianEnterpriseChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetRussianEnterpriseChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetRussianEnterpriseListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_russian_enterprise_list_response: Optional[
        GetRussianEnterpriseListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getRussianEnterpriseListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetRussianEnterpriseListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetActivityLocationListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetActivityLocationListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBusinessEntityByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBusinessEntityByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetBusinessEntityChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBusinessEntityChangesListOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class EnterpriseServicePortTypeGetBusinessEntityListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBusinessEntityListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetBusinessMemberByGlnOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBusinessMemberByGlnOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetEnterpriseByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetEnterpriseByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetEnterpriseByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetEnterpriseByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetForeignEnterpriseChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetForeignEnterpriseChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetForeignEnterpriseListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetForeignEnterpriseListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetRussianEnterpriseChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetRussianEnterpriseChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetRussianEnterpriseListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetRussianEnterpriseListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetActivityLocationList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetActivityLocationList"
    input = EnterpriseServicePortTypeGetActivityLocationListInput
    output = EnterpriseServicePortTypeGetActivityLocationListOutput


class EnterpriseServicePortTypeGetBusinessEntityByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetBusinessEntityByGuid"
    input = EnterpriseServicePortTypeGetBusinessEntityByGuidInput
    output = EnterpriseServicePortTypeGetBusinessEntityByGuidOutput


class EnterpriseServicePortTypeGetBusinessEntityByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetBusinessEntityByUuid"
    input = EnterpriseServicePortTypeGetBusinessEntityByUuidInput
    output = EnterpriseServicePortTypeGetBusinessEntityByUuidOutput


class EnterpriseServicePortTypeGetBusinessEntityChangesList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetBusinessEntityChangesList"
    input = EnterpriseServicePortTypeGetBusinessEntityChangesListInput
    output = EnterpriseServicePortTypeGetBusinessEntityChangesListOutput


class EnterpriseServicePortTypeGetBusinessEntityList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetBusinessEntityList"
    input = EnterpriseServicePortTypeGetBusinessEntityListInput
    output = EnterpriseServicePortTypeGetBusinessEntityListOutput


class EnterpriseServicePortTypeGetBusinessMemberByGln(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetBusinessMemberByGLN"
    input = EnterpriseServicePortTypeGetBusinessMemberByGlnInput
    output = EnterpriseServicePortTypeGetBusinessMemberByGlnOutput


class EnterpriseServicePortTypeGetEnterpriseByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetEnterpriseByGuid"
    input = EnterpriseServicePortTypeGetEnterpriseByGuidInput
    output = EnterpriseServicePortTypeGetEnterpriseByGuidOutput


class EnterpriseServicePortTypeGetEnterpriseByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetEnterpriseByUuid"
    input = EnterpriseServicePortTypeGetEnterpriseByUuidInput
    output = EnterpriseServicePortTypeGetEnterpriseByUuidOutput


class EnterpriseServicePortTypeGetForeignEnterpriseChangesList(
    RegistryOperation
):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetForeignEnterpriseChangesList"
    input = EnterpriseServicePortTypeGetForeignEnterpriseChangesListInput
    output = EnterpriseServicePortTypeGetForeignEnterpriseChangesListOutput


class EnterpriseServicePortTypeGetForeignEnterpriseList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetForeignEnterpriseList"
    input = EnterpriseServicePortTypeGetForeignEnterpriseListInput
    output = EnterpriseServicePortTypeGetForeignEnterpriseListOutput


class EnterpriseServicePortTypeGetRussianEnterpriseChangesList(
    RegistryOperation
):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetRussianEnterpriseChangesList"
    input = EnterpriseServicePortTypeGetRussianEnterpriseChangesListInput
    output = EnterpriseServicePortTypeGetRussianEnterpriseChangesListOutput


class EnterpriseServicePortTypeGetRussianEnterpriseList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetRussianEnterpriseList"
    input = EnterpriseServicePortTypeGetRussianEnterpriseListInput
    output = EnterpriseServicePortTypeGetRussianEnterpriseListOutput
