from typing import Optional, Dict, Type, Tuple
from pydantic import BaseModel


class BaseApplication:
    """Базовый класс для ответа/запроса заявок."""

    @staticmethod
    def _get_doc_str_by(bases: Tuple[Type, ...]) -> Optional[str]:
        """Возвращает докстринг к ответу/заявке.

        Т.к. в xsd-схемах содержится довольно специфичное описание,
        настоящий докстринг может располагаться в базовом классе.
        """

        result = None

        for base in bases:
            if not issubclass(base, BaseApplication) and (doc_str := base.__doc__):
                # пропускаем докстринг pydantic.BaseModel
                if base is not BaseModel:
                    result = doc_str
                    break

        return result


class ApplicationRequest(BaseApplication):
    """Заявка/запрос."""

    def __init_subclass__(cls, **kwargs):
        """Динамически модифицирует докстринг класса (если он пуст)
        докстрингом базового класса.
        """
        super().__init_subclass__(**kwargs)

        cls.__doc__ = cls.__doc__ or cls._get_doc_str_by(cls.__bases__)


class ApplicationResponse(BaseApplication):
    """Ответ по заявке/запросу."""

    def __init_subclass__(cls, **kwargs):
        """Динамически модифицирует докстринг класса (если он пуст)
        докстрингом базового класса.
        """
        super().__init_subclass__(**kwargs)

        cls.__doc__ = cls.__doc__ or cls._get_doc_str_by(cls.__bases__)
