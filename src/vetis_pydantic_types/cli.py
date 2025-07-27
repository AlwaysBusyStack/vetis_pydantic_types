#!/usr/bin/env python3
"""Модуль с CLI командами."""
import click
from xsdata.cli import generate
from vetis_pydantic_types import __version__
import vetis_pydantic_types.mercury.services as mercury_services
import vetis_pydantic_types.mercury.constants as mercury_constants
import vetis_pydantic_types.herriot.services as herriot_services
import vetis_pydantic_types.herriot.constants as herriot_constants
import vetis_pydantic_types.crpt.services as crpt_services
import vetis_pydantic_types.crpt.constants as crpt_constants
from vetis_pydantic_types.base import VetisCircuitEnum
from vetis_pydantic_types.constants import XSDATA_CONFIG_FILE, TYPES_PACKAGE, TEST_TYPES_PACKAGE, PROD_TYPES_PACKAGE

@click.command()
@click.version_option(version=__version__)
def main():
    """Основная команда CLI."""

    def generate_pydantic_types(wsdl_url, package):
        generate.callback(
            debug=True,
            cache=False,
            recursive=False,
            source=wsdl_url,
            config=XSDATA_CONFIG_FILE,
            package=package,
        )

    def get_package_name(module_package, service, service_constants):
        result = None
        module_name = module_package.split('.')[-1]

        if service_constants.SPLIT_CIRCUIT_TYPES:
            if service.circuit == VetisCircuitEnum.TEST:
                result = f'{module_name}.{TEST_TYPES_PACKAGE}'
            elif service.circuit == VetisCircuitEnum.PRODUCTIVE:
                result = f'{module_name}.{PROD_TYPES_PACKAGE}'
        else:
            result = f'{module_name}.{TYPES_PACKAGE}'

        return result

    for mercury_service in (
        mercury_services.ams_productive_service,
        mercury_services.ams_test_service,
        mercury_services.dictionary_productive_service,
        mercury_services.dictionary_test_service,
        mercury_services.enterprise_productive_service,
        mercury_services.enterprise_test_service,
        mercury_services.ikar_productive_service,
        mercury_services.ikar_test_service,
        mercury_services.product_productive_service,
        mercury_services.product_test_service,
        mercury_services.regionalization_productive_service,
        mercury_services.regionalization_test_service,
    ):
        package_name = get_package_name(mercury_services.__package__, mercury_service, mercury_constants)
        generate_pydantic_types(mercury_service.wsdl_uri, package_name)

    for herriot_service in (
        herriot_services.ams_productive_service,
        herriot_services.ams_test_service,
        herriot_services.dictionary_productive_service,
        herriot_services.dictionary_test_service,
        herriot_services.enterprise_productive_service,
        herriot_services.enterprise_test_service,
        herriot_services.ikar_productive_service,
        herriot_services.ikar_test_service,
        herriot_services.product_productive_service,
        herriot_services.product_test_service,
    ):
        package_name = get_package_name(herriot_services.__package__, herriot_service, herriot_constants)
        generate_pydantic_types(herriot_service.wsdl_uri, package_name)

    for crpt_service in (
        crpt_services.crpt_ams_test_service,
    ):
        package_name = get_package_name(crpt_services.__package__, mercury_service, crpt_constants)
        generate_pydantic_types(crpt_service.wsdl_uri, package_name)


if __name__ == '__main__':
    main()
