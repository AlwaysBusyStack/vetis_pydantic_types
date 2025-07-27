from pathlib import Path
from typing import List

from xsdata.codegen.models import Class
from xsdata.formats.dataclass.filters import Filters
from xsdata.models.config import GeneratorConfig
from xsdata_pydantic.generator import PydanticGenerator, PydanticFilters


class VetisPydanticGenerator(PydanticGenerator):
    """Генератор pydantic классов для типов ВетИС.API."""

    # стандартный шаблон изменен для расширения логики генерации сервисов
    service_template = 'vetis_service.jinja2'

    @classmethod
    def init_filters(cls, config: GeneratorConfig) -> Filters:
        return VetisPydanticFilters(config)

    @classmethod
    def get_template_paths(cls):
        paths = super().get_template_paths()

        # добавляем шаблоны приложения в окружение Jinja
        paths.extend((
            str(Path(__file__).parent.joinpath("templates")),
        ))

        return paths


class VetisPydanticFilters(PydanticFilters):
    def __init__(self, config: GeneratorConfig):
        super().__init__(config)

    def class_bases(self, obj: Class, class_name: str) -> List[str]:
        """Получает наследуемые классы во время генерации классов."""

        # если нужно сгенерировать код для сервиса - нужно перепрыгнуть
        # xsdata-pydantic логику, и перейти к базовой
        if obj.is_service:
            result = super(PydanticFilters, self).class_bases(obj, class_name)
        else:
            result = super().class_bases(obj, class_name)

        return result
