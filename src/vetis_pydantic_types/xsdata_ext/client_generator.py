"""
Генератор клиентов Vetis.
"""
import importlib
import inspect
import re
import pkgutil
from collections import defaultdict
from collections.abc import Iterator
from pathlib import Path
from typing import Any, Dict, List, Optional, Type, Tuple, Iterable

from jinja2 import Environment, FileSystemLoader
from xsdata.codegen.models import Class
from xsdata.formats.dataclass.filters import Filters
from xsdata.formats.mixins import AbstractGenerator, GeneratorResult
from xsdata.models.config import GeneratorConfig

import vetis_pydantic_types.mercury.services as mercury_services
import vetis_pydantic_types.herriot.services as herriot_services
from vetis_pydantic_types.base import (
    BaseOperation,
    RegistryOperation,
    ReceiveApplicationResultOperation,
    SubmitApplicationRequestOperation,
    VetisAMSService,
    VetisRegistryService,
    VetisCircuitEnum,
    BaseVetisService,
)
from vetis_pydantic_types.constants import XSDATA_CONFIG_FILE


class VetisTypesCollector:
    """Сборщик типов операций Vetis."""

    def __init__(self):
        # Собираем все сервисы в одну кучу
        self.all_services = [
            *[
                getattr(mercury_services, attr)
                for attr in dir(mercury_services)
                if not attr.startswith('_') and isinstance(
                    getattr(mercury_services, attr), BaseVetisService
                )
            ],
            *[
                getattr(herriot_services, attr)
                for attr in dir(herriot_services)
                if not attr.startswith('_') and isinstance(
                    getattr(herriot_services, attr), BaseVetisService
                )
            ]
        ]

    def collect_all_services(self) -> List[Class]:
        """Собирает все сервисы с операциями в формате xsdata.Class."""
        # Группируем сервисы по wsdl_uri (без pilot/production суффиксов)
        service_groups = {}

        for service in self.all_services:
            base_wsdl = self._get_base_wsdl(service.wsdl_uri)

            if base_wsdl not in service_groups:
                service_groups[base_wsdl] = {
                    'test': None,
                    'production': None
                }

            if service.circuit == VetisCircuitEnum.TEST:
                service_groups[base_wsdl]['test'] = service
            else:
                service_groups[base_wsdl]['production'] = service

        # Создаем Class объекты для каждой группы
        result = []
        for base_wsdl, group in service_groups.items():
            if group['test'] and group['production']:
                cls = self._create_service_class(group)
                if cls:
                    result.append(cls)

        return result

    def _get_base_wsdl(self, wsdl_uri: str) -> str:
        """Получает базовый WSDL URI без pilot/production суффиксов."""
        return re.sub(r'_(pilot|production)\.wsdl$', '.wsdl', wsdl_uri)

    def _create_service_class(self, group: Dict[str, Any]) -> Optional[Class]:
        """Создает xsdata.Class объект для сервиса."""
        test_service = group['test']
        production_service = group['production']

        is_ams = isinstance(test_service, VetisAMSService)

        # Получаем операции для сервиса
        operations = self._collect_operations_for_service(test_service)
        if not operations:
            return None

        # Создаем имя клиента на основе WSDL
        client_name = self._extract_client_name(test_service.wsdl_uri, is_ams)
        service_name = self._extract_service_name(test_service.wsdl_uri)

        # Находим имена переменных сервисов
        test_service_var = self._find_service_variable(test_service)
        production_service_var = self._find_service_variable(production_service)

        # Находим модули с операциями
        pilot_module_name, product_module_name = self._find_operation_modules(test_service)

        # Создаем Class объект
        cls = Class(
            qname=f"{service_name}.{client_name}",
            module=service_name,
            package=service_name,
            tag='Client',
            location='generated'
        )

        # Сохраняем метаданные в Class
        cls.meta = {
            'service_name': service_name,
            'client_name': client_name,
            'component_name': test_service.component_name,  # Добавляем component_name
            'is_ams': is_ams,
            'operations': operations,
            'test_service_instance': test_service,
            'test_service_var': test_service_var,
            'production_service_instance': production_service,
            'production_service_var': production_service_var,
            'class_help': f'"""Клиент, который покрывает "{test_service.verbose_name}"."""',
            'pilot_module': pilot_module_name,
            'pilot_module_name': f'{service_name}_{VetisCircuitEnum.TEST.value}',
            'product_module': product_module_name,
            'product_module_name': f'{service_name}_{VetisCircuitEnum.PRODUCTIVE.value}',
        }

        return cls

    def _extract_client_name(self, wsdl_uri: str, is_ams: bool) -> str:
        """Создает имя клиента на основе WSDL URI."""
        # Извлекаем базовое имя сервиса
        service_name = self._extract_service_name(wsdl_uri)

        # Формируем имя клиента
        if is_ams:
            client_name = "AMSClient"
        else:
            client_name = f"{service_name.capitalize()}Client"

        return client_name

    def _extract_service_name(self, wsdl_uri: str) -> str:
        """Извлекает имя сервиса из WSDL URI."""
        # Ищем паттерн: /ServiceName_v2.1_production.wsdl
        match = re.search(r'/(\w+)(?:_v[\d.]+)?(?:_production|_pilot)?\.wsdl', wsdl_uri)
        if match:
            service_name = match.group(1)
            # Убираем Service суффикс если есть
            if service_name.endswith('Service'):
                service_name = service_name[:-7]
            return service_name.lower()
        return 'unknown'

    def _find_service_variable(self, service: BaseVetisService) -> str:
        """Находит имя переменной сервиса."""
        # Ищем в mercury_services
        for attr_name in dir(mercury_services):
            if not attr_name.startswith('_'):
                attr_value = getattr(mercury_services, attr_name)
                if attr_value is service:
                    return attr_name

        # Ищем в herriot_services
        for attr_name in dir(herriot_services):
            if not attr_name.startswith('_'):
                attr_value = getattr(herriot_services, attr_name)
                if attr_value is service:
                    return attr_name

        raise ValueError(f"Не найдена переменная для сервиса {service}")

    def _find_operation_modules(self, service: BaseVetisService) -> Tuple[str, str]:
        """Находит модули с операциями для сервиса."""
        component = service.component_name
        tns_namespace = service.ns_map['tns']

        # Сканируем все модули в types
        types_package = f"vetis_pydantic_types.{component}.types"

        pilot_module = None
        production_module = None

        # Получаем список всех модулей в пакете types
        component_types = importlib.import_module(types_package)

        for _, module_name, _ in pkgutil.iter_modules(component_types.__path__):
            full_module_name = f"{types_package}.{module_name}"

            try:
                module = importlib.import_module(full_module_name)

                # Проверяем __NAMESPACE__
                if hasattr(module, '__NAMESPACE__') and module.__NAMESPACE__ == tns_namespace:
                    if 'pilot' in module_name:
                        pilot_module = full_module_name
                    elif 'production' in module_name:
                        production_module = full_module_name
                    else:
                        # Если нет разделения pilot/production
                        pilot_module = production_module = full_module_name

            except ImportError:
                continue

        return pilot_module, production_module

    def _collect_operations_for_service(self, service: BaseVetisService) -> List[Dict[str, Any]]:
        """Собирает операции для сервиса."""
        pilot_module_name, production_module_name = self._find_operation_modules(service)

        operations = []

        # Загружаем модули
        for module_name in [pilot_module_name, production_module_name]:
            if module_name == 'unknown':
                continue

            try:
                module = importlib.import_module(module_name)
                module_operations = self._extract_operations_from_module(module)
                operations.extend(module_operations)
            except ImportError:
                continue

        # Убираем дубликаты по имени операции
        unique_operations = {}
        for op in operations:
            op_name = op['name']
            if op_name not in unique_operations:
                unique_operations[op_name] = op

        return list(unique_operations.values())

    def _extract_operations_from_module(self, module) -> List[Dict[str, Any]]:
        """Извлекает операции из модуля."""
        operations = []

        for attr_name in dir(module):
            if attr_name.startswith('_'):
                continue

            attr_value = getattr(module, attr_name)

            if self._is_operation_class(attr_value):
                operation_info = self._parse_operation_class(attr_value)
                if operation_info:
                    operations.append(operation_info)

        return operations

    def _is_operation_class(self, obj) -> bool:
        """Проверяет, является ли объект классом операции."""
        return (
            inspect.isclass(obj) and
            issubclass(obj, BaseOperation)
        )

    def _parse_operation_class(self, operation_cls: Type) -> Optional[Dict[str, Any]]:
        """Парсит класс операции."""
        try:
            temp_instance = operation_cls(client=None)
            input_field_name, input_info = temp_instance.input_info
            output_field_name, output_info = temp_instance.output_info
            # Если Optional[ResponseType] - нужно вытащить ResponseType
            response_type = (
                output_info.annotation
                if output_info.annotation._name != 'Optional'
                else output_info.annotation.__args__[0]
            )

            class_name = operation_cls.__name__
            operation_name = self._extract_operation_name(class_name)

            if not operation_name:
                return None

            return {
                'name': operation_name,
                'description': input_info.annotation.__doc__.split('Attributes')[0].strip(),
                'request_type': self._get_type_name(input_info.annotation),
                'response_type': self._get_type_name(response_type),
            }
        except Exception:
            return None

    def _extract_operation_name(self, class_name: str) -> Optional[str]:
        """Извлекает имя операции из названия класса."""
        match = re.match(r'(\w+)ServicePortType(\w+)', class_name)
        if match:
            return match.group(2)
        return None

    def _get_type_name(self, type_annotation) -> str:
        """Получает имя типа."""
        if hasattr(type_annotation, '__name__'):
            return type_annotation.__name__
        return str(type_annotation)


class VetisClientGenerator(AbstractGenerator):
    """Генератор клиентов для Vetis API."""

    def __init__(self, config: GeneratorConfig, templates_dir: Path):
        super().__init__(config)
        self._import_patterns = None
        self.templates_dir = templates_dir
        self.collector = VetisTypesCollector()
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            trim_blocks=True,
            lstrip_blocks=True
        )
        self._setup_filters()

    @property
    def import_patterns(self):
        if not self._import_patterns:
            import_patterns = Filters.build_import_patterns()
            import_patterns["typing"]['Coroutine'] = 'Coroutine'
            import_patterns["typing"]['Dict'] = 'Dict'
            import_patterns.update({
                'requests.auth': {
                    'HTTPBasicAuth': 'HTTPBasicAuth',
                },
                'vetis_pydantic_types.base': {
                    'VetisCircuitEnum': 'VetisCircuitEnum',
                    'VetisRegistryClient': 'VetisRegistryClient',
                },
            })

            self._import_patterns = import_patterns

        return self._import_patterns

    def add_client_imports(self, classes, component_name: str):
        """Добавляет импорты для клиентов конкретного компонента."""
        # Добавляем импорты сервисов для компонента
        services_module = f"vetis_pydantic_types.{component_name}.services"
        self.import_patterns[services_module] = {}

        # Собираем все имена сервисов для данного компонента
        for cls in classes:
            meta = cls.meta
            if meta['component_name'] == component_name:
                test_service_var = meta['test_service_var']
                production_service_var = meta['production_service_var']

                # Добавляем в импорты
                self.import_patterns[services_module][test_service_var] = test_service_var
                self.import_patterns[services_module][production_service_var] = production_service_var

        # Добавляем импорты типов для компонента
        for cls in classes:
            meta = cls.meta
            if meta['component_name'] == component_name:
                test_service_instance = meta['test_service_instance']
                is_types_splited = test_service_instance.split_circuit_types

                types_str = f"vetis_pydantic_types.{component_name}.types"
                if is_types_splited:
                    test_types_str = f'{types_str}.{VetisCircuitEnum.TEST.value}'
                    prod_types_str = f'{types_str}.{VetisCircuitEnum.PRODUCTIVE.value}'

                    for types_module in [test_types_str, prod_types_str]:
                        module = importlib.import_module(types_module)
                        if hasattr(module, '__all__'):
                            self.import_patterns[types_module] = {
                                type_: type_ for type_ in module.__all__
                            }
                else:
                    module = importlib.import_module(types_str)
                    if hasattr(module, '__all__'):
                        self.import_patterns[types_str] = {
                            type_: type_ for type_ in module.__all__
                        }

    def _setup_filters(self):
        """Регистрация фильтров."""
        def operation_name_filter(name: str) -> str:
            return f"{name}Operation"

        def function_name_filter(name: str) -> str:
            return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

        self.jinja_env.filters['operation_name'] = operation_name_filter
        self.jinja_env.filters['function_name'] = function_name_filter

    def unique_sequence(self, items: Iterable[Any], key: Optional[str] = None) -> list[Any]:
        """Return a new unique list, preserving the original order.

        Args:
            items: The iterable to filter
            key: An optional callable to generate the unique keys

        Returns:
            A new unique list.
        """
        seen = set()

        def is_new(val: Any) -> bool:
            if key:
                val = getattr(val, key)

            if val in seen:
                return False

            seen.add(val)
            return True

        return [item for item in items if is_new(item)]

    def default_imports(self, output: str) -> str:
        """Generate the default imports for the given package output."""
        imports = []
        for library, types in self.import_patterns.items():
            names = [
                name
                for name, searches in types.items()
                if any(search in output for search in searches)
            ]

            if len(names) == 1 and names[0] == "__module__":
                imports.append(f"import {library}")
            elif names:
                imports.append(f"from {library} import {', '.join(names)}")

        return "\n".join(self.unique_sequence(imports))

    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        """Генерирует клиенты раздельно для каждого компонента."""
        collected_classes = self.collector.collect_all_services()

        if not classes:
            classes = collected_classes
        else:
            classes.extend(collected_classes)

        # Группируем классы по component_name
        classes_by_component = defaultdict(list)
        for cls in classes:
            component_name = cls.meta['component_name']
            classes_by_component[component_name].append(cls)

        # Генерируем файл для каждого компонента
        for component_name, component_classes in classes_by_component.items():
            # Очищаем импорты для нового компонента
            self._import_patterns = None

            # Добавляем импорты для текущего компонента
            self.add_client_imports(component_classes, component_name)

            # Собираем всех клиентов компонента в один файл
            all_clients = []

            for cls in component_classes:
                meta = cls.meta

                template_data = {
                    'class_name': meta['client_name'],
                    'class_help': meta['class_help'],
                    'operations': meta['operations'],
                    'test_service_name': meta['test_service_var'],
                    'production_service_name': meta['production_service_var'],
                    'pilot_module_name': meta['pilot_module_name'],
                    'product_module_name': meta['product_module_name'],
                }

                template_name = 'vetis_ams_client.jinja2' if meta['is_ams'] else 'vetis_registry_client.jinja2'
                template = self.jinja_env.get_template(template_name)

                client_code = template.render(**template_data)
                all_clients.append(client_code)

            # Собираем весь файл для компонента
            header = self.render_header()
            full_source = "\n\n\n".join(all_clients)
            imports = self.default_imports(full_source)
            full_source = header + imports + '\n\n\n' + full_source

            # Имя файла для компонента
            filename = f"{component_name}_clients.py"

            yield GeneratorResult(
                path=Path(filename),
                title=f"Vetis {component_name.capitalize()} Clients",
                source=full_source
            )


def generate_all_clients(templates_dir: Path, output_dir: Path) -> None:
    """
    Генерирует клиентов Vetis раздельно для каждого компонента.

    Args:
        templates_dir: Путь к директории с шаблонами
        output_dir: Путь к директории для сохранения файлов клиентов
    """
    config = GeneratorConfig.read(XSDATA_CONFIG_FILE.resolve())
    generator = VetisClientGenerator(config, templates_dir)

    # Генерируем файлы клиентов
    output_dir.mkdir(exist_ok=True)

    generated_files = []
    for result in generator.render([]):
        output_file = output_dir / result.path
        output_file.write_text(result.source, encoding='utf-8')
        generated_files.append(result.path)
        print(f"✅ Сгенерирован {result.path}")

    print(f"🎉 Сгенерировано {len(generated_files)} файлов клиентов:")
    for filename in generated_files:
        print(f"   - {filename}")


if __name__ == "__main__":
    templates_dir = Path(__file__).parent / "templates"
    output_dir = Path(__file__).parent / "generated_clients"

    generate_all_clients(templates_dir, output_dir)
