from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict

from vetis_pydantic_types.base import BaseIOOperation, RegistryOperation
from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.herriot.types.pilot.base_ws_definitions_v2_1 import (
    EntityNotFoundFault,
    IncorrectRequestFault,
    InternalServiceFault,
    OffsetOutOfRangeFault,
)
from vetis_pydantic_types.herriot.types.pilot.registry_ws_definitions_v2_5 import (
    GetBesupervisedObjectListRequest,
    GetBesupervisedObjectListResponse,
    GetBusinessEntityByGuidRequest,
    GetBusinessEntityByGuidResponse,
    GetBusinessEntityByUuidRequest,
    GetBusinessEntityByUuidResponse,
    GetBusinessEntityChangesListRequest,
    GetBusinessEntityChangesListResponse,
    GetBusinessEntityListRequest,
    GetBusinessEntityListResponse,
    GetEnterpriseByGuidRequest,
    GetEnterpriseByGuidResponse,
    GetEnterpriseByUuidRequest,
    GetEnterpriseByUuidResponse,
    GetRussianEnterpriseChangesListRequest,
    GetRussianEnterpriseChangesListResponse,
    GetRussianEnterpriseListRequest,
    GetRussianEnterpriseListResponse,
    GetSupervisedObjectActivityListRequest,
    GetSupervisedObjectActivityListResponse,
    GetSupervisedObjectByGuidRequest,
    GetSupervisedObjectByGuidResponse,
    GetSupervisedObjectByUuidRequest,
    GetSupervisedObjectByUuidResponse,
    GetSupervisedObjectTypeListRequest,
    GetSupervisedObjectTypeListResponse,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/registry/enterprise/service/v3"


class EnterpriseServicePortTypeGetBesupervisedObjectListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_besupervised_object_list_request: GetBesupervisedObjectListRequest = field(
        metadata={
            "name": "getBESupervisedObjectListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetBesupervisedObjectListOutputBodyFaultDetail(
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


class EnterpriseServicePortTypeGetSupervisedObjectActivityListInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_supervised_object_activity_list_request: GetSupervisedObjectActivityListRequest = field(
        metadata={
            "name": "getSupervisedObjectActivityListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectActivityListOutputBodyFaultDetail(
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


class EnterpriseServicePortTypeGetSupervisedObjectByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_supervised_object_by_guid_request: GetSupervisedObjectByGuidRequest = field(
        metadata={
            "name": "getSupervisedObjectByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectByGuidOutputBodyFaultDetail(
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


class EnterpriseServicePortTypeGetSupervisedObjectByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_supervised_object_by_uuid_request: GetSupervisedObjectByUuidRequest = field(
        metadata={
            "name": "getSupervisedObjectByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectByUuidOutputBodyFaultDetail(
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


class EnterpriseServicePortTypeGetSupervisedObjectTypeListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_supervised_object_type_list_request: GetSupervisedObjectTypeListRequest = field(
        metadata={
            "name": "getSupervisedObjectTypeListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectTypeListOutputBodyFaultDetail(
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


class EnterpriseServicePortTypeGetBesupervisedObjectListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBesupervisedObjectListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetBesupervisedObjectListOutputBodyFault(
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
    detail: EnterpriseServicePortTypeGetBesupervisedObjectListOutputBodyFaultDetail = field(
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


class EnterpriseServicePortTypeGetSupervisedObjectActivityListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetSupervisedObjectActivityListInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class EnterpriseServicePortTypeGetSupervisedObjectActivityListOutputBodyFault(
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
    detail: EnterpriseServicePortTypeGetSupervisedObjectActivityListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetSupervisedObjectByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectByGuidOutputBodyFault(
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
    detail: EnterpriseServicePortTypeGetSupervisedObjectByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetSupervisedObjectByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectByUuidOutputBodyFault(
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
    detail: EnterpriseServicePortTypeGetSupervisedObjectByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectTypeListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetSupervisedObjectTypeListInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class EnterpriseServicePortTypeGetSupervisedObjectTypeListOutputBodyFault(
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
    detail: EnterpriseServicePortTypeGetSupervisedObjectTypeListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class EnterpriseServicePortTypeGetBesupervisedObjectListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_besupervised_object_list_response: Optional[
        GetBesupervisedObjectListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getBESupervisedObjectListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetBesupervisedObjectListOutputBodyFault
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


class EnterpriseServicePortTypeGetSupervisedObjectActivityListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_supervised_object_activity_list_response: Optional[
        GetSupervisedObjectActivityListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getSupervisedObjectActivityListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetSupervisedObjectActivityListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetSupervisedObjectByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_supervised_object_by_guid_response: Optional[
        GetSupervisedObjectByGuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getSupervisedObjectByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetSupervisedObjectByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetSupervisedObjectByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_supervised_object_by_uuid_response: Optional[
        GetSupervisedObjectByUuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getSupervisedObjectByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetSupervisedObjectByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetSupervisedObjectTypeListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_supervised_object_type_list_response: Optional[
        GetSupervisedObjectTypeListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getSupervisedObjectTypeListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        EnterpriseServicePortTypeGetSupervisedObjectTypeListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class EnterpriseServicePortTypeGetBesupervisedObjectListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetBesupervisedObjectListOutputBody = field(
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


class EnterpriseServicePortTypeGetSupervisedObjectActivityListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetSupervisedObjectActivityListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetSupervisedObjectByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetSupervisedObjectByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class EnterpriseServicePortTypeGetSupervisedObjectTypeListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: EnterpriseServicePortTypeGetSupervisedObjectTypeListOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class EnterpriseServicePortTypeGetBesupervisedObjectList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetBESupervisedObjectList"
    input = EnterpriseServicePortTypeGetBesupervisedObjectListInput
    output = EnterpriseServicePortTypeGetBesupervisedObjectListOutput


class EnterpriseServicePortTypeGetBusinessEntityByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetBusinessEntityByGuid"
    input = EnterpriseServicePortTypeGetBusinessEntityByGuidInput
    output = EnterpriseServicePortTypeGetBusinessEntityByGuidOutput


class EnterpriseServicePortTypeGetBusinessEntityByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetBusinessEntityByUuid"
    input = EnterpriseServicePortTypeGetBusinessEntityByUuidInput
    output = EnterpriseServicePortTypeGetBusinessEntityByUuidOutput


class EnterpriseServicePortTypeGetBusinessEntityChangesList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetBusinessEntityChangesList"
    input = EnterpriseServicePortTypeGetBusinessEntityChangesListInput
    output = EnterpriseServicePortTypeGetBusinessEntityChangesListOutput


class EnterpriseServicePortTypeGetBusinessEntityList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetBusinessEntityList"
    input = EnterpriseServicePortTypeGetBusinessEntityListInput
    output = EnterpriseServicePortTypeGetBusinessEntityListOutput


class EnterpriseServicePortTypeGetEnterpriseByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetEnterpriseByGuid"
    input = EnterpriseServicePortTypeGetEnterpriseByGuidInput
    output = EnterpriseServicePortTypeGetEnterpriseByGuidOutput


class EnterpriseServicePortTypeGetEnterpriseByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetEnterpriseByUuid"
    input = EnterpriseServicePortTypeGetEnterpriseByUuidInput
    output = EnterpriseServicePortTypeGetEnterpriseByUuidOutput


class EnterpriseServicePortTypeGetRussianEnterpriseChangesList(
    RegistryOperation
):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetRussianEnterpriseChangesList"
    input = EnterpriseServicePortTypeGetRussianEnterpriseChangesListInput
    output = EnterpriseServicePortTypeGetRussianEnterpriseChangesListOutput


class EnterpriseServicePortTypeGetRussianEnterpriseList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetRussianEnterpriseList"
    input = EnterpriseServicePortTypeGetRussianEnterpriseListInput
    output = EnterpriseServicePortTypeGetRussianEnterpriseListOutput


class EnterpriseServicePortTypeGetSupervisedObjectActivityList(
    RegistryOperation
):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetSupervisedObjectActivityList"
    input = EnterpriseServicePortTypeGetSupervisedObjectActivityListInput
    output = EnterpriseServicePortTypeGetSupervisedObjectActivityListOutput


class EnterpriseServicePortTypeGetSupervisedObjectByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetSupervisedObjectByGuid"
    input = EnterpriseServicePortTypeGetSupervisedObjectByGuidInput
    output = EnterpriseServicePortTypeGetSupervisedObjectByGuidOutput


class EnterpriseServicePortTypeGetSupervisedObjectByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetSupervisedObjectByUuid"
    input = EnterpriseServicePortTypeGetSupervisedObjectByUuidInput
    output = EnterpriseServicePortTypeGetSupervisedObjectByUuidOutput


class EnterpriseServicePortTypeGetSupervisedObjectTypeList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/EnterpriseService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetSupervisedObjectTypeList"
    input = EnterpriseServicePortTypeGetSupervisedObjectTypeListInput
    output = EnterpriseServicePortTypeGetSupervisedObjectTypeListOutput
