from vetis_pydantic_types.constants import AMS_PREFIXES

PLATFORM_URL = 'http://api.vetrf.ru/schema/platform'

VERSION = '1.0'
VERSION_URL = f'{PLATFORM_URL}/crptgw/v{VERSION}.0-crpt-latest'

AMS_NAME = 'Маркировка товаров (ГИС МТ)'
AMS_NS_PREFIXES = AMS_PREFIXES
SERVICE_ID = 'crpt-gateway.service'
API_URI = 'https://api2.vetrf.ru'
API_PORT = 8002

SPLIT_CIRCUIT_TYPES = False
