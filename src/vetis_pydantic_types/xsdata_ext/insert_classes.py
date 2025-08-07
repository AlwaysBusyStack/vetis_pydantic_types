from enum import Enum


# Интересное решение от разработчиков ВетИС.API. Вместо создания типа с
# возможными значениями - сделали простой числовой тип, а о значениях
# рассказали в документации :)
# Правим это вставкой этого класса в генерацию кода pydantic схем,
# после чего заменим аннотации типов в полях на этот тип
class VersionStatus(Enum):
    """Тип, описывающий статусы версионных объектов."""
    CREATED = '100'
    CREATED_WHEN_MERGE = '110'
    CREATED_WHEN_SPLIT = '120'
    UPDATED = '200'
    UPDATED_WHEN_ATTACH = '230'
    UPDATED_WHEN_FORK = '240'
    MOVED = '300'
    DELETED = '400'
    DELETED_WHEN_MERGE = '410'
    DELETED_WHEN_SPLIT = '420'
    DELETED_WHEN_ATTACH = '430'

    __descriptions = {
        CREATED: 'Запись создана',
        CREATED_WHEN_MERGE: 'Запись создана в результате объединения двух или более других',
        CREATED_WHEN_SPLIT: 'Запись создана в результате разделения другой',
        UPDATED: 'В запись были внесены изменения',
        UPDATED_WHEN_ATTACH: 'Запись была обновлена в результате присоединения другой',
        UPDATED_WHEN_FORK: 'Запись была обновлена в результате отделения от неё другой',
        MOVED: 'Запись была перемещена в другую группу (для иерархических справочников)',
        DELETED: 'Запись была удалена',
        DELETED_WHEN_MERGE: 'Запись была удалена в результате объединения',
        DELETED_WHEN_SPLIT: 'Запись была удалена в результате разделения',
        DELETED_WHEN_ATTACH: 'Запись была удалена в результате присоединения'
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VersionStatus.CREATED.verbose_name
        """

        return type(self).__descriptions.get(self.value)
