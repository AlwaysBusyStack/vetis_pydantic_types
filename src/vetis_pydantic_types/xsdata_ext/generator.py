from inspect import getsource
from pathlib import Path
from typing import List, Optional, Dict

from xsdata.codegen.models import Class, Attr
from xsdata.formats.dataclass.filters import Filters
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import Tag
from xsdata_pydantic.generator import PydanticGenerator, PydanticFilters

from vetis_pydantic_types.base.fields import xsdata_to_pydantic_restriction_keys_map
from vetis_pydantic_types.xsdata_ext.codegen_extensions import URL_TO_EXTENSIONS_SETTINGS


class VetisPydanticGenerator(PydanticGenerator):
    """Генератор pydantic классов для типов ВетИС.API."""

    # стандартный шаблон изменен для расширения логики генерации сервисов
    service_template = 'vetis_service.jinja2'
    enum_template = 'vetis_enum.jinja2'

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

    def render_classes(
        self,
        classes: list[Class],
        module_namespace: Optional[str],
    ) -> str:
        result = super().render_classes(classes, module_namespace)
        classes_sources = []

        if module_namespace in URL_TO_EXTENSIONS_SETTINGS:
            extensions = URL_TO_EXTENSIONS_SETTINGS[module_namespace]

            classes_sources = [
                getsource(class_to_insert)
                for class_to_insert in extensions['insert_classes']
            ]

        return "\n".join((
            *classes_sources,
            result,
        ))


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

    def field_type(self, obj: Class, attr: Attr) -> str:
        # TODO: Ужасный костыль - этот фильтр вызывается из Jinja-темплейта,
        #  а этот фильтр имеет специальный сайд-эффект, а именно: изменение
        #  обязательности присутствия ошибок - xsdata считает все Fault-ы
        #  обязательными в SOAP, тогда как сам SOAP - нет :)
        #  Лучше сделать PR в xsdata, правящий метод генерации
        #  атрибутов DefinitionsMapper.build_parts_attributes
        # Починка Fault-ов - они не должны быть обязательными
        # по протоколу SOAP
        if obj.tag == Tag.BINDING_MESSAGE and attr.name.endswith("Fault"):
            attr.restrictions.min_occurs = 0

        result = super().field_type(obj, attr)

        if tns := URL_TO_EXTENSIONS_SETTINGS.get(obj.target_namespace):
            annotations_changes = tns.get('change_annotations')
            lookup = f'{self.class_name(obj.name)}.{self.field_name(attr.name, obj.name)}'

            if annotations_changes and lookup in annotations_changes:
                result = annotations_changes[lookup]

        return result

    def field_definition(
        self,
        obj: Class,
        attr: Attr,
        parent_namespace: Optional[str],
    ) -> str:
        """Return the field definition with any extra metadata."""
        ns_map = obj.ns_map
        default_value = self.field_default_value(attr, ns_map)
        metadata = self.field_metadata(obj, attr, parent_namespace)

        kwargs = {}
        if attr.fixed or attr.is_prohibited:
            kwargs["init"] = False

            if attr.is_prohibited:
                kwargs[self.DEFAULT_KEY] = None

        if default_value is not False and not attr.is_prohibited:
            key = self.FACTORY_KEY if attr.is_factory else self.DEFAULT_KEY
            kwargs[key] = default_value

        if metadata:
            kwargs["metadata"] = metadata

        if attr.is_prohibited:
            del kwargs['init']
            kwargs['exclude'] = True
            kwargs['default'] = None
        elif attr.fixed:
            del kwargs['init']
            kwargs['const'] = True

        # удаляем мета информацию об ограничениях простых типов,
        # если для поля подменяли тип динамически
        if tns := URL_TO_EXTENSIONS_SETTINGS.get(obj.target_namespace):
            annotations_changes = tns.get('change_annotations')
            lookup = f'{self.class_name(obj.name)}.{self.field_name(attr.name, obj.name)}'

            if annotations_changes and lookup in annotations_changes:
                for xsdata_key in xsdata_to_pydantic_restriction_keys_map.keys():
                    if xsdata_key in metadata:
                        del metadata[xsdata_key]

        return f"field({self.format_arguments(kwargs, 4)})"

    @classmethod
    def build_import_patterns(cls) -> Dict[str, Dict]:
        patterns = super().build_import_patterns()
        patterns.update(
            {
                "xsdata_pydantic.fields": {},
                "vetis_pydantic_types.base.fields": {"field": [" = field("]},
            }
        )

        return {key: patterns[key] for key in sorted(patterns)}
