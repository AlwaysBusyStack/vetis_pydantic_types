PLATFORM_URL = 'http://api.vetrf.ru/schema/platform'

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

AMS_SERVICE_ID = f'herriot.service:1.0'
AMS_VERBOSE_NAME = 'Подсистема обработки заявок компонента Меркурий'
DICTIONARY_VERBOSE_NAME = 'Сервис получения справочной информации'
ENTERPRISE_VERBOSE_NAME = 'Сервис получения реестра хозяйствующих субъектов и предприятий (Цербер)'
IKAR_VERBOSE_NAME = 'Сервис получения адресной справочной информации (Икар)'
PRODUCT_VERBOSE_NAME = 'Сервис получения реестра категорий продукции'
