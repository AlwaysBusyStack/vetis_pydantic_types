from vetis_pydantic_types.base import VetisAMSService, VetisCircuitEnum
from vetis_pydantic_types.crpt.constants import VERSION, SERVICE_ID, AMS_NAME, API_URI, API_PORT, VERSION_URL

# AMS сервисы ГИС МТ (только тестовый контур)
crpt_ams_test_service = VetisAMSService(
    name=AMS_NAME,
    service_id=SERVICE_ID,
    version=VERSION,
    circuit=VetisCircuitEnum.TEST,
    wsdl_uri=f'{VERSION_URL}/ams-crpt-gateway.service_v{VERSION}_pilot.wsdl',
    api_uri=API_URI,
    api_port=API_PORT,
)
