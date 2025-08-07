from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict

from vetis_pydantic_types.base import BaseIOOperation, RegistryOperation
from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.mercury.types.base_ws_definitions_v2_0 import (
    IncorrectRequestFault,
    InternalServiceFault,
    OffsetOutOfRangeFault,
)
from vetis_pydantic_types.mercury.types.registry_ws_definitions_v2_1 import (
    GetActualR13NRegionStatusListRequest,
    GetActualR13NRegionStatusListResponse,
    GetActualR13NShippingRuleListRequest,
    GetActualR13NShippingRuleListResponse,
    GetR13NConditionListRequest,
    GetR13NConditionListResponse,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/registry/r13n/service/v2"


class RegionalizationServicePortTypeGetActualR13NRegionStatusListInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_actual_r13n_region_status_list_request: GetActualR13NRegionStatusListRequest = field(
        metadata={
            "name": "getActualR13nRegionStatusListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class RegionalizationServicePortTypeGetActualR13NRegionStatusListOutputBodyFaultDetail(
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


class RegionalizationServicePortTypeGetActualR13NShippingRuleListInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_actual_r13n_shipping_rule_list_request: GetActualR13NShippingRuleListRequest = field(
        metadata={
            "name": "getActualR13nShippingRuleListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class RegionalizationServicePortTypeGetActualR13NShippingRuleListOutputBodyFaultDetail(
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


class RegionalizationServicePortTypeGetR13NConditionListInputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_r13n_condition_list_request: GetR13NConditionListRequest = field(
        metadata={
            "name": "getR13nConditionListRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        }
    )


class RegionalizationServicePortTypeGetR13NConditionListOutputBodyFaultDetail(
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


class RegionalizationServicePortTypeGetActualR13NRegionStatusListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: RegionalizationServicePortTypeGetActualR13NRegionStatusListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class RegionalizationServicePortTypeGetActualR13NRegionStatusListOutputBodyFault(
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
    detail: RegionalizationServicePortTypeGetActualR13NRegionStatusListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class RegionalizationServicePortTypeGetActualR13NShippingRuleListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: RegionalizationServicePortTypeGetActualR13NShippingRuleListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class RegionalizationServicePortTypeGetActualR13NShippingRuleListOutputBodyFault(
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
    detail: RegionalizationServicePortTypeGetActualR13NShippingRuleListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class RegionalizationServicePortTypeGetR13NConditionListInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: RegionalizationServicePortTypeGetR13NConditionListInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class RegionalizationServicePortTypeGetR13NConditionListOutputBodyFault(
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
    detail: RegionalizationServicePortTypeGetR13NConditionListOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class RegionalizationServicePortTypeGetActualR13NRegionStatusListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_actual_r13n_region_status_list_response: Optional[
        GetActualR13NRegionStatusListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getActualR13nRegionStatusListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        RegionalizationServicePortTypeGetActualR13NRegionStatusListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class RegionalizationServicePortTypeGetActualR13NShippingRuleListOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_actual_r13n_shipping_rule_list_response: Optional[
        GetActualR13NShippingRuleListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getActualR13nShippingRuleListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        RegionalizationServicePortTypeGetActualR13NShippingRuleListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class RegionalizationServicePortTypeGetR13NConditionListOutputBody(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    get_r13n_condition_list_response: Optional[
        GetR13NConditionListResponse
    ] = field(
        default=None,
        metadata={
            "name": "getR13nConditionListResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2",
        },
    )
    fault: Optional[
        RegionalizationServicePortTypeGetR13NConditionListOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class RegionalizationServicePortTypeGetActualR13NRegionStatusListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: RegionalizationServicePortTypeGetActualR13NRegionStatusListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class RegionalizationServicePortTypeGetActualR13NShippingRuleListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: RegionalizationServicePortTypeGetActualR13NShippingRuleListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class RegionalizationServicePortTypeGetR13NConditionListOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: RegionalizationServicePortTypeGetR13NConditionListOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class RegionalizationServicePortTypeGetActualR13NRegionStatusList(
    RegistryOperation
):
    style = "document"
    location = (
        "https://api.vetrf.ru/platform/services/2.1/RegionalizationService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetProductByTypeList"
    input = RegionalizationServicePortTypeGetActualR13NRegionStatusListInput
    output = RegionalizationServicePortTypeGetActualR13NRegionStatusListOutput


class RegionalizationServicePortTypeGetActualR13NShippingRuleList(
    RegistryOperation
):
    style = "document"
    location = (
        "https://api.vetrf.ru/platform/services/2.1/RegionalizationService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetProductByTypeList"
    input = RegionalizationServicePortTypeGetActualR13NShippingRuleListInput
    output = RegionalizationServicePortTypeGetActualR13NShippingRuleListOutput


class RegionalizationServicePortTypeGetR13NConditionList(RegistryOperation):
    style = "document"
    location = (
        "https://api.vetrf.ru/platform/services/2.1/RegionalizationService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "GetProductByTypeList"
    input = RegionalizationServicePortTypeGetR13NConditionListInput
    output = RegionalizationServicePortTypeGetR13NConditionListOutput
