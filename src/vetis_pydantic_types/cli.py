#!/usr/bin/env python3
"""Модуль с CLI командами."""
import shutil
import subprocess
from datetime import date

import click
from vetis_pydantic_types import __version__
import vetis_pydantic_types.mercury.services as mercury_services
import vetis_pydantic_types.mercury.constants as mercury_constants
import vetis_pydantic_types.herriot.services as herriot_services
import vetis_pydantic_types.herriot.constants as herriot_constants
from vetis_pydantic_types.base import VetisCircuitEnum
from vetis_pydantic_types.constants import XSDATA_CONFIG_FILE, TYPES_PACKAGE, TEST_TYPES_PACKAGE, PROD_TYPES_PACKAGE, \
    ROOT_DIR
from vetis_pydantic_types.version_manager import update_version_with_vetis_type_changes


@click.command()
@click.version_option(version=__version__)
def generate_vetis_types():
    """Основная команда CLI."""

    def generate_pydantic_types(wsdl_url, package):
        config_file = XSDATA_CONFIG_FILE.resolve()
        root_dir = ROOT_DIR.parent.resolve()
        result = subprocess.run(
            [
                "xsdata",
                "generate",
                wsdl_url,
                "--config",
                config_file,
                "--package",
                package,
                "--debug",
            ],
            cwd=root_dir,
            text=True,
        )


    def get_package_name(module_package, service, need_split_types):
        result = None
        module_name = module_package

        if need_split_types:
            if service.circuit == VetisCircuitEnum.TEST:
                result = f'{module_name}.{TEST_TYPES_PACKAGE}'
            elif service.circuit == VetisCircuitEnum.PRODUCTIVE:
                result = f'{module_name}.{PROD_TYPES_PACKAGE}'
        else:
            result = f'{module_name}.{TYPES_PACKAGE}'

        return result

    types_package = ROOT_DIR / f'{mercury_services.__package__.split(".")[-1]}/{TYPES_PACKAGE}'
    if types_package.exists() and types_package.is_dir():
        shutil.rmtree(str(types_package.resolve()))

    for mercury_service in (
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
        mercury_services.ams_productive_service,
        mercury_services.ams_test_service,
    ):
        package_name = get_package_name(
            mercury_services.__package__,
            mercury_service,
            mercury_constants.SPLIT_CIRCUIT_TYPES,
        )
        generate_pydantic_types(mercury_service.wsdl_uri, package_name)

    types_package = ROOT_DIR / f'{herriot_services.__package__.split(".")[-1]}/{TYPES_PACKAGE}'
    if types_package.exists() and types_package.is_dir():
        shutil.rmtree(str(types_package.resolve()))

    for herriot_service in (
        herriot_services.dictionary_productive_service,
        herriot_services.dictionary_test_service,
        herriot_services.enterprise_productive_service,
        herriot_services.enterprise_test_service,
        herriot_services.ikar_productive_service,
        herriot_services.ikar_test_service,
        herriot_services.product_productive_service,
        herriot_services.product_test_service,
        herriot_services.ams_productive_service,
        herriot_services.ams_test_service,
    ):
        package_name = get_package_name(herriot_services.__package__, herriot_service, herriot_constants)
        generate_pydantic_types(herriot_service.wsdl_uri, package_name)

    update_version_with_vetis_type_changes(date.today())

if __name__ == '__main__':
    generate_vetis_types()
