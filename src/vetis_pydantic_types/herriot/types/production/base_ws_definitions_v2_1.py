from __future__ import annotations

from pydantic import ConfigDict

from vetis_pydantic_types.herriot.types.production.base_v2_1 import FaultInfo

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/base/ws-definitions"


class AccessDeniedFault(FaultInfo):
    class Meta:
        name = "accessDeniedFault"
        namespace = "http://api.vetrf.ru/schema/cdm/base/ws-definitions"

    model_config = ConfigDict(defer_build=True)


class EntityNotFoundFault(FaultInfo):
    class Meta:
        name = "entityNotFoundFault"
        namespace = "http://api.vetrf.ru/schema/cdm/base/ws-definitions"

    model_config = ConfigDict(defer_build=True)


class IncorrectRequestFault(FaultInfo):
    class Meta:
        name = "incorrectRequestFault"
        namespace = "http://api.vetrf.ru/schema/cdm/base/ws-definitions"

    model_config = ConfigDict(defer_build=True)


class InternalServiceFault(FaultInfo):
    class Meta:
        name = "internalServiceFault"
        namespace = "http://api.vetrf.ru/schema/cdm/base/ws-definitions"

    model_config = ConfigDict(defer_build=True)


class OffsetOutOfRangeFault(FaultInfo):
    class Meta:
        name = "offsetOutOfRangeFault"
        namespace = "http://api.vetrf.ru/schema/cdm/base/ws-definitions"

    model_config = ConfigDict(defer_build=True)


class RequestRejectedFault(FaultInfo):
    class Meta:
        name = "requestRejectedFault"
        namespace = "http://api.vetrf.ru/schema/cdm/base/ws-definitions"

    model_config = ConfigDict(defer_build=True)
