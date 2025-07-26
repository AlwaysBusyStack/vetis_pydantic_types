PLATFORM_URL = 'http://api.vetrf.ru/schema/platform'
VERSION = '2.1'
CURRENT_VERSION_URL = f'{PLATFORM_URL}/services/{VERSION}-RC-last'
TEST_API_URI = 'https://api2.vetrf.ru'
TEST_API_PORT = 8002
PROD_API_URI = 'https://api.vetrf.ru'
PROD_API_PORT = None

AMS_SERVICE_ID = f'mercury-g2b.service:{VERSION}'
AMS_VERBOSE_NAME = 'Подсистема обработки заявок компонента Меркурий'
DICTIONARY_VERBOSE_NAME = 'Сервис получения справочной информации'
ENTERPRISE_VERBOSE_NAME = 'Сервис получения реестра хозяйствующих субъектов и предприятий (Цербер)'
IKAR_VERBOSE_NAME = 'Сервис получения адресной справочной информации (Икар)'
PRODUCT_VERBOSE_NAME = 'Сервис получения реестра категорий продукции'
REGIONALIZATION_VERBOSE_NAME = 'Сервис проверки благополучия регионов и получения правил регионализации'
