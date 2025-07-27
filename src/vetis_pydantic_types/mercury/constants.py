from vetis_pydantic_types.constants import AMS_PREFIXES, REGISTRY_PREFIXES

PLATFORM_URL = 'http://api.vetrf.ru/schema/platform'
VERSION = '2.1'
CURRENT_VERSION_URL = f'{PLATFORM_URL}/services/{VERSION}-RC-last'
TEST_API_URI = 'https://api2.vetrf.ru'
TEST_API_PORT = 8002
PROD_API_URI = 'https://api.vetrf.ru'
PROD_API_PORT = None

AMS_SERVICE_ID = f'mercury-g2b.service:{VERSION}'
AMS_VERBOSE_NAME = 'Подсистема обработки заявок компонента Меркурий'
AMS_NS_PREFIXES = AMS_PREFIXES

DICTIONARY_VERBOSE_NAME = 'Сервис получения справочной информации'
DICTIONARY_NS_PREFIXES = REGISTRY_PREFIXES | {
    'tns': 'http://api.vetrf.ru/schema/cdm/registry/dictionary/service/v2',
}

ENTERPRISE_VERBOSE_NAME = 'Сервис получения реестра хозяйствующих субъектов и предприятий (Цербер)'
ENTERPRISE_NS_PREFIXES = REGISTRY_PREFIXES | {
    'tns': 'http://api.vetrf.ru/schema/cdm/registry/enterprise/service/v2',
}

IKAR_VERBOSE_NAME = 'Сервис получения адресной справочной информации (Икар)'
IKAR_NS_PREFIXES = REGISTRY_PREFIXES | {
    'tns': 'http://api.vetrf.ru/schema/cdm/registry/ikar/service/v2',
}

PRODUCT_VERBOSE_NAME = 'Сервис получения реестра категорий продукции'
PRODUCT_NS_PREFIXES = REGISTRY_PREFIXES | {
    'tns': 'http://api.vetrf.ru/schema/cdm/registry/r13n/service/v2',
}

REGIONALIZATION_VERBOSE_NAME = 'Сервис проверки благополучия регионов и получения правил регионализации'
REGIONALIZATION_NS_PREFIXES = REGISTRY_PREFIXES | {
    'tns': 'http://api.vetrf.ru/schema/cdm/registry/product/service/v2',
}

SPLIT_CIRCUIT_TYPES = False
