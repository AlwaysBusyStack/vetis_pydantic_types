from vetis_pydantic_types.base import VetisCircuitEnum, \
    VetisAMSService, VetisDictionaryService
from vetis_pydantic_types.mercury.constants import CURRENT_VERSION_URL, TEST_API_URI, TEST_API_PORT, AMS_SERVICE_ID, \
    VERSION, PROD_API_URI, PROD_API_PORT, AMS_VERBOSE_NAME, DICTIONARY_VERBOSE_NAME, ENTERPRISE_VERBOSE_NAME, \
    IKAR_VERBOSE_NAME, PRODUCT_VERBOSE_NAME, REGIONALIZATION_VERBOSE_NAME

# Сервисы работы с заявками компонента Меркурий
ams_productive_service = VetisAMSService(
    name=AMS_VERBOSE_NAME,
    service_id=AMS_SERVICE_ID,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    wsdl_uri=f'{CURRENT_VERSION_URL}/ams-mercury-g2b.service_v{VERSION}_production.wsdl',
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
)
ams_test_service = VetisAMSService(
    name=AMS_VERBOSE_NAME,
    service_id=AMS_SERVICE_ID,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    wsdl_uri=f'{CURRENT_VERSION_URL}/ams-mercury-g2b.service_v{VERSION}_pilot.wsdl',
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
)

# Справочные сервисы компонента Меркурий
# Сервисы получения справочной информации
dictionary_productive_service = VetisDictionaryService(
    name=DICTIONARY_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    wsdl_uri=f'{CURRENT_VERSION_URL}/DictionaryService_v{VERSION}_production.wsdl',
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
)
dictionary_test_service = VetisDictionaryService(
    name=DICTIONARY_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    wsdl_uri=f'{CURRENT_VERSION_URL}/DictionaryService_v{VERSION}_pilot.wsdl',
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
)

# Сервисы получения реестра хозяйствующих субъектов и предприятий (Цербер)
enterprise_productive_service = VetisDictionaryService(
    name=ENTERPRISE_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    wsdl_uri=f'{CURRENT_VERSION_URL}/EnterpriseService_v{VERSION}_production.wsdl',
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
)
enterprise_test_service = VetisDictionaryService(
    name=ENTERPRISE_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    wsdl_uri=f'{CURRENT_VERSION_URL}/EnterpriseService_v{VERSION}_pilot.wsdl',
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
)

# Сервисы получения адресной справочной информации (Икар)
ikar_productive_service = VetisDictionaryService(
    name=IKAR_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    wsdl_uri=f'{CURRENT_VERSION_URL}/IkarService_v{VERSION}_production.wsdl',
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
)
ikar_test_service = VetisDictionaryService(
    name=IKAR_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    wsdl_uri=f'{CURRENT_VERSION_URL}/IkarService_v{VERSION}_pilot.wsdl',
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
)

# Сервисы получения реестра категорий продукции
product_productive_service = VetisDictionaryService(
    name=PRODUCT_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    wsdl_uri=f'{CURRENT_VERSION_URL}/ProductService_v{VERSION}_production.wsdl',
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
)
product_test_service = VetisDictionaryService(
    name=PRODUCT_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    wsdl_uri=f'{CURRENT_VERSION_URL}/ProductService_v{VERSION}_pilot.wsdl',
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
)

# Сервисы проверки благополучия регионов и получения правил регионализации
regionalization_productive_service = VetisDictionaryService(
    name=REGIONALIZATION_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    wsdl_uri=f'{CURRENT_VERSION_URL}/RegionalizationService_v{VERSION}_production.wsdl',
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
)
regionalization_test_service = VetisDictionaryService(
    name=REGIONALIZATION_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    wsdl_uri=f'{CURRENT_VERSION_URL}/RegionalizationService_v{VERSION}_pilot.wsdl',
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
)
