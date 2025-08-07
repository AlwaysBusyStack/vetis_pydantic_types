from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime

from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.mercury.types.base_v2_0 import Error

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/application"


class ApplicationDataInternalType(BaseModel):
    class Meta:
        name = "ApplicationData"

    model_config = ConfigDict(defer_build=True)


class ApplicationResultDataInternalType(BaseModel):
    class Meta:
        name = "ApplicationResultData"

    model_config = ConfigDict(defer_build=True)


class ApplicationStatus(Enum):
    ACCEPTED = "ACCEPTED"
    IN_PROCESS = "IN_PROCESS"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"

    __descriptions = {
        ACCEPTED: "",
        IN_PROCESS: "",
        COMPLETED: "",
        REJECTED: "",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ApplicationStatus.ACCEPTED.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ContentEncoding(Enum):
    PLAIN = "plain"
    GZIP = "gzip"

    __descriptions = {
        PLAIN: "",
        GZIP: "",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ContentEncoding.PLAIN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class Binary(BaseModel):
    class Meta:
        name = "binary"
        namespace = "http://api.vetrf.ru/schema/cdm/application"

    model_config = ConfigDict(defer_build=True)
    value: bytes = field(
        metadata={
            "required": True,
            "format": "base64",
        }
    )


class ApplicationDataWrapper(BaseModel):
    model_config = ConfigDict(defer_build=True)
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    encoding: Optional[ContentEncoding] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class ApplicationResultWrapper(BaseModel):
    model_config = ConfigDict(defer_build=True)
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    encoding: Optional[ContentEncoding] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class BusinessErrorInternalType(Error):
    class Meta:
        name = "BusinessError"

    model_config = ConfigDict(defer_build=True)


class ApplicationData(ApplicationDataInternalType):
    class Meta:
        name = "applicationData"
        namespace = "http://api.vetrf.ru/schema/cdm/application"

    model_config = ConfigDict(defer_build=True)


class ApplicationResultData(ApplicationResultDataInternalType):
    class Meta:
        name = "applicationResultData"
        namespace = "http://api.vetrf.ru/schema/cdm/application"

    model_config = ConfigDict(defer_build=True)


class BusinessErrorList(BaseModel):
    model_config = ConfigDict(defer_build=True)
    error: list[BusinessErrorInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
        },
    )


class BusinessError(BusinessErrorInternalType):
    class Meta:
        name = "businessError"
        namespace = "http://api.vetrf.ru/schema/cdm/application"

    model_config = ConfigDict(defer_build=True)


class ApplicationInternalType(BaseModel):
    class Meta:
        name = "Application"

    model_config = ConfigDict(defer_build=True)
    application_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "applicationId",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )
    status: Optional[ApplicationStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
        },
    )
    service_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceId",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
        },
    )
    issuer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerId",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )
    issue_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
        },
    )
    rcv_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "rcvDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
        },
    )
    prdc_rslt_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "prdcRsltDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
        },
    )
    data: Optional[ApplicationDataWrapper] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
        },
    )
    result: Optional[ApplicationResultWrapper] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
        },
    )
    errors: Optional[BusinessErrorList] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/application",
        },
    )


class ErrorList(BusinessErrorList):
    class Meta:
        name = "errorList"
        namespace = "http://api.vetrf.ru/schema/cdm/application"

    model_config = ConfigDict(defer_build=True)


class Application(ApplicationInternalType):
    class Meta:
        name = "application"
        namespace = "http://api.vetrf.ru/schema/cdm/application"

    model_config = ConfigDict(defer_build=True)
