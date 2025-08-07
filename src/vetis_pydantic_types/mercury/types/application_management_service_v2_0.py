from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict

from vetis_pydantic_types.base import (
    BaseIOOperation,
    ReceiveApplicationResultOperation,
    SubmitApplicationRequestOperation,
)
from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.mercury.types.application_ws_definitions_v2_0 import (
    ReceiveApplicationResultRequest,
    ReceiveApplicationResultResponse,
    SubmitApplicationRequest,
    SubmitApplicationResponse,
    UnknownServiceIdFault,
    UnsupportedApplicationDataTypeFault,
)
from vetis_pydantic_types.mercury.types.base_ws_definitions_v2_0 import (
    AccessDeniedFault,
    EntityNotFoundFault,
    IncorrectRequestFault,
    InternalServiceFault,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/application/service"


class ApplicationManagementServicePortTypeReceiveApplicationResultInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    receive_application_result_request: ReceiveApplicationResultRequest = field(
        metadata={
            "name": "receiveApplicationResultRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application/ws-definitions",
        }
    )


class ApplicationManagementServicePortTypeReceiveApplicationResultOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    entity_not_found_fault: Optional[EntityNotFoundFault] = field(
        default=None,
        metadata={
            "name": "entityNotFoundFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )
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
    access_denied_fault: Optional[AccessDeniedFault] = field(
        default=None,
        metadata={
            "name": "accessDeniedFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class ApplicationManagementServicePortTypeSubmitApplicationRequestInputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    submit_application_request: SubmitApplicationRequest = field(
        metadata={
            "name": "submitApplicationRequest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application/ws-definitions",
        }
    )


class ApplicationManagementServicePortTypeSubmitApplicationRequestOutputBodyFaultDetail(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    unsupported_application_data_type_fault: Optional[
        UnsupportedApplicationDataTypeFault
    ] = field(
        default=None,
        metadata={
            "name": "unsupportedApplicationDataTypeFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application/ws-definitions",
        },
    )
    unknown_service_id_fault: Optional[UnknownServiceIdFault] = field(
        default=None,
        metadata={
            "name": "unknownServiceIdFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application/ws-definitions",
        },
    )
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
    access_denied_fault: Optional[AccessDeniedFault] = field(
        default=None,
        metadata={
            "name": "accessDeniedFault",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base/ws-definitions",
        },
    )


class ApplicationManagementServicePortTypeReceiveApplicationResultInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ApplicationManagementServicePortTypeReceiveApplicationResultInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ApplicationManagementServicePortTypeReceiveApplicationResultOutputBodyFault(
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
    detail: ApplicationManagementServicePortTypeReceiveApplicationResultOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class ApplicationManagementServicePortTypeSubmitApplicationRequestInput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ApplicationManagementServicePortTypeSubmitApplicationRequestInputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ApplicationManagementServicePortTypeSubmitApplicationRequestOutputBodyFault(
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
    detail: ApplicationManagementServicePortTypeSubmitApplicationRequestOutputBodyFaultDetail = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class ApplicationManagementServicePortTypeReceiveApplicationResultOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    receive_application_result_response: Optional[
        ReceiveApplicationResultResponse
    ] = field(
        default=None,
        metadata={
            "name": "receiveApplicationResultResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application/ws-definitions",
        },
    )
    fault: Optional[
        ApplicationManagementServicePortTypeReceiveApplicationResultOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class ApplicationManagementServicePortTypeSubmitApplicationRequestOutputBody(
    BaseModel
):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    submit_application_response: Optional[SubmitApplicationResponse] = field(
        default=None,
        metadata={
            "name": "submitApplicationResponse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application/ws-definitions",
        },
    )
    fault: Optional[
        ApplicationManagementServicePortTypeSubmitApplicationRequestOutputBodyFault
    ] = field(
        default=None,
        metadata={
            "name": "Fault",
            "type": "Element",
            "namespace": "http://schemas.xmlsoap.org/soap/envelope/",
        },
    )


class ApplicationManagementServicePortTypeReceiveApplicationResultOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ApplicationManagementServicePortTypeReceiveApplicationResultOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ApplicationManagementServicePortTypeSubmitApplicationRequestOutput(
    BaseModel, BaseIOOperation
):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    model_config = ConfigDict(defer_build=True)
    body: ApplicationManagementServicePortTypeSubmitApplicationRequestOutputBody = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )


class ApplicationManagementServicePortTypeReceiveApplicationResult(
    ReceiveApplicationResultOperation
):
    style = "document"
    location = "https://api2.vetrf.ru:8002/platform/services/2.1/ApplicationManagementService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "receiveApplicationResult"
    input = ApplicationManagementServicePortTypeReceiveApplicationResultInput
    output = ApplicationManagementServicePortTypeReceiveApplicationResultOutput


class ApplicationManagementServicePortTypeSubmitApplicationRequest(
    SubmitApplicationRequestOperation
):
    style = "document"
    location = "https://api2.vetrf.ru:8002/platform/services/2.1/ApplicationManagementService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "submitApplicationRequest"
    input = ApplicationManagementServicePortTypeSubmitApplicationRequestInput
    output = ApplicationManagementServicePortTypeSubmitApplicationRequestOutput
