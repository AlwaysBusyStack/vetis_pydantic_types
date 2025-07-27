from pathlib import Path

TYPES_PACKAGE = 'types'
ROOT_DIR = Path(__file__).parent
XSDATA_CONFIG_FILE = ROOT_DIR / '.xsdata.xml'
TEST_TYPES_PACKAGE = f'{TYPES_PACKAGE}.pilot'
PROD_TYPES_PACKAGE = f'{TYPES_PACKAGE}.production'

COMMON_NS_PREFIXES = {
    'soap': 'http://schemas.xmlsoap.org/wsdl/soap/',
    'wsdl': 'http://schemas.xmlsoap.org/wsdl/',
    'xlink': 'http://www.w3.org/1999/xlink',
    'xml': 'http://www.w3.org/XML/1998/namespace',
    'xs': 'http://www.w3.org/2001/XMLSchema',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
}

AMS_SPECIFIC_NS_PREFIXES = {
    'bsdef': 'http://api.vetrf.ru/schema/cdm/base/ws-definitions',
    'def': 'http://api.vetrf.ru/schema/cdm/application/ws-definitions',
    'tns': 'http://api.vetrf.ru/schema/cdm/application/service',
}
AMS_PREFIXES = COMMON_NS_PREFIXES | AMS_SPECIFIC_NS_PREFIXES


REGISTRY_SPECIFIC_NS_PREFIXES = {
    'bsdef': 'http://api.vetrf.ru/schema/cdm/base/ws-definitions',
    'def': 'http://api.vetrf.ru/schema/cdm/application/ws-definitions',
    'tns': 'http://api.vetrf.ru/schema/cdm/application/service',
}
REGISTRY_PREFIXES = COMMON_NS_PREFIXES | REGISTRY_SPECIFIC_NS_PREFIXES

VERSION_FILE = ROOT_DIR / 'version.json'
