from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.herriot.types.pilot.application_v2_1 import (
    Application,
)
from vetis_pydantic_types.herriot.types.pilot.base_v2_1 import FaultInfo

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/application/ws-definitions"


class ReceiveApplicationResultRequest(BaseModel):
    class Meta:
        name = "receiveApplicationResultRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/application/ws-definitions"

    model_config = ConfigDict(defer_build=True)
    api_key: str = field(
        metadata={
            "name": "apiKey",
            "type": "Element",
            "required": True,
        }
    )
    issuer_id: str = field(
        metadata={
            "name": "issuerId",
            "type": "Element",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )
    application_id: str = field(
        metadata={
            "name": "applicationId",
            "type": "Element",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )


class ReceiveApplicationResultResponse(BaseModel):
    class Meta:
        name = "receiveApplicationResultResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/application/ws-definitions"

    model_config = ConfigDict(defer_build=True)
    application: Application = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
            "required": True,
        }
    )


class SubmitApplicationRequest(BaseModel):
    class Meta:
        name = "submitApplicationRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/application/ws-definitions"

    model_config = ConfigDict(defer_build=True)
    api_key: str = field(
        metadata={
            "name": "apiKey",
            "type": "Element",
            "required": True,
        }
    )
    application: Application = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
            "required": True,
        }
    )


class SubmitApplicationResponse(BaseModel):
    class Meta:
        name = "submitApplicationResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/application/ws-definitions"

    model_config = ConfigDict(defer_build=True)
    application: Application = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
            "required": True,
        }
    )


class UnknownServiceIdFault(FaultInfo):
    class Meta:
        name = "unknownServiceIdFault"
        namespace = "http://api.vetrf.ru/schema/cdm/application/ws-definitions"

    model_config = ConfigDict(defer_build=True)


class UnsupportedApplicationDataTypeFault(FaultInfo):
    class Meta:
        name = "unsupportedApplicationDataTypeFault"
        namespace = "http://api.vetrf.ru/schema/cdm/application/ws-definitions"

    model_config = ConfigDict(defer_build=True)
