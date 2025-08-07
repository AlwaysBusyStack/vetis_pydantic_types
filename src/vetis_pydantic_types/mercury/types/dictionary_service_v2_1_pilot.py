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
    GetDiseaseByGuidRequest,
    GetDiseaseByGuidResponse,
    GetDiseaseByUuidRequest,
    GetDiseaseByUuidResponse,
    GetDiseaseChangesListRequest,
    GetDiseaseChangesListResponse,
    GetDiseaseListRequest,
    GetDiseaseListResponse,
    GetPurposeByGuidRequest,
    GetPurposeByGuidResponse,
    GetPurposeByUuidRequest,
    GetPurposeByUuidResponse,
    GetPurposeChangesListRequest,
    GetPurposeChangesListResponse,
    GetPurposeListRequest,
    GetPurposeListResponse,
    GetResearchMethodByGuidRequest,
    GetResearchMethodByGuidResponse,
    GetResearchMethodByUuidRequest,
    GetResearchMethodByUuidResponse,
    GetResearchMethodChangesListRequest,
    GetResearchMethodChangesListResponse,
    GetResearchMethodListRequest,
    GetResearchMethodListResponse,
    GetUnitByGuidRequest,
    GetUnitByGuidResponse,
    GetUnitByUuidRequest,
    GetUnitByUuidResponse,
    GetUnitChangesListRequest,
    GetUnitChangesListResponse,
    GetUnitListRequest,
    GetUnitListResponse,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/registry/dictionary/service/v2"


class DictionaryServicePortTypeGetDiseaseByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_disease_by_guid_request: GetDiseaseByGuidRequest = field(
        metadata={
            "name": "getDiseaseByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetDiseaseByGuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetDiseaseByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_disease_by_uuid_request: GetDiseaseByUuidRequest = field(
        metadata={
            "name": "getDiseaseByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetDiseaseByUuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetDiseaseChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_disease_changes_list_request: GetDiseaseChangesListRequest = field(
        metadata={
            "name": "getDiseaseChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetDiseaseChangesListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetDiseaseListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_disease_list_request: GetDiseaseListRequest = field(
        metadata={
            "name": "getDiseaseListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetDiseaseListOutputBodyFaultDetail(BaseModel):
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


class DictionaryServicePortTypeGetPurposeByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_purpose_by_guid_request: GetPurposeByGuidRequest = field(
        metadata={
            "name": "getPurposeByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetPurposeByGuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetPurposeByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_purpose_by_uuid_request: GetPurposeByUuidRequest = field(
        metadata={
            "name": "getPurposeByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetPurposeByUuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetPurposeChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_purpose_changes_list_request: GetPurposeChangesListRequest = field(
        metadata={
            "name": "getPurposeChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetPurposeChangesListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetPurposeListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_purpose_list_request: GetPurposeListRequest = field(
        metadata={
            "name": "getPurposeListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetPurposeListOutputBodyFaultDetail(BaseModel):
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


class DictionaryServicePortTypeGetResearchMethodByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_research_method_by_guid_request: GetResearchMethodByGuidRequest = field(
        metadata={
            "name": "getResearchMethodByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetResearchMethodByGuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetResearchMethodByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_research_method_by_uuid_request: GetResearchMethodByUuidRequest = field(
        metadata={
            "name": "getResearchMethodByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetResearchMethodByUuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetResearchMethodChangesListInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_research_method_changes_list_request: GetResearchMethodChangesListRequest = field(
        metadata={
            "name": "getResearchMethodChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetResearchMethodChangesListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetResearchMethodListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_research_method_list_request: GetResearchMethodListRequest = field(
        metadata={
            "name": "getResearchMethodListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetResearchMethodListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetUnitByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_unit_by_guid_request: GetUnitByGuidRequest = field(
        metadata={
            "name": "getUnitByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetUnitByGuidOutputBodyFaultDetail(BaseModel):
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


class DictionaryServicePortTypeGetUnitByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_unit_by_uuid_request: GetUnitByUuidRequest = field(
        metadata={
            "name": "getUnitByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetUnitByUuidOutputBodyFaultDetail(BaseModel):
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


class DictionaryServicePortTypeGetUnitChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_unit_changes_list_request: GetUnitChangesListRequest = field(
        metadata={
            "name": "getUnitChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetUnitChangesListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetUnitListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_unit_list_request: GetUnitListRequest = field(
        metadata={
            "name": "getUnitListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetUnitListOutputBodyFaultDetail(BaseModel):
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


class DictionaryServicePortTypeGetDiseaseByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetDiseaseByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetDiseaseByGuidOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetDiseaseByGuidOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class DictionaryServicePortTypeGetDiseaseByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetDiseaseByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetDiseaseByUuidOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetDiseaseByUuidOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class DictionaryServicePortTypeGetDiseaseChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetDiseaseChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetDiseaseChangesListOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetDiseaseChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetDiseaseListInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetDiseaseListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetDiseaseListOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetDiseaseListOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class DictionaryServicePortTypeGetPurposeByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetPurposeByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetPurposeByGuidOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetPurposeByGuidOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class DictionaryServicePortTypeGetPurposeByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetPurposeByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetPurposeByUuidOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetPurposeByUuidOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class DictionaryServicePortTypeGetPurposeChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetPurposeChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetPurposeChangesListOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetPurposeChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetPurposeListInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetPurposeListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetPurposeListOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetPurposeListOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class DictionaryServicePortTypeGetResearchMethodByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetResearchMethodByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetResearchMethodByGuidOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetResearchMethodByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetResearchMethodByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetResearchMethodByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetResearchMethodByUuidOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetResearchMethodByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetResearchMethodChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetResearchMethodChangesListInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetResearchMethodChangesListOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetResearchMethodChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetResearchMethodListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetResearchMethodListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetResearchMethodListOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetResearchMethodListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetUnitByGuidInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetUnitByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetUnitByGuidOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetUnitByGuidOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class DictionaryServicePortTypeGetUnitByUuidInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetUnitByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetUnitByUuidOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetUnitByUuidOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class DictionaryServicePortTypeGetUnitChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetUnitChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetUnitChangesListOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetUnitChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetUnitListInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetUnitListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetUnitListOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetUnitListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetDiseaseByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_disease_by_guid_response: Optional[GetDiseaseByGuidResponse] = field(
        default=None,
        metadata={
            "name": "getDiseaseByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetDiseaseByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetDiseaseByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_disease_by_uuid_response: Optional[GetDiseaseByUuidResponse] = field(
        default=None,
        metadata={
            "name": "getDiseaseByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetDiseaseByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetDiseaseChangesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_disease_changes_list_response: Optional[
        GetDiseaseChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getDiseaseChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetDiseaseChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetDiseaseListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_disease_list_response: Optional[GetDiseaseListResponse] = field(
        default=None,
        metadata={
            "name": "getDiseaseListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[DictionaryServicePortTypeGetDiseaseListOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class DictionaryServicePortTypeGetPurposeByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_purpose_by_guid_response: Optional[GetPurposeByGuidResponse] = field(
        default=None,
        metadata={
            "name": "getPurposeByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetPurposeByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetPurposeByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_purpose_by_uuid_response: Optional[GetPurposeByUuidResponse] = field(
        default=None,
        metadata={
            "name": "getPurposeByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetPurposeByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetPurposeChangesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_purpose_changes_list_response: Optional[
        GetPurposeChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getPurposeChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetPurposeChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetPurposeListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_purpose_list_response: Optional[GetPurposeListResponse] = field(
        default=None,
        metadata={
            "name": "getPurposeListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[DictionaryServicePortTypeGetPurposeListOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class DictionaryServicePortTypeGetResearchMethodByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_research_method_by_guid_response: Optional[
        GetResearchMethodByGuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getResearchMethodByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetResearchMethodByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetResearchMethodByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_research_method_by_uuid_response: Optional[
        GetResearchMethodByUuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getResearchMethodByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetResearchMethodByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetResearchMethodChangesListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_research_method_changes_list_response: Optional[
        GetResearchMethodChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getResearchMethodChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetResearchMethodChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetResearchMethodListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_research_method_list_response: Optional[
        GetResearchMethodListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getResearchMethodListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetResearchMethodListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetUnitByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_unit_by_guid_response: Optional[GetUnitByGuidResponse] = field(
        default=None,
        metadata={
            "name": "getUnitByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[DictionaryServicePortTypeGetUnitByGuidOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class DictionaryServicePortTypeGetUnitByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_unit_by_uuid_response: Optional[GetUnitByUuidResponse] = field(
        default=None,
        metadata={
            "name": "getUnitByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[DictionaryServicePortTypeGetUnitByUuidOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class DictionaryServicePortTypeGetUnitChangesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_unit_changes_list_response: Optional[GetUnitChangesListResponse] = (
        field(
            default=None,
            metadata={
                "name": "getUnitChangesListResponse",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
            },
        )
    )
    fault: Optional[
        DictionaryServicePortTypeGetUnitChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetUnitListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_unit_list_response: Optional[GetUnitListResponse] = field(
        default=None,
        metadata={
            "name": "getUnitListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[DictionaryServicePortTypeGetUnitListOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class DictionaryServicePortTypeGetDiseaseByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetDiseaseByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetDiseaseByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetDiseaseByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetDiseaseChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetDiseaseChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetDiseaseListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetDiseaseListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetPurposeByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetPurposeByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetPurposeByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetPurposeByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetPurposeChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetPurposeChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetPurposeListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetPurposeListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetResearchMethodByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetResearchMethodByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetResearchMethodByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetResearchMethodByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetResearchMethodChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetResearchMethodChangesListOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetResearchMethodListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetResearchMethodListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetUnitByGuidOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetUnitByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetUnitByUuidOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetUnitByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetUnitChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetUnitChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetUnitListOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetUnitListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetDiseaseByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetDiseaseByGuid"
    input = DictionaryServicePortTypeGetDiseaseByGuidInput
    output = DictionaryServicePortTypeGetDiseaseByGuidOutput


class DictionaryServicePortTypeGetDiseaseByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetDiseaseByUuid"
    input = DictionaryServicePortTypeGetDiseaseByUuidInput
    output = DictionaryServicePortTypeGetDiseaseByUuidOutput


class DictionaryServicePortTypeGetDiseaseChangesList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetDiseaseChangesList"
    input = DictionaryServicePortTypeGetDiseaseChangesListInput
    output = DictionaryServicePortTypeGetDiseaseChangesListOutput


class DictionaryServicePortTypeGetDiseaseList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetDiseaseList"
    input = DictionaryServicePortTypeGetDiseaseListInput
    output = DictionaryServicePortTypeGetDiseaseListOutput


class DictionaryServicePortTypeGetPurposeByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetPurposeByGuid"
    input = DictionaryServicePortTypeGetPurposeByGuidInput
    output = DictionaryServicePortTypeGetPurposeByGuidOutput


class DictionaryServicePortTypeGetPurposeByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetPurposeByUuid"
    input = DictionaryServicePortTypeGetPurposeByUuidInput
    output = DictionaryServicePortTypeGetPurposeByUuidOutput


class DictionaryServicePortTypeGetPurposeChangesList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetPurposeChangesList"
    input = DictionaryServicePortTypeGetPurposeChangesListInput
    output = DictionaryServicePortTypeGetPurposeChangesListOutput


class DictionaryServicePortTypeGetPurposeList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetPurposeList"
    input = DictionaryServicePortTypeGetPurposeListInput
    output = DictionaryServicePortTypeGetPurposeListOutput


class DictionaryServicePortTypeGetResearchMethodByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetResearchMethodByGuid"
    input = DictionaryServicePortTypeGetResearchMethodByGuidInput
    output = DictionaryServicePortTypeGetResearchMethodByGuidOutput


class DictionaryServicePortTypeGetResearchMethodByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetResearchMethodByUuid"
    input = DictionaryServicePortTypeGetResearchMethodByUuidInput
    output = DictionaryServicePortTypeGetResearchMethodByUuidOutput


class DictionaryServicePortTypeGetResearchMethodChangesList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetResearchMethodChangesList"
    input = DictionaryServicePortTypeGetResearchMethodChangesListInput
    output = DictionaryServicePortTypeGetResearchMethodChangesListOutput


class DictionaryServicePortTypeGetResearchMethodList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetResearchMethodList"
    input = DictionaryServicePortTypeGetResearchMethodListInput
    output = DictionaryServicePortTypeGetResearchMethodListOutput


class DictionaryServicePortTypeGetUnitByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetUnitByGuid"
    input = DictionaryServicePortTypeGetUnitByGuidInput
    output = DictionaryServicePortTypeGetUnitByGuidOutput


class DictionaryServicePortTypeGetUnitByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetUnitByUuid"
    input = DictionaryServicePortTypeGetUnitByUuidInput
    output = DictionaryServicePortTypeGetUnitByUuidOutput


class DictionaryServicePortTypeGetUnitChangesList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetUnitChangesList"
    input = DictionaryServicePortTypeGetUnitChangesListInput
    output = DictionaryServicePortTypeGetUnitChangesListOutput


class DictionaryServicePortTypeGetUnitList(RegistryOperation):
    style = "document"
    location = (
        "https://api2.vetrf.ru:8002/platform/services/2.1/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetUnitList"
    input = DictionaryServicePortTypeGetUnitListInput
    output = DictionaryServicePortTypeGetUnitListOutput
