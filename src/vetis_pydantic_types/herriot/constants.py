from vetis_pydantic_types.constants import AMS_PREFIXES, REGISTRY_PREFIXES

PLATFORM_URL = 'http://api.vetrf.ru/schema/platform'

COMPONENT_NAME = __file__.rsplit('/', maxsplit=2)[-2]
VERSION = '1.0'
VERSION_BETA = f'v{VERSION}b'
TEST_VERSION = f'{VERSION_BETA}-20250203'
PROD_VERSION = f'{VERSION_BETA}-20240216'

PROD_VERSION_URL = f'{PLATFORM_URL}/herriot/{VERSION_BETA}-last'
TEST_VERSION_URL = f'{PLATFORM_URL}/herriot/{PROD_VERSION}'

TEST_API_URI = 'https://api2.vetrf.ru'
TEST_API_PORT = 8002
PROD_API_URI = 'https://api.vetrf.ru'
PROD_API_PORT = None

HERRIOT_SPECIFIC_NS_PREFIXES = {
    # Префикс неймспейсов специфичных прикладных типов Хорриот
    'cl': 'http://api.vetrf.ru/schema/cdm/codelist/v2',
}

AMS_SERVICE_ID = f'herriot.service:1.0'
AMS_VERBOSE_NAME = 'Подсистема обработки заявок компонента Хорриот'
AMS_NS_PREFIXES = AMS_PREFIXES | HERRIOT_SPECIFIC_NS_PREFIXES | {
    # возможные типы заявок компонента Хорриот
    'hrt': 'http://api.vetrf.ru/schema/cdm/herriot/applications/v1',
    'tns': 'http://api.vetrf.ru/schema/cdm/application/service',
}

DICTIONARY_VERBOSE_NAME = 'Сервис получения справочной информации'
DICTIONARY_NS_PREFIXES = REGISTRY_PREFIXES | HERRIOT_SPECIFIC_NS_PREFIXES | {
    'tns': 'http://api.vetrf.ru/schema/cdm/registry/dictionary/service/v3',
}

ENTERPRISE_VERBOSE_NAME = 'Сервис получения реестра хозяйствующих субъектов и предприятий (Цербер)'
ENTERPRISE_NS_PREFIXES = REGISTRY_PREFIXES | HERRIOT_SPECIFIC_NS_PREFIXES | {
    'tns': 'http://api.vetrf.ru/schema/cdm/registry/enterprise/service/v3',
}

IKAR_VERBOSE_NAME = 'Сервис получения адресной справочной информации (Икар)'
IKAR_NS_PREFIXES = REGISTRY_PREFIXES | HERRIOT_SPECIFIC_NS_PREFIXES | {
    'tns': 'http://api.vetrf.ru/schema/cdm/registry/ikar/service/v3',
}

PRODUCT_VERBOSE_NAME = 'Сервис получения реестра категорий продукции'
PRODUCT_NS_PREFIXES = REGISTRY_PREFIXES | HERRIOT_SPECIFIC_NS_PREFIXES | {
    'tns': 'http://api.vetrf.ru/schema/cdm/registry/product/service/v3',
}

SPLIT_CIRCUIT_TYPES = True
