from pathlib import Path

TYPES_PACKAGE = 'types'
ROOT_DIR = Path(__file__).parent
XSDATA_CONFIG_FILE = ROOT_DIR / '.xsdata.xml'
TEST_TYPES_PACKAGE = f'{TYPES_PACKAGE}.pilot'
PROD_TYPES_PACKAGE = f'{TYPES_PACKAGE}.production'

COMMON_NS_PREFIXES = {
    # Префиксы стандартных подключаемых схем в SOAP-файлах
    'soap': 'http://schemas.xmlsoap.org/wsdl/soap/',
    'wsdl': 'http://schemas.xmlsoap.org/wsdl/',
    'xlink': 'http://www.w3.org/1999/xlink',
    'xml': 'http://www.w3.org/XML/1998/namespace',
    'xs': 'http://www.w3.org/2001/XMLSchema',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    # Префиксы неймспейсов, содержащих общие типы данных
    # для всех веб-сервисов ВетИС.API
    'bsdef': 'http://api.vetrf.ru/schema/cdm/base/ws-definitions',
    # Префиксы неймспейсов, содержащих прикладные типы данных
    'bs': 'http://api.vetrf.ru/schema/cdm/base',
    'dt': 'http://api.vetrf.ru/schema/cdm/dictionary/v2',
    'vd': 'http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2',
}

AMS_SPECIFIC_NS_PREFIXES = {
    # типы данных для описания заявки для заявочной системы
    'apl': 'http://api.vetrf.ru/schema/cdm/application',
    # возможные типы запросов в заявочные системы
    'apldef': 'http://api.vetrf.ru/schema/cdm/application/ws-definitions',
}
AMS_PREFIXES = COMMON_NS_PREFIXES | AMS_SPECIFIC_NS_PREFIXES

REGISTRY_SPECIFIC_NS_PREFIXES = {
    # возможные типы запросов в справочные системы
    'ws': 'http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2',
}
REGISTRY_PREFIXES = COMMON_NS_PREFIXES | REGISTRY_SPECIFIC_NS_PREFIXES

VERSION_FILE = ROOT_DIR / 'version.json'
MILLISECONDS_PER_SECOND = 1000
