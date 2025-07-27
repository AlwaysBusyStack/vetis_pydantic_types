import json
import os
from datetime import datetime

from vetis_pydantic_types.constants import VERSION_FILE


class VersionManager:
    """Простой менеджер версий в формате YYYY.MM.DD.FIX_NUMBER"""

    def __init__(self):
        self.config_file = VERSION_FILE
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """Загружает конфигурацию"""

        if os.path.exists(self.config_file):
            with open(self.config_file, 'r', encoding='utf-8') as f:
                content = f.read()

            config = json.loads(content) if content else {}
        else:
            raise FileNotFoundError('Файл с настройками версии не существует')

        return config

    def _save_config(self):
        """Сохраняет конфигурацию"""

        with open(self.config_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.config, ensure_ascii=False, indent=2))

    def get_version(self) -> str:
        """Возвращает текущую версию"""

        date = self.config.get('vetis_types_generation_date') or ''
        fix_num = self.config.get('fix_num') or 0

        return f"{date}.{fix_num:02d}"

    def set_types_date(self, date: datetime.date):
        """Устанавливает дату получения типов, сбрасывает номер фикса в 01"""

        date_str = date.strftime("%Y.%m.%d")

        # Если дата изменилась - сбрасываем фикс
        if self.config.get('vetis_types_generation_date') != date_str:
            self.config['fix_number'] = 1

        self.config['vetis_types_generation_date'] = date_str
        self._save_config()

    def increment_fix(self):
        """Увеличивает номер фикса"""

        self.config["fix_number"] += 1
        self._save_config()


def update_version_with_vetis_type_changes(date: datetime.date):
    """Вызывать из скрипта получения типов.

    Args:
        date: Дата изменения версии.
    """

    vm = VersionManager()
    vm.set_types_date(date)


def increment_fix_number():
    """Увеличивает номер фикса."""

    vm = VersionManager()
    vm.increment_fix()


def get_current_version() -> str:
    """Получить текущую версию"""

    vm = VersionManager()

    return vm.get_version()
