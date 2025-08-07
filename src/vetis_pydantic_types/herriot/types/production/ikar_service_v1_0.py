from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict

from vetis_pydantic_types.base import BaseIOOperation, RegistryOperation
from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.herriot.types.production.base_ws_definitions_v2_1 import (
    EntityNotFoundFault,
    IncorrectRequestFault,
    InternalServiceFault,
    OffsetOutOfRangeFault,
)
from vetis_pydantic_types.herriot.types.production.registry_ws_definitions_v2_5 import (
    FindLocalityListByNameRequest,
    FindLocalityListByNameResponse,
    FindStreetListByNameRequest,
    FindStreetListByNameResponse,
    GetAllCountryListRequest,
    GetAllCountryListResponse,
    GetCountryByGuidRequest,
    GetCountryByGuidResponse,
    GetCountryByUuidRequest,
    GetCountryByUuidResponse,
    GetCountryChangesListRequest,
    GetCountryChangesListResponse,
    GetDistrictByGuidRequest,
    GetDistrictByGuidResponse,
    GetDistrictByUuidRequest,
    GetDistrictByUuidResponse,
    GetDistrictChangesListRequest,
    GetDistrictChangesListResponse,
    GetDistrictListByRegionRequest,
    GetDistrictListByRegionResponse,
    GetLocalityChangesListRequest,
    GetLocalityChangesListResponse,
    GetLocalityListByDistrictRequest,
    GetLocalityListByDistrictResponse,
    GetLocalityListByLocalityRequest,
    GetLocalityListByLocalityResponse,
    GetLocalityListByRegionRequest,
    GetLocalityListByRegionResponse,
    GetRegionByGuidRequest,
    GetRegionByGuidResponse,
    GetRegionByUuidRequest,
    GetRegionByUuidResponse,
    GetRegionChangesListRequest,
    GetRegionChangesListResponse,
    GetRegionListByCountryRequest,
    GetRegionListByCountryResponse,
    GetStreetChangesListRequest,
    GetStreetChangesListResponse,
    GetStreetListByLocalityRequest,
    GetStreetListByLocalityResponse,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/registry/ikar/service/v3"


class IkarServicePortTypeFindLocalityListByNameInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    find_locality_list_by_name_request: FindLocalityListByNameRequest = field(
        metadata={
            "name": "findLocalityListByNameRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeFindLocalityListByNameOutputBodyFaultDetail(
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
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class IkarServicePortTypeFindStreetListByNameInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    find_street_list_by_name_request: FindStreetListByNameRequest = field(
        metadata={
            "name": "findStreetListByNameRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeFindStreetListByNameOutputBodyFaultDetail(BaseModel):
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
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class IkarServicePortTypeGetAllCountryListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_all_country_list_request: GetAllCountryListRequest = field(
        metadata={
            "name": "getAllCountryListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetAllCountryListOutputBodyFaultDetail(BaseModel):
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


class IkarServicePortTypeGetCountryByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_country_by_guid_request: GetCountryByGuidRequest = field(
        metadata={
            "name": "getCountryByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetCountryByGuidOutputBodyFaultDetail(BaseModel):
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


class IkarServicePortTypeGetCountryByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_country_by_uuid_request: GetCountryByUuidRequest = field(
        metadata={
            "name": "getCountryByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetCountryByUuidOutputBodyFaultDetail(BaseModel):
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


class IkarServicePortTypeGetCountryChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_country_changes_list_request: GetCountryChangesListRequest = field(
        metadata={
            "name": "getCountryChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetCountryChangesListOutputBodyFaultDetail(BaseModel):
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


class IkarServicePortTypeGetDistrictByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_district_by_guid_request: GetDistrictByGuidRequest = field(
        metadata={
            "name": "getDistrictByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetDistrictByGuidOutputBodyFaultDetail(BaseModel):
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


class IkarServicePortTypeGetDistrictByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_district_by_uuid_request: GetDistrictByUuidRequest = field(
        metadata={
            "name": "getDistrictByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetDistrictByUuidOutputBodyFaultDetail(BaseModel):
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


class IkarServicePortTypeGetDistrictChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_district_changes_list_request: GetDistrictChangesListRequest = field(
        metadata={
            "name": "getDistrictChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetDistrictChangesListOutputBodyFaultDetail(
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


class IkarServicePortTypeGetDistrictListByRegionInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_district_list_by_region_request: GetDistrictListByRegionRequest = field(
        metadata={
            "name": "getDistrictListByRegionRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetDistrictListByRegionOutputBodyFaultDetail(
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
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class IkarServicePortTypeGetLocalityChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_locality_changes_list_request: GetLocalityChangesListRequest = field(
        metadata={
            "name": "getLocalityChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetLocalityChangesListOutputBodyFaultDetail(
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


class IkarServicePortTypeGetLocalityListByDistrictInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_locality_list_by_district_request: GetLocalityListByDistrictRequest = field(
        metadata={
            "name": "getLocalityListByDistrictRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetLocalityListByDistrictOutputBodyFaultDetail(
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
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class IkarServicePortTypeGetLocalityListByLocalityInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_locality_list_by_locality_request: GetLocalityListByLocalityRequest = field(
        metadata={
            "name": "getLocalityListByLocalityRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetLocalityListByLocalityOutputBodyFaultDetail(
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
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class IkarServicePortTypeGetLocalityListByRegionInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_locality_list_by_region_request: GetLocalityListByRegionRequest = field(
        metadata={
            "name": "getLocalityListByRegionRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetLocalityListByRegionOutputBodyFaultDetail(
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
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class IkarServicePortTypeGetRegionByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_region_by_guid_request: GetRegionByGuidRequest = field(
        metadata={
            "name": "getRegionByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetRegionByGuidOutputBodyFaultDetail(BaseModel):
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


class IkarServicePortTypeGetRegionByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_region_by_uuid_request: GetRegionByUuidRequest = field(
        metadata={
            "name": "getRegionByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetRegionByUuidOutputBodyFaultDetail(BaseModel):
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


class IkarServicePortTypeGetRegionChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_region_changes_list_request: GetRegionChangesListRequest = field(
        metadata={
            "name": "getRegionChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetRegionChangesListOutputBodyFaultDetail(BaseModel):
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


class IkarServicePortTypeGetRegionListByCountryInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_region_list_by_country_request: GetRegionListByCountryRequest = field(
        metadata={
            "name": "getRegionListByCountryRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetRegionListByCountryOutputBodyFaultDetail(
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
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class IkarServicePortTypeGetStreetChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_street_changes_list_request: GetStreetChangesListRequest = field(
        metadata={
            "name": "getStreetChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetStreetChangesListOutputBodyFaultDetail(BaseModel):
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


class IkarServicePortTypeGetStreetListByLocalityInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_street_list_by_locality_request: GetStreetListByLocalityRequest = field(
        metadata={
            "name": "getStreetListByLocalityRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class IkarServicePortTypeGetStreetListByLocalityOutputBodyFaultDetail(
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
    offset_out_of_range_fault: Optional[OffsetOutOfRangeFault] = field(
        default=None,
        metadata={
            "name": "offsetOutOfRangeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class IkarServicePortTypeFindLocalityListByNameInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeFindLocalityListByNameInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeFindLocalityListByNameOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeFindLocalityListByNameOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class IkarServicePortTypeFindStreetListByNameInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeFindStreetListByNameInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeFindStreetListByNameOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeFindStreetListByNameOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class IkarServicePortTypeGetAllCountryListInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetAllCountryListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetAllCountryListOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetAllCountryListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class IkarServicePortTypeGetCountryByGuidInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetCountryByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetCountryByGuidOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetCountryByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class IkarServicePortTypeGetCountryByUuidInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetCountryByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetCountryByUuidOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetCountryByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class IkarServicePortTypeGetCountryChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetCountryChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetCountryChangesListOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetCountryChangesListOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class IkarServicePortTypeGetDistrictByGuidInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetDistrictByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetDistrictByGuidOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetDistrictByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class IkarServicePortTypeGetDistrictByUuidInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetDistrictByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetDistrictByUuidOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetDistrictByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class IkarServicePortTypeGetDistrictChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetDistrictChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetDistrictChangesListOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetDistrictChangesListOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class IkarServicePortTypeGetDistrictListByRegionInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetDistrictListByRegionInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetDistrictListByRegionOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetDistrictListByRegionOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class IkarServicePortTypeGetLocalityChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetLocalityChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetLocalityChangesListOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetLocalityChangesListOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class IkarServicePortTypeGetLocalityListByDistrictInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetLocalityListByDistrictInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetLocalityListByDistrictOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetLocalityListByDistrictOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class IkarServicePortTypeGetLocalityListByLocalityInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetLocalityListByLocalityInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetLocalityListByLocalityOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetLocalityListByLocalityOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class IkarServicePortTypeGetLocalityListByRegionInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetLocalityListByRegionInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetLocalityListByRegionOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetLocalityListByRegionOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class IkarServicePortTypeGetRegionByGuidInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetRegionByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetRegionByGuidOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetRegionByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class IkarServicePortTypeGetRegionByUuidInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetRegionByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetRegionByUuidOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetRegionByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class IkarServicePortTypeGetRegionChangesListInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetRegionChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetRegionChangesListOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetRegionChangesListOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class IkarServicePortTypeGetRegionListByCountryInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetRegionListByCountryInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetRegionListByCountryOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetRegionListByCountryOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class IkarServicePortTypeGetStreetChangesListInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetStreetChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetStreetChangesListOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetStreetChangesListOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class IkarServicePortTypeGetStreetListByLocalityInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetStreetListByLocalityInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetStreetListByLocalityOutputBodyFault(BaseModel):
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
    detail: IkarServicePortTypeGetStreetListByLocalityOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class IkarServicePortTypeFindLocalityListByNameOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    find_locality_list_by_name_response: Optional[
        FindLocalityListByNameResponse
    ] = field(
        default=None,
        metadata={
            "name": "findLocalityListByNameResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        IkarServicePortTypeFindLocalityListByNameOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeFindStreetListByNameOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    find_street_list_by_name_response: Optional[
        FindStreetListByNameResponse
    ] = field(
        default=None,
        metadata={
            "name": "findStreetListByNameResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[IkarServicePortTypeFindStreetListByNameOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class IkarServicePortTypeGetAllCountryListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_all_country_list_response: Optional[GetAllCountryListResponse] = field(
        default=None,
        metadata={
            "name": "getAllCountryListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[IkarServicePortTypeGetAllCountryListOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class IkarServicePortTypeGetCountryByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_country_by_guid_response: Optional[GetCountryByGuidResponse] = field(
        default=None,
        metadata={
            "name": "getCountryByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[IkarServicePortTypeGetCountryByGuidOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class IkarServicePortTypeGetCountryByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_country_by_uuid_response: Optional[GetCountryByUuidResponse] = field(
        default=None,
        metadata={
            "name": "getCountryByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[IkarServicePortTypeGetCountryByUuidOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class IkarServicePortTypeGetCountryChangesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_country_changes_list_response: Optional[
        GetCountryChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getCountryChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        IkarServicePortTypeGetCountryChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeGetDistrictByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_district_by_guid_response: Optional[GetDistrictByGuidResponse] = field(
        default=None,
        metadata={
            "name": "getDistrictByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[IkarServicePortTypeGetDistrictByGuidOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class IkarServicePortTypeGetDistrictByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_district_by_uuid_response: Optional[GetDistrictByUuidResponse] = field(
        default=None,
        metadata={
            "name": "getDistrictByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[IkarServicePortTypeGetDistrictByUuidOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class IkarServicePortTypeGetDistrictChangesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_district_changes_list_response: Optional[
        GetDistrictChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getDistrictChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        IkarServicePortTypeGetDistrictChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeGetDistrictListByRegionOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_district_list_by_region_response: Optional[
        GetDistrictListByRegionResponse
    ] = field(
        default=None,
        metadata={
            "name": "getDistrictListByRegionResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        IkarServicePortTypeGetDistrictListByRegionOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeGetLocalityChangesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_locality_changes_list_response: Optional[
        GetLocalityChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getLocalityChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        IkarServicePortTypeGetLocalityChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeGetLocalityListByDistrictOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_locality_list_by_district_response: Optional[
        GetLocalityListByDistrictResponse
    ] = field(
        default=None,
        metadata={
            "name": "getLocalityListByDistrictResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        IkarServicePortTypeGetLocalityListByDistrictOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeGetLocalityListByLocalityOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_locality_list_by_locality_response: Optional[
        GetLocalityListByLocalityResponse
    ] = field(
        default=None,
        metadata={
            "name": "getLocalityListByLocalityResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        IkarServicePortTypeGetLocalityListByLocalityOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeGetLocalityListByRegionOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_locality_list_by_region_response: Optional[
        GetLocalityListByRegionResponse
    ] = field(
        default=None,
        metadata={
            "name": "getLocalityListByRegionResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        IkarServicePortTypeGetLocalityListByRegionOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeGetRegionByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_region_by_guid_response: Optional[GetRegionByGuidResponse] = field(
        default=None,
        metadata={
            "name": "getRegionByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[IkarServicePortTypeGetRegionByGuidOutputBodyFault] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeGetRegionByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_region_by_uuid_response: Optional[GetRegionByUuidResponse] = field(
        default=None,
        metadata={
            "name": "getRegionByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[IkarServicePortTypeGetRegionByUuidOutputBodyFault] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeGetRegionChangesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_region_changes_list_response: Optional[
        GetRegionChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getRegionChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[IkarServicePortTypeGetRegionChangesListOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class IkarServicePortTypeGetRegionListByCountryOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_region_list_by_country_response: Optional[
        GetRegionListByCountryResponse
    ] = field(
        default=None,
        metadata={
            "name": "getRegionListByCountryResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        IkarServicePortTypeGetRegionListByCountryOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeGetStreetChangesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_street_changes_list_response: Optional[
        GetStreetChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getStreetChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[IkarServicePortTypeGetStreetChangesListOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class IkarServicePortTypeGetStreetListByLocalityOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_street_list_by_locality_response: Optional[
        GetStreetListByLocalityResponse
    ] = field(
        default=None,
        metadata={
            "name": "getStreetListByLocalityResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        IkarServicePortTypeGetStreetListByLocalityOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class IkarServicePortTypeFindLocalityListByNameOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeFindLocalityListByNameOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeFindStreetListByNameOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeFindStreetListByNameOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetAllCountryListOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetAllCountryListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetCountryByGuidOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetCountryByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetCountryByUuidOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetCountryByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetCountryChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetCountryChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetDistrictByGuidOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetDistrictByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetDistrictByUuidOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetDistrictByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetDistrictChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetDistrictChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetDistrictListByRegionOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetDistrictListByRegionOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetLocalityChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetLocalityChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetLocalityListByDistrictOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetLocalityListByDistrictOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetLocalityListByLocalityOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetLocalityListByLocalityOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetLocalityListByRegionOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetLocalityListByRegionOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetRegionByGuidOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetRegionByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetRegionByUuidOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetRegionByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetRegionChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetRegionChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetRegionListByCountryOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetRegionListByCountryOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetStreetChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetStreetChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeGetStreetListByLocalityOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: IkarServicePortTypeGetStreetListByLocalityOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class IkarServicePortTypeFindLocalityListByName(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "FindLocalityListByName"
    input = IkarServicePortTypeFindLocalityListByNameInput
    output = IkarServicePortTypeFindLocalityListByNameOutput


class IkarServicePortTypeFindStreetListByName(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "FindStreetListByName"
    input = IkarServicePortTypeFindStreetListByNameInput
    output = IkarServicePortTypeFindStreetListByNameOutput


class IkarServicePortTypeGetAllCountryList(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAllCountryList"
    input = IkarServicePortTypeGetAllCountryListInput
    output = IkarServicePortTypeGetAllCountryListOutput


class IkarServicePortTypeGetCountryByGuid(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetCountryByGuid"
    input = IkarServicePortTypeGetCountryByGuidInput
    output = IkarServicePortTypeGetCountryByGuidOutput


class IkarServicePortTypeGetCountryByUuid(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetCountryByUuid"
    input = IkarServicePortTypeGetCountryByUuidInput
    output = IkarServicePortTypeGetCountryByUuidOutput


class IkarServicePortTypeGetCountryChangesList(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetCountryChangesList"
    input = IkarServicePortTypeGetCountryChangesListInput
    output = IkarServicePortTypeGetCountryChangesListOutput


class IkarServicePortTypeGetDistrictByGuid(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetDistrictByGuid"
    input = IkarServicePortTypeGetDistrictByGuidInput
    output = IkarServicePortTypeGetDistrictByGuidOutput


class IkarServicePortTypeGetDistrictByUuid(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetDistrictByUuid"
    input = IkarServicePortTypeGetDistrictByUuidInput
    output = IkarServicePortTypeGetDistrictByUuidOutput


class IkarServicePortTypeGetDistrictChangesList(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetDistrictChangesList"
    input = IkarServicePortTypeGetDistrictChangesListInput
    output = IkarServicePortTypeGetDistrictChangesListOutput


class IkarServicePortTypeGetDistrictListByRegion(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetDistrictListByRegion"
    input = IkarServicePortTypeGetDistrictListByRegionInput
    output = IkarServicePortTypeGetDistrictListByRegionOutput


class IkarServicePortTypeGetLocalityChangesList(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetLocalityChangesList"
    input = IkarServicePortTypeGetLocalityChangesListInput
    output = IkarServicePortTypeGetLocalityChangesListOutput


class IkarServicePortTypeGetLocalityListByDistrict(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetLocalityListByDistrict"
    input = IkarServicePortTypeGetLocalityListByDistrictInput
    output = IkarServicePortTypeGetLocalityListByDistrictOutput


class IkarServicePortTypeGetLocalityListByLocality(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetLocalityListByLocality"
    input = IkarServicePortTypeGetLocalityListByLocalityInput
    output = IkarServicePortTypeGetLocalityListByLocalityOutput


class IkarServicePortTypeGetLocalityListByRegion(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetLocalityListByRegion"
    input = IkarServicePortTypeGetLocalityListByRegionInput
    output = IkarServicePortTypeGetLocalityListByRegionOutput


class IkarServicePortTypeGetRegionByGuid(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetRegionByGuid"
    input = IkarServicePortTypeGetRegionByGuidInput
    output = IkarServicePortTypeGetRegionByGuidOutput


class IkarServicePortTypeGetRegionByUuid(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetRegionByUuid"
    input = IkarServicePortTypeGetRegionByUuidInput
    output = IkarServicePortTypeGetRegionByUuidOutput


class IkarServicePortTypeGetRegionChangesList(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetRegionChangesList"
    input = IkarServicePortTypeGetRegionChangesListInput
    output = IkarServicePortTypeGetRegionChangesListOutput


class IkarServicePortTypeGetRegionListByCountry(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetRegionListByCountry"
    input = IkarServicePortTypeGetRegionListByCountryInput
    output = IkarServicePortTypeGetRegionListByCountryOutput


class IkarServicePortTypeGetStreetChangesList(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetStreetChangesList"
    input = IkarServicePortTypeGetStreetChangesListInput
    output = IkarServicePortTypeGetStreetChangesListOutput


class IkarServicePortTypeGetStreetListByLocality(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/IkarService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetStreetListByLocality"
    input = IkarServicePortTypeGetStreetListByLocalityInput
    output = IkarServicePortTypeGetStreetListByLocalityOutput
