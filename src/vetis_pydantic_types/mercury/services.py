from vetis_pydantic_types.base import (
    VetisAMSService,
    VetisCircuitEnum,
    VetisRegistryService,
)
from vetis_pydantic_types.mercury.constants import (
    AMS_NS_PREFIXES,
    AMS_SERVICE_ID,
    AMS_VERBOSE_NAME,
    COMPONENT_NAME,
    CURRENT_VERSION_URL,
    DICTIONARY_NS_PREFIXES,
    DICTIONARY_VERBOSE_NAME,
    ENTERPRISE_NS_PREFIXES,
    ENTERPRISE_VERBOSE_NAME,
    IKAR_NS_PREFIXES,
    IKAR_VERBOSE_NAME,
    PROD_API_PORT,
    PROD_API_URI,
    PRODUCT_NS_PREFIXES,
    PRODUCT_VERBOSE_NAME,
    REGIONALIZATION_NS_PREFIXES,
    REGIONALIZATION_VERBOSE_NAME,
    SPLIT_CIRCUIT_TYPES,
    TEST_API_PORT,
    TEST_API_URI,
    VERSION,
)

# Сервисы работы с заявками компонента Меркурий
ams_productive_service = VetisAMSService(
    component_name=COMPONENT_NAME,
    verbose_name=AMS_VERBOSE_NAME,
    service_id=AMS_SERVICE_ID,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    ns_map=AMS_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/ams-mercury-g2b.service_v{VERSION}_production.wsdl",
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
ams_test_service = VetisAMSService(
    component_name=COMPONENT_NAME,
    verbose_name=AMS_VERBOSE_NAME,
    service_id=AMS_SERVICE_ID,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    ns_map=AMS_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/ams-mercury-g2b.service_v{VERSION}_pilot.wsdl",
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)

# Справочные сервисы компонента Меркурий
# Сервисы получения справочной информации
dictionary_productive_service = VetisRegistryService(
    component_name=COMPONENT_NAME,
    verbose_name=DICTIONARY_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    ns_map=DICTIONARY_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/DictionaryService_v{VERSION}_production.wsdl",
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
dictionary_test_service = VetisRegistryService(
    component_name=COMPONENT_NAME,
    verbose_name=DICTIONARY_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    ns_map=DICTIONARY_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/DictionaryService_v{VERSION}_pilot.wsdl",
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)

# Сервисы получения реестра хозяйствующих субъектов и предприятий (Цербер)
enterprise_productive_service = VetisRegistryService(
    component_name=COMPONENT_NAME,
    verbose_name=ENTERPRISE_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    ns_map=ENTERPRISE_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/EnterpriseService_v{VERSION}_production.wsdl",
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
enterprise_test_service = VetisRegistryService(
    component_name=COMPONENT_NAME,
    verbose_name=ENTERPRISE_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    ns_map=ENTERPRISE_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/EnterpriseService_v{VERSION}_pilot.wsdl",
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)

# Сервисы получения адресной справочной информации (Икар)
ikar_productive_service = VetisRegistryService(
    component_name=COMPONENT_NAME,
    verbose_name=IKAR_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    ns_map=IKAR_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/IkarService_v{VERSION}_production.wsdl",
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
ikar_test_service = VetisRegistryService(
    component_name=COMPONENT_NAME,
    verbose_name=IKAR_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    ns_map=IKAR_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/IkarService_v{VERSION}_pilot.wsdl",
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)

# Сервисы получения реестра категорий продукции
product_productive_service = VetisRegistryService(
    component_name=COMPONENT_NAME,
    verbose_name=PRODUCT_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    ns_map=PRODUCT_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/ProductService_v{VERSION}_production.wsdl",
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
product_test_service = VetisRegistryService(
    component_name=COMPONENT_NAME,
    verbose_name=PRODUCT_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    ns_map=PRODUCT_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/ProductService_v{VERSION}_pilot.wsdl",
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)

# Сервисы проверки благополучия регионов и получения правил регионализации
regionalization_productive_service = VetisRegistryService(
    component_name=COMPONENT_NAME,
    verbose_name=REGIONALIZATION_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.PRODUCTIVE,
    ns_map=REGIONALIZATION_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/RegionalizationService_v{VERSION}_production.wsdl",
    api_uri=PROD_API_URI,
    api_port=PROD_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
regionalization_test_service = VetisRegistryService(
    component_name=COMPONENT_NAME,
    verbose_name=REGIONALIZATION_VERBOSE_NAME,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    ns_map=REGIONALIZATION_NS_PREFIXES,
    wsdl_uri=f"{CURRENT_VERSION_URL}/RegionalizationService_v{VERSION}_pilot.wsdl",
    api_uri=TEST_API_URI,
    api_port=TEST_API_PORT,
    split_circuit_types=SPLIT_CIRCUIT_TYPES,
)
