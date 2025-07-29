"""
Файл для фикса генераций JSON схем для Pydantic схем. Нужен для исправления
генераций JSON схем, которые парсились библиотекой xsdata_pydantic.

Для этой библиотеки был создан Issue с PR, когда его закроют - можно убирать
эти исправления (см. https://github.com/tefra/xsdata-pydantic/issues/42)
"""

from typing import Any, Callable

from pydantic_core import core_schema
from pydantic_core.core_schema import str_schema
from xsdata.formats.converter import converter
from xsdata_pydantic.compat import XmlDate, XmlDateTime, XmlTime, XmlDuration, XmlPeriod


def set_validator(data_type: Any, json_input_schema: core_schema.CoreSchema):
    def validator(
        cls: Any,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        conv = converter.type_converter(data_type)

        return core_schema.json_or_python_schema(
            json_schema=core_schema.no_info_plain_validator_function(
                conv.deserialize,
                json_schema_input_schema=json_input_schema,
            ),
            python_schema=core_schema.is_instance_schema(data_type),
            serialization=core_schema.plain_serializer_function_ser_schema(
                conv.serialize
            ),
        )

    setattr(data_type, "__get_pydantic_core_schema__", classmethod(validator))  # noqa


types = [XmlDate, XmlDateTime, XmlTime, XmlDuration, XmlPeriod]
for tp in types:
    set_validator(tp, str_schema())
