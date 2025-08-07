from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime

from vetis_pydantic_types.base.fields import field

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/base"


class VersionStatus(Enum):
    """Тип, описывающий статусы версионных объектов."""

    CREATED = "100"
    CREATED_WHEN_MERGE = "110"
    CREATED_WHEN_SPLIT = "120"
    UPDATED = "200"
    UPDATED_WHEN_ATTACH = "230"
    UPDATED_WHEN_FORK = "240"
    MOVED = "300"
    DELETED = "400"
    DELETED_WHEN_MERGE = "410"
    DELETED_WHEN_SPLIT = "420"
    DELETED_WHEN_ATTACH = "430"

    __descriptions = {
        CREATED: "Запись создана",
        CREATED_WHEN_MERGE: "Запись создана в результате объединения двух или более других",
        CREATED_WHEN_SPLIT: "Запись создана в результате разделения другой",
        UPDATED: "В запись были внесены изменения",
        UPDATED_WHEN_ATTACH: "Запись была обновлена в результате присоединения другой",
        UPDATED_WHEN_FORK: "Запись была обновлена в результате отделения от неё другой",
        MOVED: "Запись была перемещена в другую группу (для иерархических справочников)",
        DELETED: "Запись была удалена",
        DELETED_WHEN_MERGE: "Запись была удалена в результате объединения",
        DELETED_WHEN_SPLIT: "Запись была удалена в результате разделения",
        DELETED_WHEN_ATTACH: "Запись была удалена в результате присоединения",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VersionStatus.CREATED.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class DateInterval(BaseModel):
    """
    Тип, с помощью которого задается временной интервал.

    Attributes:
        begin_date: Начало временного интервала.
        end_date: Конец временного интервала.
    """

    model_config = ConfigDict(defer_build=True)
    begin_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "beginDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )


class EntityList(BaseModel):
    """
    Базовый тип для описания списков сущностей.

    Attributes:
        count: Размер списка, передаваемого в ответе на запрос.
        total: Размер всего списка, удовлетворяющего запросу.
        offset: Смещение первого элемента передаваемого списка во всем
            списке результатов, удовлетворяющих запросу.
        has_more: Признак того, что передаваемая часть (страница)
            списка, удовлетворяющего запросу, не является последней. Для
            списка в ответе сервиса обязательным является наличие одного
            из двух атрибутов: total или hasMore
    """

    model_config = ConfigDict(defer_build=True)
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    total: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    has_more: Optional[bool] = field(
        default=None,
        metadata={
            "name": "hasMore",
            "type": "Attribute",
        },
    )


class Error(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    qualifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 100,
        },
    )


class GenericEntity(BaseModel):
    """
    Тип, базовый для любой сущности системы.

    Attributes:
        uuid: Идентификатор сущности.
    """

    model_config = ConfigDict(defer_build=True)
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class ListOptionsInternalType(BaseModel):
    """
    Тип, определяющий параметры запрашиваемого у сервиса списка объектов.

    Attributes:
        count: Максимальное запрашиваемое количество объектов в списке.
        offset: Номер элемента, по которому осуществляется смещение
            первого элемента списка.
    """

    class Meta:
        name = "ListOptions"

    model_config = ConfigDict(defer_build=True)
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )


class RegisterModificationType(Enum):
    """
    Тип операции на изменение реестра.

    Attributes:
        CREATE: Добавление новой записи.
        FIND_OR_CREATE: Поиск существующей или добавление новой записи.
            [CREATE IF NOT EXISTS]
        UPDATE: Внесение изменений в существующую запись.
        DELETE: Удаление существующей записи.
        MERGE: Объединение двух или нескольких записей.
        ATTACH: Присоединение одной или нескольких записе к другой.
        SPLIT: Разделение записи на две и более.
        FORK: Отделение одной и более записей от существующей.
    """

    CREATE = "CREATE"
    FIND_OR_CREATE = "FIND_OR_CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    MERGE = "MERGE"
    ATTACH = "ATTACH"
    SPLIT = "SPLIT"
    FORK = "FORK"

    __descriptions = {
        CREATE: "Добавление новой записи.",
        FIND_OR_CREATE: "Поиск существующей или добавление новой записи. [CREATE IF NOT EXISTS]",
        UPDATE: "Внесение изменений в существующую запись.",
        DELETE: "Удаление существующей записи.",
        MERGE: "Объединение двух или нескольких записей.",
        ATTACH: "Присоединение одной или нескольких записе к другой.",
        SPLIT: "Разделение записи на две и более.",
        FORK: "Отделение одной и более записей от существующей.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        RegisterModificationType.CREATE.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class Guid(BaseModel):
    class Meta:
        name = "guid"
        namespace = "http://api.vetrf.ru/schema/cdm/base"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class Uuid(BaseModel):
    class Meta:
        name = "uuid"
        namespace = "http://api.vetrf.ru/schema/cdm/base"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class FaultInfo(BaseModel):
    """
    Тип, описываюший ошибки.
    """

    model_config = ConfigDict(defer_build=True)
    message: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )
    error: list[Error] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )


class GenericVersioningEntity(GenericEntity):
    """
    Тип, базовый для сущностей, поддерживающих версии.

    Attributes:
        guid: Глобальный идентификатор в системах Россельхознадзора.
        active: Флаг, определяющий актуальность записи.
        last: Флаг, указывающий на то, что запись является последней в
            истории.
        status: Статус объекта.
        create_date: Дата создания объекта.
        update_date: Дата последнего обновления объекта.
        previous: Идентификатор предыдущей версии объекта.
        next: Идентификатор последующей версии объекта.
    """

    model_config = ConfigDict(defer_build=True)
    guid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    last: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    status: VersionStatus = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    create_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "createDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    update_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "updateDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    previous: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )
    next: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class ListOptions(ListOptionsInternalType):
    class Meta:
        name = "listOptions"
        namespace = "http://api.vetrf.ru/schema/cdm/base"

    model_config = ConfigDict(defer_build=True)


class UpdateDateInterval(DateInterval):
    class Meta:
        name = "updateDateInterval"
        namespace = "http://api.vetrf.ru/schema/cdm/base"

    model_config = ConfigDict(defer_build=True)
