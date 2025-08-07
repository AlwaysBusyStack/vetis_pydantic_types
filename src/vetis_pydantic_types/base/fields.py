from typing import Optional, Dict, Any, Callable

from pydantic_core import PydanticUndefined
from xsdata_pydantic.fields import FieldInfo


xsdata_to_pydantic_restriction_keys_map = {
    'min_exclusive': 'gt',
    'min_inclusive': 'ge',
    'max_exclusive': 'lt',
    'max_inclusive': 'le',
    'total_digits': 'max_digits',
    'fraction_digits': 'decimal_places',
    'min_length': 'min_length',
    'max_length': 'max_length',
    'pattern': 'pattern',
}

def field(
    metadata: Optional[Dict[str, Any]] = None,
    *,
    default: Any = PydanticUndefined,
    default_factory: Optional[Callable[[], Any]] = PydanticUndefined,
    **kwargs: Any,
):
    """Переопределение xsdata_pydantic.fields.field для отображения
    ограничений в полях схем.
    """

    for xsdata_key, pydantic_key in xsdata_to_pydantic_restriction_keys_map.items():
        if metadata_value := metadata.get(xsdata_key):
            kwargs.setdefault(pydantic_key, metadata_value)

    return FieldInfo(
        metadata=metadata,
        default=default,
        default_factory=default_factory,
        **kwargs,
    )
