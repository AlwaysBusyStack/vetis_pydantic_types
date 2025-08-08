from vetis_pydantic_types.version_manager import get_current_version
from vetis_pydantic_types import logging

# версия пакета - дата, т.к. содержание типов очень сильно зависит
# от даты их генерации. Версия строится по формату:
# год.месяц.день.fix_number
__version__ = get_current_version()
