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
    GetAnimalBreedByGuidRequest,
    GetAnimalBreedByGuidResponse,
    GetAnimalBreedByUuidRequest,
    GetAnimalBreedByUuidResponse,
    GetAnimalBreedChangesListRequest,
    GetAnimalBreedChangesListResponse,
    GetAnimalBreedListRequest,
    GetAnimalBreedListResponse,
    GetAnimalKeepingPurposeByGuidRequest,
    GetAnimalKeepingPurposeByGuidResponse,
    GetAnimalKeepingPurposeByUuidRequest,
    GetAnimalKeepingPurposeByUuidResponse,
    GetAnimalKeepingPurposeChangesListRequest,
    GetAnimalKeepingPurposeChangesListResponse,
    GetAnimalKeepingPurposeListRequest,
    GetAnimalKeepingPurposeListResponse,
    GetAnimalKeepingTypeByGuidRequest,
    GetAnimalKeepingTypeByGuidResponse,
    GetAnimalKeepingTypeByUuidRequest,
    GetAnimalKeepingTypeByUuidResponse,
    GetAnimalKeepingTypeChangesListRequest,
    GetAnimalKeepingTypeChangesListResponse,
    GetAnimalKeepingTypeListRequest,
    GetAnimalKeepingTypeListResponse,
    GetAnimalMarkingLocationByGuidRequest,
    GetAnimalMarkingLocationByGuidResponse,
    GetAnimalMarkingLocationByUuidRequest,
    GetAnimalMarkingLocationByUuidResponse,
    GetAnimalMarkingLocationChangesListRequest,
    GetAnimalMarkingLocationChangesListResponse,
    GetAnimalMarkingLocationListRequest,
    GetAnimalMarkingLocationListResponse,
    GetAnimalSpeciesByGuidRequest,
    GetAnimalSpeciesByGuidResponse,
    GetAnimalSpeciesByUuidRequest,
    GetAnimalSpeciesByUuidResponse,
    GetAnimalSpeciesChangesListRequest,
    GetAnimalSpeciesChangesListResponse,
    GetAnimalSpeciesListRequest,
    GetAnimalSpeciesListResponse,
    GetUnitByGuidRequest,
    GetUnitByGuidResponse,
    GetUnitByUuidRequest,
    GetUnitByUuidResponse,
    GetUnitChangesListRequest,
    GetUnitChangesListResponse,
    GetUnitListRequest,
    GetUnitListResponse,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/registry/dictionary/service/v3"


class DictionaryServicePortTypeGetAnimalBreedByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_breed_by_guid_request: GetAnimalBreedByGuidRequest = field(
        metadata={
            "name": "getAnimalBreedByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedByGuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalBreedByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_breed_by_uuid_request: GetAnimalBreedByUuidRequest = field(
        metadata={
            "name": "getAnimalBreedByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedByUuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalBreedChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_breed_changes_list_request: GetAnimalBreedChangesListRequest = field(
        metadata={
            "name": "getAnimalBreedChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedChangesListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalBreedListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_breed_list_request: GetAnimalBreedListRequest = field(
        metadata={
            "name": "getAnimalBreedListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_purpose_by_guid_request: GetAnimalKeepingPurposeByGuidRequest = field(
        metadata={
            "name": "getAnimalKeepingPurposeByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_purpose_by_uuid_request: GetAnimalKeepingPurposeByUuidRequest = field(
        metadata={
            "name": "getAnimalKeepingPurposeByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_purpose_changes_list_request: GetAnimalKeepingPurposeChangesListRequest = field(
        metadata={
            "name": "getAnimalKeepingPurposeChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalKeepingPurposeListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_purpose_list_request: GetAnimalKeepingPurposeListRequest = field(
        metadata={
            "name": "getAnimalKeepingPurposeListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalKeepingTypeByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_type_by_guid_request: GetAnimalKeepingTypeByGuidRequest = field(
        metadata={
            "name": "getAnimalKeepingTypeByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeByGuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalKeepingTypeByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_type_by_uuid_request: GetAnimalKeepingTypeByUuidRequest = field(
        metadata={
            "name": "getAnimalKeepingTypeByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeByUuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalKeepingTypeChangesListInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_type_changes_list_request: GetAnimalKeepingTypeChangesListRequest = field(
        metadata={
            "name": "getAnimalKeepingTypeChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeChangesListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalKeepingTypeListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_type_list_request: GetAnimalKeepingTypeListRequest = field(
        metadata={
            "name": "getAnimalKeepingTypeListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalMarkingLocationByGuidInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_marking_location_by_guid_request: GetAnimalMarkingLocationByGuidRequest = field(
        metadata={
            "name": "getAnimalMarkingLocationByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationByGuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalMarkingLocationByUuidInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_marking_location_by_uuid_request: GetAnimalMarkingLocationByUuidRequest = field(
        metadata={
            "name": "getAnimalMarkingLocationByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationByUuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalMarkingLocationChangesListInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_marking_location_changes_list_request: GetAnimalMarkingLocationChangesListRequest = field(
        metadata={
            "name": "getAnimalMarkingLocationChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationChangesListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalMarkingLocationListInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_marking_location_list_request: GetAnimalMarkingLocationListRequest = field(
        metadata={
            "name": "getAnimalMarkingLocationListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalSpeciesByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_species_by_guid_request: GetAnimalSpeciesByGuidRequest = field(
        metadata={
            "name": "getAnimalSpeciesByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesByGuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalSpeciesByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_species_by_uuid_request: GetAnimalSpeciesByUuidRequest = field(
        metadata={
            "name": "getAnimalSpeciesByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesByUuidOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalSpeciesChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_species_changes_list_request: GetAnimalSpeciesChangesListRequest = field(
        metadata={
            "name": "getAnimalSpeciesChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesChangesListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalSpeciesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_species_list_request: GetAnimalSpeciesListRequest = field(
        metadata={
            "name": "getAnimalSpeciesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesListOutputBodyFaultDetail(
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


class DictionaryServicePortTypeGetAnimalBreedByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalBreedByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedByGuidOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetAnimalBreedByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalBreedByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedByUuidOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetAnimalBreedByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalBreedChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedChangesListOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalBreedChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalBreedListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedListOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetAnimalBreedListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingPurposeListInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeListOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalKeepingPurposeListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingTypeByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeByGuidOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalKeepingTypeByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingTypeByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeByUuidOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalKeepingTypeByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingTypeChangesListInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeChangesListOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalKeepingTypeChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingTypeListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeListOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalKeepingTypeListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalMarkingLocationByGuidInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationByGuidOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalMarkingLocationByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalMarkingLocationByUuidInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationByUuidOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalMarkingLocationByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalMarkingLocationChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationChangesListOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalMarkingLocationChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalMarkingLocationListInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationListOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalMarkingLocationListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalSpeciesByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesByGuidOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalSpeciesByGuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalSpeciesByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesByUuidOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalSpeciesByUuidOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalSpeciesChangesListInputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalSpeciesChangesListOutputBodyFault(
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
    detail: DictionaryServicePortTypeGetAnimalSpeciesChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalSpeciesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesListOutputBodyFault(BaseModel):
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
    detail: DictionaryServicePortTypeGetAnimalSpeciesListOutputBodyFaultDetail = field(
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


class DictionaryServicePortTypeGetAnimalBreedByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_breed_by_guid_response: Optional[
        GetAnimalBreedByGuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalBreedByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalBreedByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalBreedByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_breed_by_uuid_response: Optional[
        GetAnimalBreedByUuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalBreedByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalBreedByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalBreedChangesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_breed_changes_list_response: Optional[
        GetAnimalBreedChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalBreedChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalBreedChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalBreedListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_breed_list_response: Optional[GetAnimalBreedListResponse] = (
        field(
            default=None,
            metadata={
                "name": "getAnimalBreedListResponse",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
            },
        )
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalBreedListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_purpose_by_guid_response: Optional[
        GetAnimalKeepingPurposeByGuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalKeepingPurposeByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_purpose_by_uuid_response: Optional[
        GetAnimalKeepingPurposeByUuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalKeepingPurposeByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_purpose_changes_list_response: Optional[
        GetAnimalKeepingPurposeChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalKeepingPurposeChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_purpose_list_response: Optional[
        GetAnimalKeepingPurposeListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalKeepingPurposeListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalKeepingPurposeListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_type_by_guid_response: Optional[
        GetAnimalKeepingTypeByGuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalKeepingTypeByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalKeepingTypeByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_type_by_uuid_response: Optional[
        GetAnimalKeepingTypeByUuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalKeepingTypeByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalKeepingTypeByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeChangesListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_type_changes_list_response: Optional[
        GetAnimalKeepingTypeChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalKeepingTypeChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalKeepingTypeChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_keeping_type_list_response: Optional[
        GetAnimalKeepingTypeListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalKeepingTypeListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalKeepingTypeListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationByGuidOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_marking_location_by_guid_response: Optional[
        GetAnimalMarkingLocationByGuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalMarkingLocationByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalMarkingLocationByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationByUuidOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_marking_location_by_uuid_response: Optional[
        GetAnimalMarkingLocationByUuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalMarkingLocationByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalMarkingLocationByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationChangesListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_marking_location_changes_list_response: Optional[
        GetAnimalMarkingLocationChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalMarkingLocationChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalMarkingLocationChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_marking_location_list_response: Optional[
        GetAnimalMarkingLocationListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalMarkingLocationListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalMarkingLocationListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalSpeciesByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_species_by_guid_response: Optional[
        GetAnimalSpeciesByGuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalSpeciesByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalSpeciesByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalSpeciesByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_species_by_uuid_response: Optional[
        GetAnimalSpeciesByUuidResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalSpeciesByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalSpeciesByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalSpeciesChangesListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_species_changes_list_response: Optional[
        GetAnimalSpeciesChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalSpeciesChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalSpeciesChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class DictionaryServicePortTypeGetAnimalSpeciesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_animal_species_list_response: Optional[
        GetAnimalSpeciesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getAnimalSpeciesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        DictionaryServicePortTypeGetAnimalSpeciesListOutputBodyFault
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


class DictionaryServicePortTypeGetAnimalBreedByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalBreedByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalBreedByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalBreedChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalBreedListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalBreedListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingPurposeListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingPurposeListOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingTypeByGuidOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingTypeByUuidOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingTypeChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalKeepingTypeListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalKeepingTypeListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalMarkingLocationByGuidOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalMarkingLocationByUuidOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalMarkingLocationChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalMarkingLocationListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalMarkingLocationListOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalSpeciesByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalSpeciesByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalSpeciesByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class DictionaryServicePortTypeGetAnimalSpeciesChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalSpeciesChangesListOutputBody = (
        field(
            metadata={
                "name": "Body",
                "type": "Element",
            }
        )
    )


class DictionaryServicePortTypeGetAnimalSpeciesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: DictionaryServicePortTypeGetAnimalSpeciesListOutputBody = field(
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


class DictionaryServicePortTypeGetAnimalBreedByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalBreedByGuid"
    input = DictionaryServicePortTypeGetAnimalBreedByGuidInput
    output = DictionaryServicePortTypeGetAnimalBreedByGuidOutput


class DictionaryServicePortTypeGetAnimalBreedByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalBreedByUuid"
    input = DictionaryServicePortTypeGetAnimalBreedByUuidInput
    output = DictionaryServicePortTypeGetAnimalBreedByUuidOutput


class DictionaryServicePortTypeGetAnimalBreedChangesList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalBreedChangesList"
    input = DictionaryServicePortTypeGetAnimalBreedChangesListInput
    output = DictionaryServicePortTypeGetAnimalBreedChangesListOutput


class DictionaryServicePortTypeGetAnimalBreedList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalBreedList"
    input = DictionaryServicePortTypeGetAnimalBreedListInput
    output = DictionaryServicePortTypeGetAnimalBreedListOutput


class DictionaryServicePortTypeGetAnimalKeepingPurposeByGuid(
    RegistryOperation
):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalKeepingPurposeByGuid"
    input = DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidInput
    output = DictionaryServicePortTypeGetAnimalKeepingPurposeByGuidOutput


class DictionaryServicePortTypeGetAnimalKeepingPurposeByUuid(
    RegistryOperation
):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalKeepingPurposeByUuid"
    input = DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidInput
    output = DictionaryServicePortTypeGetAnimalKeepingPurposeByUuidOutput


class DictionaryServicePortTypeGetAnimalKeepingPurposeChangesList(
    RegistryOperation
):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalKeepingPurposeChangesList"
    input = DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListInput
    output = DictionaryServicePortTypeGetAnimalKeepingPurposeChangesListOutput


class DictionaryServicePortTypeGetAnimalKeepingPurposeList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalKeepingPurposeList"
    input = DictionaryServicePortTypeGetAnimalKeepingPurposeListInput
    output = DictionaryServicePortTypeGetAnimalKeepingPurposeListOutput


class DictionaryServicePortTypeGetAnimalKeepingTypeByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalKeepingTypeByGuid"
    input = DictionaryServicePortTypeGetAnimalKeepingTypeByGuidInput
    output = DictionaryServicePortTypeGetAnimalKeepingTypeByGuidOutput


class DictionaryServicePortTypeGetAnimalKeepingTypeByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalKeepingTypeByUuid"
    input = DictionaryServicePortTypeGetAnimalKeepingTypeByUuidInput
    output = DictionaryServicePortTypeGetAnimalKeepingTypeByUuidOutput


class DictionaryServicePortTypeGetAnimalKeepingTypeChangesList(
    RegistryOperation
):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalKeepingTypeChangesList"
    input = DictionaryServicePortTypeGetAnimalKeepingTypeChangesListInput
    output = DictionaryServicePortTypeGetAnimalKeepingTypeChangesListOutput


class DictionaryServicePortTypeGetAnimalKeepingTypeList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalKeepingTypeList"
    input = DictionaryServicePortTypeGetAnimalKeepingTypeListInput
    output = DictionaryServicePortTypeGetAnimalKeepingTypeListOutput


class DictionaryServicePortTypeGetAnimalMarkingLocationByGuid(
    RegistryOperation
):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalMarkingLocationByGuid"
    input = DictionaryServicePortTypeGetAnimalMarkingLocationByGuidInput
    output = DictionaryServicePortTypeGetAnimalMarkingLocationByGuidOutput


class DictionaryServicePortTypeGetAnimalMarkingLocationByUuid(
    RegistryOperation
):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalMarkingLocationByUuid"
    input = DictionaryServicePortTypeGetAnimalMarkingLocationByUuidInput
    output = DictionaryServicePortTypeGetAnimalMarkingLocationByUuidOutput


class DictionaryServicePortTypeGetAnimalMarkingLocationChangesList(
    RegistryOperation
):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalMarkingLocationChangesList"
    input = DictionaryServicePortTypeGetAnimalMarkingLocationChangesListInput
    output = DictionaryServicePortTypeGetAnimalMarkingLocationChangesListOutput


class DictionaryServicePortTypeGetAnimalMarkingLocationList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalMarkingLocationList"
    input = DictionaryServicePortTypeGetAnimalMarkingLocationListInput
    output = DictionaryServicePortTypeGetAnimalMarkingLocationListOutput


class DictionaryServicePortTypeGetAnimalSpeciesByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalSpeciesByGuid"
    input = DictionaryServicePortTypeGetAnimalSpeciesByGuidInput
    output = DictionaryServicePortTypeGetAnimalSpeciesByGuidOutput


class DictionaryServicePortTypeGetAnimalSpeciesByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalSpeciesByUuid"
    input = DictionaryServicePortTypeGetAnimalSpeciesByUuidInput
    output = DictionaryServicePortTypeGetAnimalSpeciesByUuidOutput


class DictionaryServicePortTypeGetAnimalSpeciesChangesList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalSpeciesChangesList"
    input = DictionaryServicePortTypeGetAnimalSpeciesChangesListInput
    output = DictionaryServicePortTypeGetAnimalSpeciesChangesListOutput


class DictionaryServicePortTypeGetAnimalSpeciesList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetAnimalSpeciesList"
    input = DictionaryServicePortTypeGetAnimalSpeciesListInput
    output = DictionaryServicePortTypeGetAnimalSpeciesListOutput


class DictionaryServicePortTypeGetUnitByGuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetUnitByGuid"
    input = DictionaryServicePortTypeGetUnitByGuidInput
    output = DictionaryServicePortTypeGetUnitByGuidOutput


class DictionaryServicePortTypeGetUnitByUuid(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetUnitByUuid"
    input = DictionaryServicePortTypeGetUnitByUuidInput
    output = DictionaryServicePortTypeGetUnitByUuidOutput


class DictionaryServicePortTypeGetUnitChangesList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetUnitChangesList"
    input = DictionaryServicePortTypeGetUnitChangesListInput
    output = DictionaryServicePortTypeGetUnitChangesListOutput


class DictionaryServicePortTypeGetUnitList(RegistryOperation):
    style = "document"
    location = (
        "https://{server}:{port}/platform/services/2.0/DictionaryService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetUnitList"
    input = DictionaryServicePortTypeGetUnitListInput
    output = DictionaryServicePortTypeGetUnitListOutput
