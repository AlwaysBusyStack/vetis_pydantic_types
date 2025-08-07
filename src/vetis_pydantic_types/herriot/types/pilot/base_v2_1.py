from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDateTime, XmlDuration

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


class BinaryData(BaseModel):
    """
    Содержимое вложенного документа в формате base64.
    """

    model_config = ConfigDict(defer_build=True)
    value: bytes = field(
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2005/05/xmlmime",
            "min_length": 3,
        },
    )


class ComplexDate(BaseModel):
    """
    Тип, описывающий дату.

    Attributes:
        year: Год
        month: Месяц
        day: День
        hour: Час
        minute: Час
    """

    model_config = ConfigDict(defer_build=True)
    year: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "pattern": r"[1-2][0-9][0-9][0-9]",
        },
    )
    month: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "min_inclusive": 1,
            "max_inclusive": 12,
        },
    )
    day: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "min_inclusive": 1,
            "max_inclusive": 31,
        },
    )
    hour: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "min_inclusive": 0,
            "max_inclusive": 23,
        },
    )
    minute: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "min_inclusive": 0,
            "max_inclusive": 59,
        },
    )


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
        cursor: Текущее значение указателя на положение в результирующем
            списке
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
    cursor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 100,
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


class FileReference(BaseModel):
    """
    Ссылка на файл, загруженный в хранилище.
    """

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
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


class HashAlgorithm(Enum):
    GOST3411_2012_256 = "GOST3411-2012.256"
    GOST3411_2012_512 = "GOST3411-2012.512"
    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"

    __descriptions = {
        GOST3411_2012_256: "",
        GOST3411_2012_512: "",
        SHA_1: "",
        SHA_256: "",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        HashAlgorithm.GOST3411_2012_256.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ListOptionsInternalType(BaseModel):
    """
    Тип, определяющий параметры запрашиваемого у сервиса списка объектов.

    Attributes:
        count: Максимальное запрашиваемое количество объектов в списке.
        offset: Номер элемента, по которому осуществляется смещение
            первого элемента списка.
        cursor: Указатель на положение в результирующем списке
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
    cursor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "max_length": 100,
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


class ComplexDatePeriod(BaseModel):
    """
    Интервал дат.

    Attributes:
        date: Точное значение.
        start_date: Минимальное значение.
        end_date: Максимальное значение.
        duration: Длительность периода
    """

    model_config = ConfigDict(defer_build=True)
    date: Optional[ComplexDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    start_date: Optional[ComplexDate] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    end_date: Optional[ComplexDate] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
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


class FileDigest(BaseModel):
    """
    Attributes:
        value:
        algorithm_id: Идентификатор алгоритма хэширования
        algorithm_name: Название алгоритма хэширования
    """

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    algorithm_id: Optional[HashAlgorithm] = field(
        default=None,
        metadata={
            "name": "algorithmId",
            "type": "Attribute",
        },
    )
    algorithm_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "algorithmName",
            "type": "Attribute",
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


class File(BaseModel):
    """
    Содержимое вложенного документа с возможностью передачи открепленной подписи.

    Attributes:
        id: Идентификатор файла.
        file_name: Название файла.
        mime_code: MIME-код файла, представленного в бинарном виде.
        encoding: Кодировка файла, представленного в бинарном виде.
        file_size: Размер файла в байтах.
        file_digest: Хеш-значение для файла в соответствии с указанным
            алгоритмом.
        reference_id: Ссылка или идентификатор файла в хранилище.
        binary_data: Содержимое файла в формате base64.
        signature: Открепленная подпись файла.
    """

    model_config = ConfigDict(defer_build=True)
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "max_length": 100,
        },
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "max_length": 255,
        },
    )
    mime_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeCode",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    file_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "fileSize",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    file_digest: Optional[FileDigest] = field(
        default=None,
        metadata={
            "name": "fileDigest",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    reference_id: Optional[FileReference] = field(
        default=None,
        metadata={
            "name": "referenceId",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    binary_data: Optional[BinaryData] = field(
        default=None,
        metadata={
            "name": "binaryData",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    signature: list[BinaryData] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
