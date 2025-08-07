from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict

from vetis_pydantic_types.base.fields import field

__NAMESPACE__ = "http://www.w3.org/2005/05/xmlmime"


class Base64Binary(BaseModel):
    class Meta:
        name = "base64Binary"

    model_config = ConfigDict(defer_build=True)
    value: bytes = field(
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2005/05/xmlmime",
            "min_length": 3,
        },
    )


class HexBinary(BaseModel):
    class Meta:
        name = "hexBinary"

    model_config = ConfigDict(defer_build=True)
    value: bytes = field(
        metadata={
            "required": True,
            "format": "base16",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2005/05/xmlmime",
            "min_length": 3,
        },
    )
