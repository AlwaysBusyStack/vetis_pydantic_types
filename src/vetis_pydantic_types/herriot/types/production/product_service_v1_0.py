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
    GetProductByGuidRequest,
    GetProductByGuidResponse,
    GetProductByTypeListRequest,
    GetProductByTypeListResponse,
    GetProductByUuidRequest,
    GetProductByUuidResponse,
    GetProductChangesListRequest,
    GetProductChangesListResponse,
    GetSubProductByGuidRequest,
    GetSubProductByGuidResponse,
    GetSubProductByProductListRequest,
    GetSubProductByProductListResponse,
    GetSubProductByUuidRequest,
    GetSubProductByUuidResponse,
    GetSubProductChangesListRequest,
    GetSubProductChangesListResponse,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/registry/product/service/v3"


class ProductServicePortTypeGetProductByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_product_by_guid_request: GetProductByGuidRequest = field(
        metadata={
            "name": "getProductByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class ProductServicePortTypeGetProductByGuidOutputBodyFaultDetail(BaseModel):
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


class ProductServicePortTypeGetProductByTypeListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_product_by_type_list_request: GetProductByTypeListRequest = field(
        metadata={
            "name": "getProductByTypeListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class ProductServicePortTypeGetProductByTypeListOutputBodyFaultDetail(
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


class ProductServicePortTypeGetProductByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_product_by_uuid_request: GetProductByUuidRequest = field(
        metadata={
            "name": "getProductByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class ProductServicePortTypeGetProductByUuidOutputBodyFaultDetail(BaseModel):
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


class ProductServicePortTypeGetProductChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_product_changes_list_request: GetProductChangesListRequest = field(
        metadata={
            "name": "getProductChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class ProductServicePortTypeGetProductChangesListOutputBodyFaultDetail(
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


class ProductServicePortTypeGetSubProductByGuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_sub_product_by_guid_request: GetSubProductByGuidRequest = field(
        metadata={
            "name": "getSubProductByGuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class ProductServicePortTypeGetSubProductByGuidOutputBodyFaultDetail(
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


class ProductServicePortTypeGetSubProductByProductListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_sub_product_by_product_list_request: GetSubProductByProductListRequest = field(
        metadata={
            "name": "getSubProductByProductListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class ProductServicePortTypeGetSubProductByProductListOutputBodyFaultDetail(
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


class ProductServicePortTypeGetSubProductByUuidInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_sub_product_by_uuid_request: GetSubProductByUuidRequest = field(
        metadata={
            "name": "getSubProductByUuidRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class ProductServicePortTypeGetSubProductByUuidOutputBodyFaultDetail(
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


class ProductServicePortTypeGetSubProductChangesListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_sub_product_changes_list_request: GetSubProductChangesListRequest = field(
        metadata={
            "name": "getSubProductChangesListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class ProductServicePortTypeGetSubProductChangesListOutputBodyFaultDetail(
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


class ProductServicePortTypeGetProductByGuidInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetProductByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetProductByGuidOutputBodyFault(BaseModel):
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
    detail: ProductServicePortTypeGetProductByGuidOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class ProductServicePortTypeGetProductByTypeListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetProductByTypeListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetProductByTypeListOutputBodyFault(BaseModel):
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
    detail: ProductServicePortTypeGetProductByTypeListOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class ProductServicePortTypeGetProductByUuidInput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetProductByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetProductByUuidOutputBodyFault(BaseModel):
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
    detail: ProductServicePortTypeGetProductByUuidOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class ProductServicePortTypeGetProductChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetProductChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetProductChangesListOutputBodyFault(BaseModel):
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
    detail: ProductServicePortTypeGetProductChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class ProductServicePortTypeGetSubProductByGuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetSubProductByGuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetSubProductByGuidOutputBodyFault(BaseModel):
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
    detail: ProductServicePortTypeGetSubProductByGuidOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class ProductServicePortTypeGetSubProductByProductListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetSubProductByProductListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetSubProductByProductListOutputBodyFault(
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
    detail: ProductServicePortTypeGetSubProductByProductListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class ProductServicePortTypeGetSubProductByUuidInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetSubProductByUuidInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetSubProductByUuidOutputBodyFault(BaseModel):
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
    detail: ProductServicePortTypeGetSubProductByUuidOutputBodyFaultDetail = (
        field(
            metadata={
                "type": "Element",
                "namespace": "",
            }
        )
    )


class ProductServicePortTypeGetSubProductChangesListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetSubProductChangesListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetSubProductChangesListOutputBodyFault(BaseModel):
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
    detail: ProductServicePortTypeGetSubProductChangesListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class ProductServicePortTypeGetProductByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_product_by_guid_response: Optional[GetProductByGuidResponse] = field(
        default=None,
        metadata={
            "name": "getProductByGuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[ProductServicePortTypeGetProductByGuidOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class ProductServicePortTypeGetProductByTypeListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_product_by_type_list_response: Optional[
        GetProductByTypeListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getProductByTypeListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        ProductServicePortTypeGetProductByTypeListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class ProductServicePortTypeGetProductByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_product_by_uuid_response: Optional[GetProductByUuidResponse] = field(
        default=None,
        metadata={
            "name": "getProductByUuidResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[ProductServicePortTypeGetProductByUuidOutputBodyFault] = (
        field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
                "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
            },
        )
    )


class ProductServicePortTypeGetProductChangesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_product_changes_list_response: Optional[
        GetProductChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getProductChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        ProductServicePortTypeGetProductChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class ProductServicePortTypeGetSubProductByGuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_sub_product_by_guid_response: Optional[GetSubProductByGuidResponse] = (
        field(
            default=None,
            metadata={
                "name": "getSubProductByGuidResponse",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
            },
        )
    )
    fault: Optional[
        ProductServicePortTypeGetSubProductByGuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class ProductServicePortTypeGetSubProductByProductListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_sub_product_by_product_list_response: Optional[
        GetSubProductByProductListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getSubProductByProductListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        ProductServicePortTypeGetSubProductByProductListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class ProductServicePortTypeGetSubProductByUuidOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_sub_product_by_uuid_response: Optional[GetSubProductByUuidResponse] = (
        field(
            default=None,
            metadata={
                "name": "getSubProductByUuidResponse",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
            },
        )
    )
    fault: Optional[
        ProductServicePortTypeGetSubProductByUuidOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class ProductServicePortTypeGetSubProductChangesListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_sub_product_changes_list_response: Optional[
        GetSubProductChangesListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getSubProductChangesListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        ProductServicePortTypeGetSubProductChangesListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class ProductServicePortTypeGetProductByGuidOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetProductByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetProductByTypeListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetProductByTypeListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetProductByUuidOutput(BaseModel, BaseIOOperation):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetProductByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetProductChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetProductChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetSubProductByGuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetSubProductByGuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetSubProductByProductListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetSubProductByProductListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetSubProductByUuidOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetSubProductByUuidOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetSubProductChangesListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ProductServicePortTypeGetSubProductChangesListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ProductServicePortTypeGetProductByGuid(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/ProductService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetProductByGuid"
    input = ProductServicePortTypeGetProductByGuidInput
    output = ProductServicePortTypeGetProductByGuidOutput


class ProductServicePortTypeGetProductByTypeList(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/ProductService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetProductByTypeList"
    input = ProductServicePortTypeGetProductByTypeListInput
    output = ProductServicePortTypeGetProductByTypeListOutput


class ProductServicePortTypeGetProductByUuid(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/ProductService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetProductByUuid"
    input = ProductServicePortTypeGetProductByUuidInput
    output = ProductServicePortTypeGetProductByUuidOutput


class ProductServicePortTypeGetProductChangesList(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/ProductService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetProductChangesList"
    input = ProductServicePortTypeGetProductChangesListInput
    output = ProductServicePortTypeGetProductChangesListOutput


class ProductServicePortTypeGetSubProductByGuid(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/ProductService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetSubProductByGuid"
    input = ProductServicePortTypeGetSubProductByGuidInput
    output = ProductServicePortTypeGetSubProductByGuidOutput


class ProductServicePortTypeGetSubProductByProductList(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/ProductService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetSubProductByProductList"
    input = ProductServicePortTypeGetSubProductByProductListInput
    output = ProductServicePortTypeGetSubProductByProductListOutput


class ProductServicePortTypeGetSubProductByUuid(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/ProductService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetSubProductByUuid"
    input = ProductServicePortTypeGetSubProductByUuidInput
    output = ProductServicePortTypeGetSubProductByUuidOutput


class ProductServicePortTypeGetSubProductChangesList(RegistryOperation):
    style = "document"
    location = "https://{server}:{port}/platform/services/2.0/ProductService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetSubProductChangesList"
    input = ProductServicePortTypeGetSubProductChangesListInput
    output = ProductServicePortTypeGetSubProductChangesListOutput
