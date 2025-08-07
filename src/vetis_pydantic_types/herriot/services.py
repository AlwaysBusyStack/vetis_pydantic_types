from vetis_pydantic_types.base import VetisAMSService, VetisCircuitEnum, VetisDictionaryService
from vetis_pydantic_types.herriot.constants import TEST_API_URI, TEST_API_PORT, AMS_SERVICE_ID, \
    PROD_API_URI, PROD_API_PORT, AMS_VERBOSE_NAME, DICTIONARY_VERBOSE_NAME, ENTERPRISE_VERBOSE_NAME, \
    IKAR_VERBOSE_NAME, PRODUCT_VERBOSE_NAME, PROD_VERSION, PROD_VERSION_URL, TEST_VERSION, TEST_VERSION_URL, VERSION, \
    AMS_NS_PREFIXES, DICTIONARY_NS_PREFIXES, ENTERPRISE_NS_PREFIXES, IKAR_NS_PREFIXES, PRODUCT_NS_PREFIXES, \
    COMPONENT_NAME, SPLIT_CIRCUIT_TYPES

# Сервисы работы с заявками компонента Меркурий
# HerriotApplicationRequest
ams_productive_service = VetisAMSService(
    component_name=COMPONENT_NAME,
    verbose_name=AMS_VERBOSE_NAME,
    service_id=AMS_SERVICE_ID,
    version=PROD_VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    ns_map=AMS_NS_PREFIXES,
    wsdl_uri=f'{PROD_VERSION_URL}/ams-herriot.service_v{VERSION}.wsdl',
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
ams_test_service = VetisAMSService(
    component_name=COMPONENT_NAME,
    verbose_name=AMS_VERBOSE_NAME,
    service_id=AMS_SERVICE_ID,
    version=TEST_VERSION,
    circuit=VetisCircuitEnum.TEST,
    ns_map=AMS_NS_PREFIXES,
    wsdl_uri=f'{TEST_VERSION_URL}/ams-herriot.service_v{VERSION}.wsdl',
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)

# Справочные сервисы компонента Меркурий
# Сервисы получения справочной информации
dictionary_productive_service = VetisDictionaryService(
    component_name=COMPONENT_NAME,
    verbose_name=DICTIONARY_VERBOSE_NAME,
    version=PROD_VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    ns_map=DICTIONARY_NS_PREFIXES,
    wsdl_uri=f'{PROD_VERSION_URL}/DictionaryService_v{VERSION}.wsdl',
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
dictionary_test_service = VetisDictionaryService(
    component_name=COMPONENT_NAME,
    verbose_name=DICTIONARY_VERBOSE_NAME,
    version=TEST_VERSION,
    circuit=VetisCircuitEnum.TEST,
    ns_map=DICTIONARY_NS_PREFIXES,
    wsdl_uri=f'{TEST_VERSION_URL}/DictionaryService_v{VERSION}.wsdl',
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)

# Сервисы получения реестра хозяйствующих субъектов и предприятий (Цербер)
enterprise_productive_service = VetisDictionaryService(
    component_name=COMPONENT_NAME,
    verbose_name=ENTERPRISE_VERBOSE_NAME,
    version=PROD_VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    ns_map=ENTERPRISE_NS_PREFIXES,
    wsdl_uri=f'{PROD_VERSION_URL}/EnterpriseService_v{VERSION}.wsdl',
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
enterprise_test_service = VetisDictionaryService(
    component_name=COMPONENT_NAME,
    verbose_name=ENTERPRISE_VERBOSE_NAME,
    version=TEST_VERSION,
    circuit=VetisCircuitEnum.TEST,
    ns_map=ENTERPRISE_NS_PREFIXES,
    wsdl_uri=f'{TEST_VERSION_URL}/EnterpriseService_v{VERSION}.wsdl',
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)

# Сервисы получения адресной справочной информации (Икар)
ikar_productive_service = VetisDictionaryService(
    component_name=COMPONENT_NAME,
    verbose_name=IKAR_VERBOSE_NAME,
    version=PROD_VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    ns_map=IKAR_NS_PREFIXES,
    wsdl_uri=f'{PROD_VERSION_URL}/IkarService_v{VERSION}.wsdl',
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
ikar_test_service = VetisDictionaryService(
    component_name=COMPONENT_NAME,
    verbose_name=IKAR_VERBOSE_NAME,
    version=TEST_VERSION,
    circuit=VetisCircuitEnum.TEST,
    ns_map=IKAR_NS_PREFIXES,
    wsdl_uri=f'{TEST_VERSION_URL}/IkarService_v{VERSION}.wsdl',
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)

# Сервисы получения реестра категорий продукции
product_productive_service = VetisDictionaryService(
    component_name=COMPONENT_NAME,
    verbose_name=PRODUCT_VERBOSE_NAME,
    version=PROD_VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    ns_map=PRODUCT_NS_PREFIXES,
    wsdl_uri=f'{TEST_VERSION_URL}/ProductService_v{VERSION}.wsdl',
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
product_test_service = VetisDictionaryService(
    component_name=COMPONENT_NAME,
    verbose_name=PRODUCT_VERBOSE_NAME,
    version=TEST_VERSION,
    circuit=VetisCircuitEnum.TEST,
    ns_map=PRODUCT_NS_PREFIXES,
    wsdl_uri=f'{PROD_VERSION_URL}/ProductService_v{VERSION}.wsdl',
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
