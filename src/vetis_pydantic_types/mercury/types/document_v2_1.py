from __future__ import annotations

from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate, XmlDateTime

from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.mercury.types.base_v2_0 import (
    DateInterval,
    EntityList,
    GenericEntity,
    GenericVersioningEntity,
    RegisterModificationType,
)
from vetis_pydantic_types.mercury.types.dictionary_v2_1 import (
    AnimalDisease,
    Area,
    BusinessEntityInternalType,
    BusinessEntityListInternalType,
    BusinessMemberInternalType,
    ComplexDate,
    CountryInternalType,
    DocumentNature,
    DocumentType,
    EnterpriseInternalType,
    EnterpriseListInternalType,
    Indicator,
    Location,
    MedicinalDrug,
    Organization,
    PackageList,
    ProducerInternalType,
    ProductInternalType,
    ProductItemInternalType,
    ProductItemListInternalType,
    ProductTypeInternalType,
    PurposeInternalType,
    ReferenceType,
    RegionalizationCondition,
    RegionalizationShippingRule,
    ResearchMethodInternalType,
    ResearchResult,
    SubProductInternalType,
    TransportationStorageType,
    TransportType,
    UnitInternalType,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"


class AnimalSpentPeriod(Enum):
    """
    Сколько времени животные находились на территории ТС.

    Attributes:
        FROM_BIRTH: Животные находились на территории ТС с рождения
        NOT_LESS_SIX_MONTHS: Животные находились на территории ТС не
            менее 6 месяцев
        IN_MONTHS: Животные находились на территории ТС указанное кол-во
            месяцев
        ZERO: Животные не находились на территории ТС
    """

    FROM_BIRTH = "FROM_BIRTH"
    NOT_LESS_SIX_MONTHS = "NOT_LESS_SIX_MONTHS"
    IN_MONTHS = "IN_MONTHS"
    ZERO = "ZERO"

    __descriptions = {
        FROM_BIRTH: "Животные находились на территории ТС с рождения",
        NOT_LESS_SIX_MONTHS: "Животные находились на территории ТС не менее 6 месяцев",
        IN_MONTHS: "Животные находились на территории ТС указанное кол-во месяцев",
        ZERO: "Животные не находились на территории ТС",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalSpentPeriod.FROM_BIRTH.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class DeliveryDecision(Enum):
    """
    Решение по поставке.

    Attributes:
        ACCEPT_ALL: Принять всю поставку.
        PARTIALLY: Принять часть груза, на оставшуюся оформить возврат.
        RETURN_ALL: Оформить возврат на всю поставку.
    """

    ACCEPT_ALL = "ACCEPT_ALL"
    PARTIALLY = "PARTIALLY"
    RETURN_ALL = "RETURN_ALL"

    __descriptions = {
        ACCEPT_ALL: "Принять всю поставку.",
        PARTIALLY: "Принять часть груза, на оставшуюся оформить возврат.",
        RETURN_ALL: "Оформить возврат на всю поставку.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        DeliveryDecision.ACCEPT_ALL.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class DeliveryInspectionResult(Enum):
    """
    Результат контроля поставки.

    Attributes:
        CORRESPONDS: Груз соответствует сведениям, заявленным в
            документах.
        MISMATCH: Груз отличается от сведений, указанных в
            сопроводительных документах.
        UNSUPERVISED: Контроль не проводился.
    """

    CORRESPONDS = "CORRESPONDS"
    MISMATCH = "MISMATCH"
    UNSUPERVISED = "UNSUPERVISED"

    __descriptions = {
        CORRESPONDS: "Груз соответствует сведениям, заявленным в документах.",
        MISMATCH: "Груз отличается от сведений, указанных в сопроводительных документах.",
        UNSUPERVISED: "Контроль не проводился.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        DeliveryInspectionResult.CORRESPONDS.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class NonFoodProductSourceType(Enum):
    """
    Attributes:
        CATTLE_SLAUGHTER: Боенское.
        LOSS_OF_CATTLE: Палое.
        MANUFACTURED: Промышленное.
        MIXED: Сборное.
        FROM_HEALTHY_ANIMALS: Полученное от здоровых животных.
        FROM_SICK_ANIMALS: Полученное от больных животных.
    """

    CATTLE_SLAUGHTER = "CATTLE_SLAUGHTER"
    LOSS_OF_CATTLE = "LOSS_OF_CATTLE"
    MANUFACTURED = "MANUFACTURED"
    MIXED = "MIXED"
    FROM_HEALTHY_ANIMALS = "FROM_HEALTHY_ANIMALS"
    FROM_SICK_ANIMALS = "FROM_SICK_ANIMALS"

    __descriptions = {
        CATTLE_SLAUGHTER: "Боенское.",
        LOSS_OF_CATTLE: "Палое.",
        MANUFACTURED: "Промышленное.",
        MIXED: "Сборное.",
        FROM_HEALTHY_ANIMALS: "Полученное от здоровых животных.",
        FROM_SICK_ANIMALS: "Полученное от больных животных.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        NonFoodProductSourceType.CATTLE_SLAUGHTER.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ProcessingProcedureType(Enum):
    """
    Attributes:
        VALUE_7: Замораживание
        VALUE_12: Убой
        VALUE_13: Упаковка/фасовка
        VALUE_34: Нарезка/разделка
        VALUE_35: Добыча (собирать, ловить, охотиться)
        VALUE_37: Производство (из сырья вручную или с помощью машин)
        VALUE_39: Обработка/переработка (посредством, как правило,
            рутинных процедур)
        VALUE_40: Выращивание
        VALUE_43: Хранение
        VALUE_51: Сжигание (утилизация)
        VALUE_73: Временное хранения
        VALUE_95: Термическая обработка
        VALUE_101: Утилизация (метод не определен или отличается от
            обозначенных выше вариантов)
        VALUE_102: Сортировка и упаковка
    """

    VALUE_7 = "7"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_37 = "37"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_43 = "43"
    VALUE_51 = "51"
    VALUE_73 = "73"
    VALUE_95 = "95"
    VALUE_101 = "101"
    VALUE_102 = "102"

    __descriptions = {
        VALUE_7: "Замораживание",
        VALUE_12: "Убой",
        VALUE_13: "Упаковка/фасовка",
        VALUE_34: "Нарезка/разделка",
        VALUE_35: "Добыча (собирать, ловить, охотиться)",
        VALUE_37: "Производство (из сырья вручную или с помощью машин)",
        VALUE_39: "Обработка/переработка (посредством, как правило, рутинных процедур)",
        VALUE_40: "Выращивание",
        VALUE_43: "Хранение",
        VALUE_51: "Сжигание (утилизация)",
        VALUE_73: "Временное хранения",
        VALUE_95: "Термическая обработка",
        VALUE_101: (
            "Утилизация (метод не определен или отличается от обозначенных выше "
            "вариантов)"
        ),
        VALUE_102: "Сортировка и упаковка",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ProcessingProcedureType.VALUE_7.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class StockEntryBlankFilter(Enum):
    """
    Attributes:
        ALL: Все записи журнала, вне зависимости от объёма.
        BLANK: Записи журнала с нулевым объёмом.
        NOT_BLANK: Записи журнала с ненулевым объёмом.
    """

    ALL = "ALL"
    BLANK = "BLANK"
    NOT_BLANK = "NOT_BLANK"

    __descriptions = {
        ALL: "Все записи журнала, вне зависимости от объёма.",
        BLANK: "Записи журнала с нулевым объёмом.",
        NOT_BLANK: "Записи журнала с ненулевым объёмом.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        StockEntryBlankFilter.ALL.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class TransportNumber(BaseModel):
    """
    Номер транспортного средства.

    Attributes:
        container_number: Номер контейнера.
        wagon_number: Номер авиарейса.
        vehicle_number: Номер автомобиля.
        trailer_number: Номер прицепа (полуприцепа).
        ship_name: Название судна.
        flight_number: Номер авиарейса.
    """

    model_config = ConfigDict(defer_build=True)
    container_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "containerNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    wagon_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "wagonNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    vehicle_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    trailer_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "trailerNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    ship_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shipName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "flightNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )


class UserAuthority(BaseModel):
    """
    Тип, описывающий список ролей пользователя.
    """

    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    granted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class VetDocumentForm(Enum):
    """
    Тип, описывающий форму ВСД.

    Attributes:
        CERTCU1: Форма 1 ветеринарного сертификата ТС
        LIC1: Форма 1 ветеринарного свидетельства
        CERTCU2: Форма 2 ветеринарного сертификата ТС
        LIC2: Форма 2 ветеринарного свидетельства
        CERTCU3: Форма 3 ветеринарного сертификата ТС
        LIC3: Форма 3 ветеринарного свидетельства
        NOTE4: Форма 4 ветеринарной справки
        CERT5_I: Форма 5i ветеринарного сертификата
        CERT61: Форма 6.1 ветеринарного сертификата
        CERT62: Форма 6.2 ветеринарного сертификата
        CERT63: Форма 6.3 ветеринарного сертификата
        PRODUCTIVE: Форма производственного ветеринарного сертификата
    """

    CERTCU1 = "CERTCU1"
    LIC1 = "LIC1"
    CERTCU2 = "CERTCU2"
    LIC2 = "LIC2"
    CERTCU3 = "CERTCU3"
    LIC3 = "LIC3"
    NOTE4 = "NOTE4"
    CERT5_I = "CERT5I"
    CERT61 = "CERT61"
    CERT62 = "CERT62"
    CERT63 = "CERT63"
    PRODUCTIVE = "PRODUCTIVE"

    __descriptions = {
        CERTCU1: "Форма 1 ветеринарного сертификата ТС",
        LIC1: "Форма 1 ветеринарного свидетельства",
        CERTCU2: "Форма 2 ветеринарного сертификата ТС",
        LIC2: "Форма 2 ветеринарного свидетельства",
        CERTCU3: "Форма 3 ветеринарного сертификата ТС",
        LIC3: "Форма 3 ветеринарного свидетельства",
        NOTE4: "Форма 4 ветеринарной справки",
        CERT5_I: "Форма 5i ветеринарного сертификата",
        CERT61: "Форма 6.1 ветеринарного сертификата",
        CERT62: "Форма 6.2 ветеринарного сертификата",
        CERT63: "Форма 6.3 ветеринарного сертификата",
        PRODUCTIVE: "Форма производственного ветеринарного сертификата",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VetDocumentForm.CERTCU1.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VetDocumentStatusInternalType(Enum):
    """
    Статус ветсертификата.

    Attributes:
        CREATED: Создан. Неоформленный проект сертификата
        CONFIRMED: Оформлен. Действующий сертификат, по которому
            разрешено совершать транзакцию с грузом.
        WITHDRAWN: Аннулирован. Не действующий более сертификат.
        UTILIZED: Погашен. Действующий сертификат, по которому
            транзакция уже была совершена.
        FINALIZED: Закрыт. Действующий производственный сертификат.
            Статус проставляется при завершении производственной смены,
            изменение финализированного вет.сертификата не допускается.
            Статус `FINALIZED` не используется в атрибуте `vetDStatus`
            сертификата, признак того, что производственный сертификат
            финализирован определяется логическим атрибутом `finalized`
            сертификата. При этом сертификат всегда находится в статусе
            `CONFIRMED`.
    """

    CREATED = "CREATED"
    CONFIRMED = "CONFIRMED"
    WITHDRAWN = "WITHDRAWN"
    UTILIZED = "UTILIZED"
    FINALIZED = "FINALIZED"

    __descriptions = {
        CREATED: "Создан. Неоформленный проект сертификата",
        CONFIRMED: (
            "Оформлен. Действующий сертификат, по которому разрешено совершать "
            "транзакцию с\nгрузом."
        ),
        WITHDRAWN: "Аннулирован. Не действующий более сертификат.",
        UTILIZED: "Погашен. Действующий сертификат, по которому транзакция уже была совершена.",
        FINALIZED: (
            "Закрыт. Действующий производственный сертификат.\nСтатус проставляется "
            "при завершении производственной смены, изменение финализированного "
            "вет.сертификата не допускается.\nСтатус `FINALIZED` не используется в "
            "атрибуте `vetDStatus` сертификата, признак того, что производственный "
            "сертификат финализирован\nопределяется логическим атрибутом `finalized` "
            "сертификата. При этом сертификат всегда находится в статусе `CONFIRMED`."
        ),
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VetDocumentStatus_1.CREATED.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VetDocumentTypeInternalType(Enum):
    """
    Тип ветсертификата.

    Attributes:
        TRANSPORT: Транспортный
        PRODUCTIVE: Производственный
        RETURNABLE: Возвратный
        INCOMING: Входящий
        OUTGOING: Исходящий
    """

    TRANSPORT = "TRANSPORT"
    PRODUCTIVE = "PRODUCTIVE"
    RETURNABLE = "RETURNABLE"
    INCOMING = "INCOMING"
    OUTGOING = "OUTGOING"

    __descriptions = {
        TRANSPORT: "Транспортный",
        PRODUCTIVE: "Производственный",
        RETURNABLE: "Возвратный",
        INCOMING: "Входящий",
        OUTGOING: "Исходящий",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VetDocumentType_1.TRANSPORT.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VeterinaryEventType(Enum):
    """
    Тип мероприятия.

    Attributes:
        UND: Не определен
        LBR: Лабораторные исследования
        VSE: Ветеринарно-санитарная экспертиза
        IMM: Иммунизация живого животного
        MED: Обработка живого животного
        QRT: Карантин
    """

    UND = "UND"
    LBR = "LBR"
    VSE = "VSE"
    IMM = "IMM"
    MED = "MED"
    QRT = "QRT"

    __descriptions = {
        UND: "Не определен",
        LBR: "Лабораторные исследования",
        VSE: "Ветеринарно-санитарная экспертиза",
        IMM: "Иммунизация живого животного",
        MED: "Обработка живого животного",
        QRT: "Карантин",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VeterinaryEventType.UND.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class StockEntryUuid(BaseModel):
    class Meta:
        name = "stockEntryUuid"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class VetDocumentUuid(BaseModel):
    class Meta:
        name = "vetDocumentUuid"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class AuthorityListInternalType(BaseModel):
    """
    Тип, описывающий список ролей пользователя.
    """

    class Meta:
        name = "AuthorityList"

    model_config = ConfigDict(defer_build=True)
    authority: list[UserAuthority] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class BeactivityLocationsModificationOperationActivityLocation(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    global_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "globalID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "length": 13,
        },
    )
    enterprise: EnterpriseInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class BemodificationOperation(BaseModel):
    """
    Операция внесения изменений в реестр ХС.

    Attributes:
        type_value: Тип операции
        affected_list: Входящие записи для операции.
        resulting_list: Получаемые в результате операции записи.
        reason: Причина изменений записи в реестре ХС.
    """

    class Meta:
        name = "BEModificationOperation"

    model_config = ConfigDict(defer_build=True)
    type_value: RegisterModificationType = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    affected_list: Optional[BusinessEntityListInternalType] = field(
        default=None,
        metadata={
            "name": "affectedList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    resulting_list: Optional[BusinessEntityListInternalType] = field(
        default=None,
        metadata={
            "name": "resultingList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class BatchExtraInfo(BaseModel):
    """
    Дополнительные сведения о партии продукции.

    Attributes:
        non_food_source: Вид проиcхождения для непищевой продукции,
            технического сырья, кормов и кормовых добавок.
    """

    model_config = ConfigDict(defer_build=True)
    non_food_source: Optional[NonFoodProductSourceType] = field(
        default=None,
        metadata={
            "name": "nonFoodSource",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class BatchOrigin(BaseModel):
    """
    Сведения о происхождении партии продукции.

    Attributes:
        product_item: Оригинальное наименование продукции (данное
            производителем).
        country: Страна происхождения продукции.
        producer: Сведения о производителях продукции.
    """

    model_config = ConfigDict(defer_build=True)
    product_item: Optional[ProductItemInternalType] = field(
        default=None,
        metadata={
            "name": "productItem",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    country: Optional[CountryInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    producer: list[ProducerInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class Citizenship(BaseModel):
    """
    Тип, описывающий гражданство.
    """

    model_config = ConfigDict(defer_build=True)
    country: Optional[CountryInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class DiscrepancyReason(GenericEntity):
    """
    Причина несоответствия.

    Attributes:
        name: Название причины.
    """

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )


class Document(GenericEntity):
    """
    Документ.

    Attributes:
        name: Название документа.
        form: Форма документа.
        issue_series: Серия документа.
        issue_number: Номер документа.
        issue_date: Дата документа.
        type_value: Тип документа.
        issuer: Организация, оформившая документ.
        for_value: Опциональная ссылка на связанный элемент. Например,
            ссылка на consignment в запросе.
        qualifier:
    """

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    form: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    issue_series: Optional[str] = field(
        default=None,
        metadata={
            "name": "issueSeries",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    issue_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "issueNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    type_value: Optional[DocumentType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    issuer: Optional[Organization] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    for_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "for",
            "type": "Attribute",
        },
    )
    qualifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 100,
        },
    )


class EntmodificationOperation(BaseModel):
    """
    Операция внесения изменений в реестр предприятий.

    Attributes:
        type_value: Тип операции
        affected_list: Входящие записи для операции.
        resulting_list: Получаемые в результате операции записи.
        reason: Причина изменений записи в реестре предприятий.
    """

    class Meta:
        name = "ENTModificationOperation"

    model_config = ConfigDict(defer_build=True)
    type_value: RegisterModificationType = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    affected_list: Optional[EnterpriseListInternalType] = field(
        default=None,
        metadata={
            "name": "affectedList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    resulting_list: Optional[EnterpriseListInternalType] = field(
        default=None,
        metadata={
            "name": "resultingList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class GoodsDate(BaseModel):
    """С версии 2.0 указание даты строкой (элемент informalDate) в запросах не
    допускается.

    В ответах сервиса дата строкой может присутствовать для старых
    вет.сертификатов/записей складского журнала.
    """

    model_config = ConfigDict(defer_build=True)
    first_date: Optional[ComplexDate] = field(
        default=None,
        metadata={
            "name": "firstDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    second_date: Optional[ComplexDate] = field(
        default=None,
        metadata={
            "name": "secondDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    informal_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "informalDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )


class PslmodificationOperation(BaseModel):
    """
    Операция внесения изменений в реестр наименований продукции производителя.

    Attributes:
        type_value: Тип операции
        affected_list: Входящие записи для операции.
        resulting_list: Получаемые в результате операции записи.
    """

    class Meta:
        name = "PSLModificationOperation"

    model_config = ConfigDict(defer_build=True)
    type_value: RegisterModificationType = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    affected_list: Optional[ProductItemListInternalType] = field(
        default=None,
        metadata={
            "name": "affectedList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    resulting_list: Optional[ProductItemListInternalType] = field(
        default=None,
        metadata={
            "name": "resultingList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class ProcessingProcedure(BaseModel):
    """
    Тип, описывающий производственный процесс.

    Attributes:
        type_value: Тип производственного процесса.
        start_date_time: Дата начала процесса.
        end_date_time: Дата окончания процесса.
    """

    model_config = ConfigDict(defer_build=True)
    type_value: ProcessingProcedureType = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    start_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startDateTime",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    end_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "endDateTime",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class RegionalizationClause(BaseModel):
    """
    Подтверждение соблюдения условия перемещения продукции.

    Attributes:
        condition: Тип соблюдаемого условия перемещения партии.
        text: Текст (точная формулировка) соблюдаемого условия
            перемещения партии.
    """

    model_config = ConfigDict(defer_build=True)
    condition: RegionalizationCondition = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class RouteSectionR13NRules(BaseModel):
    """
    Правила перемещения партии согласно регионализации между двух точек маршрута.

    Attributes:
        sqn_id: Порядовый номер отрезка маршрута.
        applied_r13n_rule: Применяемое правило перемещения для каждой
            категории груза на данном участке маршрута.
    """

    class Meta:
        name = "RouteSectionR13nRules"

    model_config = ConfigDict(defer_build=True)
    sqn_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "sqnId",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    applied_r13n_rule: list[RegionalizationShippingRule] = field(
        default_factory=list,
        metadata={
            "name": "appliedR13nRule",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class TransportInfo(BaseModel):
    """
    Тип, описывающий информацию о транспорте.

    Attributes:
        transport_type: Тип транспортного средства.
        transport_number: Номера т/с.
    """

    model_config = ConfigDict(defer_build=True)
    transport_type: Optional[TransportType] = field(
        default=None,
        metadata={
            "name": "transportType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transport_number: Optional[TransportNumber] = field(
        default=None,
        metadata={
            "name": "transportNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class WorkingArea(BaseModel):
    """
    Тип, описывающий список зон обслуживания.
    """

    model_config = ConfigDict(defer_build=True)
    area: Optional[Area] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    enterprise: Optional[EnterpriseInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class Consignor(BusinessMemberInternalType):
    class Meta:
        name = "consignor"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class DeliveryParticipant(BusinessMemberInternalType):
    class Meta:
        name = "deliveryParticipant"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class IssueDateInterval(DateInterval):
    class Meta:
        name = "issueDateInterval"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class VetDocumentStatus(BaseModel):
    class Meta:
        name = "vetDocumentStatus"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)
    value: VetDocumentStatusInternalType = field(
        metadata={
            "required": True,
        }
    )


class VetDocumentType(BaseModel):
    class Meta:
        name = "vetDocumentType"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)
    value: VetDocumentTypeInternalType = field(
        metadata={
            "required": True,
        }
    )


class BeactivityLocationsModificationOperation(BaseModel):
    """
    Операция изменения связи между хозяйствующим субъектом и предприятиями.

    Attributes:
        type_value: Тип операции
        business_entity: Хозяйствующий субъект.
        activity_location: Список предприятий, для которых должна
            измениться привязка к хозяйствующему субъекту.
    """

    class Meta:
        name = "BEActivityLocationsModificationOperation"

    model_config = ConfigDict(defer_build=True)
    type_value: RegisterModificationType = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    business_entity: BusinessEntityInternalType = field(
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    activity_location: list[
        BeactivityLocationsModificationOperationActivityLocation
    ] = field(
        default_factory=list,
        metadata={
            "name": "activityLocation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "min_occurs": 1,
        },
    )


class Batch(BaseModel):
    """
    Тип, описывающий партию груза.

    Attributes:
        product_type: Тип продукции.
        product: Продукция.
        sub_product: Вид продукции.
        product_item: Наименование продукции согласно номенклатуре
            владельца партии (склада).
        volume: Объём груза.
        unit: Единица измерения объёма груза.
        date_of_production: Дата производства (выработки).
        expiry_date: Дата окончания срока годности.
        batch_id: Уникальный идентификатор производственной партии
            продукции.
        perishable: Скоропортящаяся продукция.
        origin: Сведения о происхождении продукции.
        low_grade_cargo: Является ли продукция некачественной.
        package_list: Описание физической упаковки. Поддерживается
            указание многоуровневой упаковки и маркировки партии
            продукции. См. описание типа vd:Package.
        owner: Собственник продукции.
        applicable_classifications: Дополнительные характеристики
            партии.
    """

    model_config = ConfigDict(defer_build=True)
    product_type: Optional[ProductTypeInternalType] = field(
        default=None,
        metadata={
            "name": "productType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    product: Optional[ProductInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    sub_product: Optional[SubProductInternalType] = field(
        default=None,
        metadata={
            "name": "subProduct",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    product_item: Optional[ProductItemInternalType] = field(
        default=None,
        metadata={
            "name": "productItem",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    volume: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "fraction_digits": 6,
        },
    )
    unit: Optional[UnitInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    date_of_production: Optional[GoodsDate] = field(
        default=None,
        metadata={
            "name": "dateOfProduction",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    expiry_date: Optional[GoodsDate] = field(
        default=None,
        metadata={
            "name": "expiryDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    batch_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "batchID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 100,
        },
    )
    perishable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    origin: Optional[BatchOrigin] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    low_grade_cargo: Optional[bool] = field(
        default=None,
        metadata={
            "name": "lowGradeCargo",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    package_list: Optional[PackageList] = field(
        default=None,
        metadata={
            "name": "packageList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    owner: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    applicable_classifications: Optional[BatchExtraInfo] = field(
        default=None,
        metadata={
            "name": "applicableClassifications",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class DiscrepancyReport(Document):
    """
    Акт о несоответствии.

    Attributes:
        reason: Причина несоответствия.
        description: Детальное описание.
    """

    model_config = ConfigDict(defer_build=True)
    reason: Optional[DiscrepancyReason] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class ReferencedDocumentInternalType(Document):
    """
    Сведения о связанном документе.

    Attributes:
        relationship_type: Тип отношения между документами.
    """

    class Meta:
        name = "ReferencedDocument"

    model_config = ConfigDict(defer_build=True)
    relationship_type: ReferenceType = field(
        metadata={
            "name": "relationshipType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class ShipmentRoutePoint(GenericEntity):
    """
    Сведения о точке маршрута.

    Attributes:
        sqn_id: Порядовый номер точки маршрута.
        location: Название пункта перегрузки.
        enterprise: Название пункта перегрузки.
        transshipment: Признак того, осуществляется ли в данной точке
            перегрузка.
        next_transport: Сведения о дальнейшем транспорте.
    """

    model_config = ConfigDict(defer_build=True)
    sqn_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "sqnId",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    enterprise: Optional[EnterpriseInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transshipment: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    next_transport: Optional[TransportInfo] = field(
        default=None,
        metadata={
            "name": "nextTransport",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class VeterinaryEvent(BaseModel):
    """Некое событие или мероприятие, ассоциированное с партией продукции (или ЖЖ).

    Например, лабораторное исследование, ВСЭ, произведенная обработка
    или иммунизация животного и т.д.

    Attributes:
        id: Идентификатор события в разрезе записи складского журнала
            или вет.сертификата. Не задаётся пользователем в запросах
            (кроме запросов на редактирование), формируется системой
            автоматически.
        name: Наименование мероприятия.
        type_value: Тип мероприятия.
        actual_date_time: Дата события
        location: Место проведения мероприятия
        enterprise: Место проведения мероприятия в случае, если это
            зарегистрированное предприятие
        operator: Организация-оператор, осуществляющий мероприятие.
            Например, лаборатория (в случае лаб.исследований) или СББЖ.
        referenced_document: Связанный документ. Например, акт отбора
            пробы для лаб.исследования.
        notes: Дополнительные сведения.
    """

    model_config = ConfigDict(defer_build=True)
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 100,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    type_value: Optional[VeterinaryEventType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    actual_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "actualDateTime",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    enterprise: Optional[EnterpriseInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    operator: Optional[Organization] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    referenced_document: list[Document] = field(
        default_factory=list,
        metadata={
            "name": "referencedDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    notes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class WorkingAreaList(EntityList):
    """
    Тип, описывающий список зон обслуживания.
    """

    model_config = ConfigDict(defer_build=True)
    working_area: list[WorkingArea] = field(
        default_factory=list,
        metadata={
            "name": "workingArea",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AuthorityList(AuthorityListInternalType):
    class Meta:
        name = "authorityList"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class R13NRouteSection(RouteSectionR13NRules):
    class Meta:
        name = "r13nRouteSection"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalMedicationEvent(VeterinaryEvent):
    """
    Сведения об обработке/иммунизации живого животного.

    Attributes:
        disease: Заболевание
        medicinal_drug: Препарат
        effective_before_date: Срок действия препарата/вакцины.
            Указывается дата и время окончания срока действия.
    """

    model_config = ConfigDict(defer_build=True)
    disease: Optional[AnimalDisease] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    medicinal_drug: Optional[MedicinalDrug] = field(
        default=None,
        metadata={
            "name": "medicinalDrug",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    effective_before_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "effectiveBeforeDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class CertifiedBatch(BaseModel):
    """
    Сертифицированная партия продукции.

    Attributes:
        producer: Сведения о производителе продукции. Участник,
            получивший производственный сертификат, собственник партии.
            Заполняется только для производственного вет.сертификата.
        batch: Сведения о партии продукции.
    """

    model_config = ConfigDict(defer_build=True)
    producer: Optional[BusinessMemberInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    batch: Optional[Batch] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class LaboratoryResearchEvent(VeterinaryEvent):
    """Лабораторное исследование.

    Исследование выполняется на конкретный показатель/заболевание в
    лаборатории.

    Attributes:
        batch_id: Уникальный идентификатор производственной партии
            продукции, для которой проводились лабораторные
            исследования.
        expertise_id: Номер экспертизы
        indicator: Показатель безопасности
        disease: Заболевание
        method: Метод исследования
        result: Результат исследования
        conclusion: Заключение
    """

    model_config = ConfigDict(defer_build=True)
    batch_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "batchID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 100,
        },
    )
    expertise_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "expertiseID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    indicator: Optional[Indicator] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    disease: Optional[AnimalDisease] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    method: Optional[ResearchMethodInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    result: Optional[ResearchResult] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    conclusion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class ProductiveBatch(Batch):
    """Тип, описывающий транспортную партию груза.

    При оформлении незавершенного производства важно: если очередной
    запрос RegisterProductionOperationRequest содержит сведения о
    выработанной продукции с указанным номером партии (Batch/batchID)),
    и ранее в рамках этой же производственной транзакции уже была
    оформлена выработанная продукция с тем же номером партии, то вновь
    выработанный объём продукции будет оприходован на ту же запись
    складского журнала с увеличением её объёма (т.е. будет выполнено
    автоматическое присоединение записей журнала, guid записи журнала
    останется прежним).

    Attributes:
        id: Идентификатор, определяющий batch в запросе. Должен быть
            указан, если запрос содержит несколько элементов batch. Если
            в запросе указано более одной производственной партии, то
            сведения для оформления ВСД (элемент vetDocument) могут
            совпадать для этих производственных партий или отличаться.
            Если сведения совпадаются, то в запросе указывается
            единственный элемент vetDocument, иначе указывается
            несколько, по одному на каждый элемент productiveBatch. При
            этом значение атрибута for элемента vetDocument совпадает со
            значением атрибута id соответствующего элемента
            productiveBatch.
    """

    model_config = ConfigDict(defer_build=True)
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class QuarantineEvent(VeterinaryEvent):
    """
    Карантин животных или продукции.

    Attributes:
        duration: Срок действия карантина. Указывается количество дней
    """

    model_config = ConfigDict(defer_build=True)
    duration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class ShipmentRouteInternalType(BaseModel):
    """
    Тип, описывающий список пунктов перегрузки груза.
    """

    class Meta:
        name = "ShipmentRoute"

    model_config = ConfigDict(defer_build=True)
    route_point: list[ShipmentRoutePoint] = field(
        default_factory=list,
        metadata={
            "name": "routePoint",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class UserInternalType(GenericEntity):
    """
    Тип, описывающий пользователя организации/учреждения.

    Attributes:
        login: Имя пользователя в системе Ветис.
        first_name: Имя пользователя.
        middle_name: Отчество пользователя.
        last_name: Фамилия пользователя.
        fio: ФИО пользователя.
        birth_date: Дата рождения пользователя.
        identity: Документ, удостоверяющий личность.
        citizenship: Гражданство.
        snils: СНИЛС пользователя.
        phone: Личный телефон пользователя.
        work_phone: Рабочий (контактный) телефон пользователя.
        email: Личный адрес электронной почты пользователя.
        work_email: Рабочий адрес электронной почты пользователя.
        organization: Организация пользователя.
        business_entity: Хозяйствующий субъект пользователя.
        post: Должность пользователя в организации (`organization` или
            `businessEntity`).
        enabled: Аккаунт пользователя разрешен/активен.
        non_expired: Аккаунт пользователя не истек (срок действия).
        non_locked: Аккаунт пользователя не заблокирован.
        authority_list: Список ролей пользователя.
        working_area_list: Список зон обслуживания.
    """

    class Meta:
        name = "User"

    model_config = ConfigDict(defer_build=True)
    login: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    middle_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "middleName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    fio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    birth_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "birthDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    identity: Optional[Document] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    citizenship: Optional[Citizenship] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    snils: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "pattern": r"[0-9]{3}-[0-9]{3}-[0-9]{3} [0-9]{2}",
        },
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    work_phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "workPhone",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    work_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "workEmail",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    organization: Optional[Organization] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    business_entity: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    post: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    non_expired: Optional[bool] = field(
        default=None,
        metadata={
            "name": "nonExpired",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    non_locked: Optional[bool] = field(
        default=None,
        metadata={
            "name": "nonLocked",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    authority_list: Optional[AuthorityListInternalType] = field(
        default=None,
        metadata={
            "name": "authorityList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    working_area_list: Optional[WorkingAreaList] = field(
        default=None,
        metadata={
            "name": "workingAreaList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class ReferencedDocument(ReferencedDocumentInternalType):
    class Meta:
        name = "referencedDocument"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class CertifiedConsignment(BaseModel):
    """
    Сертифицированная транспортная партия.

    Attributes:
        consignor: Сведения об отправителе (владельце). Заполняется
            только для транспортного вет.сертификата.
        consignee: Сведения о получателе груза. Заполняется только для
            транспортного вет.сертификата.
        broker: Сведения о фирме-посреднике.
        transport_info: Сведения о транспорте.
        transport_storage_type: Способ хранения при перевозке.
        shipment_route: Сведения о маршруте следования (пунктах
            перегрузки).
        batch: Сведения о партии продукции.
    """

    model_config = ConfigDict(defer_build=True)
    consignor: Optional[BusinessMemberInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    consignee: Optional[BusinessMemberInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    broker: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transport_info: Optional[TransportInfo] = field(
        default=None,
        metadata={
            "name": "transportInfo",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transport_storage_type: Optional[TransportationStorageType] = field(
        default=None,
        metadata={
            "name": "transportStorageType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    shipment_route: Optional[ShipmentRouteInternalType] = field(
        default=None,
        metadata={
            "name": "shipmentRoute",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    batch: Optional[Batch] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class DeliveryInspection(BaseModel):
    """
    Контроль поставки (документарный, ветеринарный)
    """

    model_config = ConfigDict(defer_build=True)
    responsible: Optional[UserInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    result: DeliveryInspectionResult = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    info: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class StockEntryEventListInternalType(BaseModel):
    """
    Список мероприятий с партией продукции.

    Attributes:
        laboratory_research: Сведения о проведенных лабораторных
            исследованиях.
        quarantine: Сведения о карантинировании.
        immunization: Сведения о проведенной обработке/иммунизации
            животных.
        veterinary_event: Сведения о проведенных мероприятиях.
    """

    class Meta:
        name = "StockEntryEventList"

    model_config = ConfigDict(defer_build=True)
    laboratory_research: list[LaboratoryResearchEvent] = field(
        default_factory=list,
        metadata={
            "name": "laboratoryResearch",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    quarantine: list[QuarantineEvent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    immunization: list[AnimalMedicationEvent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    veterinary_event: list[VeterinaryEvent] = field(
        default_factory=list,
        metadata={
            "name": "veterinaryEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class UserListInternalType(EntityList):
    """
    Тип, описывающий список пользователей.
    """

    class Meta:
        name = "UserList"

    model_config = ConfigDict(defer_build=True)
    user: list[UserInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class VetDocumentStatusChange(BaseModel):
    """
    Сведения об изменении статуса ветеринарного документа.

    Attributes:
        status: Установленный статус документа.
        specified_person: Пользователь, изменивший статус ВСД (например,
            подписавший или аннулировавший его).
        actual_date_time: Дата и время изменения статуса ВСД.
        reason: Основание изменения статуса ВСД (например, причина
            аннулирования сертификата).
    """

    model_config = ConfigDict(defer_build=True)
    status: VetDocumentStatusInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    specified_person: UserInternalType = field(
        metadata={
            "name": "specifiedPerson",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    actual_date_time: XmlDateTime = field(
        metadata={
            "name": "actualDateTime",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class VeterinaryAuthentication(BaseModel):
    """Результаты осмотра/исследований партии.

    Заключение ветеринарного врача/специалиста.

    Attributes:
        purpose: Цель. Назначение груза.
        cargo_inspected: Осуществлен контроль гос.ветврачом на
            соответствие требованиям.
        cargo_expertized: Проводилась ли ветсанэкспертиза.
        location_prosperity: Благополучие местности.
        animal_spent_period: Нахождение животных на территории ТС.
        months_spent: Количество месяцев нахождения животных на
            территории ТС.
        laboratory_research: Сведения о проведенных лабораторных
            исследованиях.
        quarantine: Сведения о карантинировании.
        immunization: Сведения о проведенной обработке/иммунизации
            животных.
        veterinary_event: Сведения о проведенных мероприятиях.
        r13n_clause: Подтверждение соблюдаемых условий перемещения
            продукции.
        special_marks: Особые отметки.
    """

    model_config = ConfigDict(defer_build=True)
    purpose: Optional[PurposeInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    cargo_inspected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "cargoInspected",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    cargo_expertized: Optional[ResearchResult] = field(
        default=None,
        metadata={
            "name": "cargoExpertized",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    location_prosperity: Optional[str] = field(
        default=None,
        metadata={
            "name": "locationProsperity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    animal_spent_period: Optional[AnimalSpentPeriod] = field(
        default=None,
        metadata={
            "name": "animalSpentPeriod",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    months_spent: Optional[str] = field(
        default=None,
        metadata={
            "name": "monthsSpent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    laboratory_research: list[LaboratoryResearchEvent] = field(
        default_factory=list,
        metadata={
            "name": "laboratoryResearch",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    quarantine: Optional[QuarantineEvent] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    immunization: list[AnimalMedicationEvent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    veterinary_event: list[VeterinaryEvent] = field(
        default_factory=list,
        metadata={
            "name": "veterinaryEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    r13n_clause: list[RegionalizationClause] = field(
        default_factory=list,
        metadata={
            "name": "r13nClause",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    special_marks: Optional[str] = field(
        default=None,
        metadata={
            "name": "specialMarks",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class Waybill(Document):
    """
    Товарно-транспортная накладная.

    Attributes:
        consignor: Сведения об отправителе (владельце).
        consignee: Сведения о получателе груза.
        broker: Сведения о фирме-посреднике.
        transport_info: Сведения о транспорте.
        transport_storage_type: Способ хранения при перевозке.
        shipment_route: Сведения о маршруте следования (пунктах
            перегрузки).
    """

    model_config = ConfigDict(defer_build=True)
    consignor: Optional[BusinessMemberInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    consignee: Optional[BusinessMemberInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    broker: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transport_info: Optional[TransportInfo] = field(
        default=None,
        metadata={
            "name": "transportInfo",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transport_storage_type: Optional[TransportationStorageType] = field(
        default=None,
        metadata={
            "name": "transportStorageType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    shipment_route: Optional[ShipmentRouteInternalType] = field(
        default=None,
        metadata={
            "name": "shipmentRoute",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class ShipmentRoute(ShipmentRouteInternalType):
    class Meta:
        name = "shipmentRoute"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class User(UserInternalType):
    class Meta:
        name = "user"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class DeliveryFactList(BaseModel):
    """
    Сведения о контроле партии.
    """

    model_config = ConfigDict(defer_build=True)
    vet_certificate_presence: DocumentNature = field(
        metadata={
            "name": "vetCertificatePresence",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    doc_inspection: DeliveryInspection = field(
        metadata={
            "name": "docInspection",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    vet_inspection: DeliveryInspection = field(
        metadata={
            "name": "vetInspection",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    decision: DeliveryDecision = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class VetDocumentInternalType(Document):
    """
    Ветеринарный сопроводительный документ.

    Attributes:
        vet_dform: Форма ВСД.
        vet_dtype: Тип ВСД.
        vet_dstatus: Статус ВСД на момент подписания.
        finalized: Флаг того, что сертификат закрыт. Имеет смысл только
            для производственных сертификатов в статусе "Оформлен"
            (CONFIRMED). В случае незавершенного производства
            оформленный производственный сертификат остаётся незакрытым
            до момента завершения производства (до завершения
            производственной транзакции).
        last_update_date: Дата и время последнего обновления
            сертификата. Дата обновления изменяется при изменении
            статуса сертификата, а также при обновлении объёма
            производственного сертификата в случае незавершенного
            производства.
        certified_batch: Сертифицированная партия. Элемент заполняется
            для производственного сертификата.
        certified_consignment: Сертифицированная партия. Элемент
            заполняется для транспортного сертификата.
        authentication: Результаты осмотра/исследований партии.
            Заключение ветеринарного врача/специалиста.
        preceding_vet_documents: DEPRECATED. Сведения о предыдущих
            ветеринарных сопроводительных документах. Поле не
            используется на запись, вместо него см.referencedDocument.
            Используется для отображения информации о предыдущих
            документах в старых версиях ВСД (или ВСД, оформленных через
            web).
        referenced_document: Сведения о документах, связанных с данным
            сертификатом.
        status_change: Сведения об установлении статуса ветеринарного
            документа.
    """

    class Meta:
        name = "VetDocument"

    model_config = ConfigDict(defer_build=True)
    vet_dform: Optional[VetDocumentForm] = field(
        default=None,
        metadata={
            "name": "vetDForm",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    vet_dtype: Optional[VetDocumentTypeInternalType] = field(
        default=None,
        metadata={
            "name": "vetDType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    vet_dstatus: Optional[VetDocumentStatusInternalType] = field(
        default=None,
        metadata={
            "name": "vetDStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    finalized: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    last_update_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastUpdateDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    certified_batch: Optional[CertifiedBatch] = field(
        default=None,
        metadata={
            "name": "certifiedBatch",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    certified_consignment: Optional[CertifiedConsignment] = field(
        default=None,
        metadata={
            "name": "certifiedConsignment",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    authentication: Optional[VeterinaryAuthentication] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    preceding_vet_documents: Optional[str] = field(
        default=None,
        metadata={
            "name": "precedingVetDocuments",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    referenced_document: list[ReferencedDocumentInternalType] = field(
        default_factory=list,
        metadata={
            "name": "referencedDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    status_change: list[VetDocumentStatusChange] = field(
        default_factory=list,
        metadata={
            "name": "statusChange",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class StockEntryEventList(StockEntryEventListInternalType):
    class Meta:
        name = "stockEntryEventList"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class UserList(UserListInternalType):
    class Meta:
        name = "userList"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class ConsignmentDocumentList(BaseModel):
    """
    Пакет сопроводительных документов.
    """

    model_config = ConfigDict(defer_build=True)
    waybill: Optional[Waybill] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    vet_certificate: list[VetDocumentInternalType] = field(
        default_factory=list,
        metadata={
            "name": "vetCertificate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    related_document: list[ReferencedDocumentInternalType] = field(
        default_factory=list,
        metadata={
            "name": "relatedDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class StockEntryInternalType(GenericVersioningEntity):
    """
    Тип, описывающий cведения о записи журнала продукции.

    Attributes:
        entry_number: Номер записи в складском журнале Меркурия.
        batch: Сведения о партии продукции.
        vet_document: Реквизиты ветеринарного сопроводительного
            документа, сертифицирующего партию.
        vet_event_list: Список мероприятий с партией продукции.
        qualifier:
    """

    class Meta:
        name = "StockEntry"

    model_config = ConfigDict(defer_build=True)
    entry_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "entryNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "pattern": r"\d+",
        },
    )
    batch: Optional[Batch] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    vet_document: list[VetDocumentInternalType] = field(
        default_factory=list,
        metadata={
            "name": "vetDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    vet_event_list: Optional[StockEntryEventListInternalType] = field(
        default=None,
        metadata={
            "name": "vetEventList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    qualifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 100,
        },
    )


class VetDocumentListInternalType(EntityList):
    """
    Тип, описывающий список ВСД.
    """

    class Meta:
        name = "VetDocumentList"

    model_config = ConfigDict(defer_build=True)
    vet_document: list[VetDocumentInternalType] = field(
        default_factory=list,
        metadata={
            "name": "vetDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class VetDocument(VetDocumentInternalType):
    class Meta:
        name = "vetDocument"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class Consignment(Batch):
    """
    Тип, описывающий транспортную партию груза.

    Attributes:
        source_stock_entry: Запись журнала, из которой формируется
            транспортная партия.
        id: Идентификатор, определяющий consignment в запросе. Должен
            быть указан, если запрос содержит несколько элементов
            consignment.
        part_of: Ссылка на consignment в разделе delivery запроса.
            Должен быть указан, если запрос содержит несколько элементов
            consignment.
    """

    model_config = ConfigDict(defer_build=True)
    source_stock_entry: Optional[StockEntryInternalType] = field(
        default=None,
        metadata={
            "name": "sourceStockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    part_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "partOf",
            "type": "Attribute",
        },
    )


class MergeStockEntriesOperation(BaseModel):
    """
    Тип, описывающий производственную операцию.

    Attributes:
        type_value: Тип операции. Поддерживается два типа: MERGE и
            ATTACH. Если элемент не указан, по умолчанию значение
            принимается равным MERGE. В случае присоединения записей
            (ATTACH) главной записью журнала (к которой осуществляется
            присоединение), будет считать первая запись sourceStockEntry
            из списка. В случае присоединения элемент batch не
            указывается, результирующая запись журнала будет иметь то же
            наименование продукции, что и главная. Объём и количество
            упаковок будет просуммировано, виду упаковки, номера партий
            логически объединены в список. Результирующая запись журнала
            продукции будет иметь тот же GUID, что и главная.
        source_stock_entry: Объединяемые записи журнала
        result_stock_entry: Партия, полученная в результате объединения.
    """

    model_config = ConfigDict(defer_build=True)
    type_value: Optional[RegisterModificationType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    source_stock_entry: list[StockEntryInternalType] = field(
        default_factory=list,
        metadata={
            "name": "sourceStockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "min_occurs": 2,
        },
    )
    result_stock_entry: list[StockEntryInternalType] = field(
        default_factory=list,
        metadata={
            "name": "resultStockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class RawBatch(BaseModel):
    """
    Тип, описывающий сырьё для производственной партии.

    Attributes:
        source_stock_entry: Запись журнала, которая используется в
            качестве сырья. Должен быть указан обязательно. В случае,
            если сырьё указывается для незавершенной производственной
            транзакции, следующие поля (volume, unit, packingList,
            packingAmount) могут быть не заполнены до окончательного
            завершения транзакции (см.
            ProductionOperation/finalizeOperation), если отсутствует
            возможность точно определить использованный объём в момент
            выпуска партии продукции. Таким образом, в ещё не закрытом
            производственном сертификате уже будет указано
            использованное сырьё без указания конкретного объёма, т.е.
            реализована прослеживаемость.
        volume: Объём сырья.
        unit: Единица измерения объёма груза.
        package_list: Описание физической упаковки партии продукции.
    """

    model_config = ConfigDict(defer_build=True)
    source_stock_entry: Optional[StockEntryInternalType] = field(
        default=None,
        metadata={
            "name": "sourceStockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    volume: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "fraction_digits": 6,
        },
    )
    unit: Optional[UnitInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    package_list: Optional[PackageList] = field(
        default=None,
        metadata={
            "name": "packageList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class StockEntryListInternalType(EntityList):
    """
    Тип, описывающий список записей журнала.
    """

    class Meta:
        name = "StockEntryList"

    model_config = ConfigDict(defer_build=True)
    stock_entry: list[StockEntryInternalType] = field(
        default_factory=list,
        metadata={
            "name": "stockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class StockEntrySearchPattern(StockEntryInternalType):
    """
    Attributes:
        blank_filter: Фильтр по объёму записи складского журнала.
            Значение по умолчанию -- ALL. См. тип StockEntryBlankFilter.
        receipt_date_interval: Интервал даты поступления партии на склад
            (дата создания первой версии stockEntry).
    """

    model_config = ConfigDict(defer_build=True)
    blank_filter: Optional[StockEntryBlankFilter] = field(
        default=None,
        metadata={
            "name": "blankFilter",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    receipt_date_interval: Optional[DateInterval] = field(
        default=None,
        metadata={
            "name": "receiptDateInterval",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class StockEntry(StockEntryInternalType):
    class Meta:
        name = "stockEntry"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class VetDocumentList(VetDocumentListInternalType):
    class Meta:
        name = "vetDocumentList"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class Delivery(GenericEntity):
    """
    Тип, описывающий поставку.

    Attributes:
        delivery_date:
        consignor: Сведения об отправителе (владельце).
        consignee: Сведения о получателе груза.
        consignment: Сведения о транспортной партии.
        broker: Сведения о фирме-посреднике.
        transport_info: Сведения о транспорте.
        transport_storage_type: Способ хранения при перевозке.
        shipment_route: Сведения о маршруте следования (пунктах
            перегрузки).
        accompanying_forms: Сопроводительные документы.
    """

    model_config = ConfigDict(defer_build=True)
    delivery_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "deliveryDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    consignor: Optional[BusinessMemberInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    consignee: Optional[BusinessMemberInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    consignment: list[Consignment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    broker: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transport_info: Optional[TransportInfo] = field(
        default=None,
        metadata={
            "name": "transportInfo",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transport_storage_type: Optional[TransportationStorageType] = field(
        default=None,
        metadata={
            "name": "transportStorageType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    shipment_route: Optional[ShipmentRouteInternalType] = field(
        default=None,
        metadata={
            "name": "shipmentRoute",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    accompanying_forms: Optional[ConsignmentDocumentList] = field(
        default=None,
        metadata={
            "name": "accompanyingForms",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class ProductionOperation(BaseModel):
    """
    Тип, описывающий производственную операцию.

    Attributes:
        operation_id: Идентификатор производственной транзакции
            (производственная смена, сутки и т.п.). Важно, что в рамках
            одной производственной транзакции всё указанное сырьё будет
            соотнесено со всеми выработанными партиями продукции.
            Сведения о списанном в производство сырье и произведенных
            партиях продукции для транзакции с определенным operationId
            могут быть переданы в нескольких запросах
            RegisterProductiveBatchRequest. Если operationId в запросе
            не указан, то такая транзакция будет завершена автоматически
            по результам выполнения запроса. Т.е. в этом случае формат
            запроса и поведение системы аналогичны версии Ветис API
            v1.3. Важно, внесенные сведения о списанном в производство
            сырье и произведенных партиях продукции невозможно
            отредактировать очередным запросом
            RegisterProductiveBatchRequest с тем же идентификатором
            производственной транзакции. Сведения, указанные в каждом
            следующем запросе будут добавлены к производственной
            транзакции. Запрос будет отклонен, если транзакция с
            указанным в operationId идентификатором завершена.
        raw_batch: Партия сырья.
        productive_batch: Производственная партия.
        finalize_operation: Флаг, который определяет, что по результатам
            выполнения запроса производственная транзакция с
            идентификатором, указанным в элементе operationId, будет
            завершена (finalizeOperation=TRUE). После того, как
            транзакция завершена, внесение сведений о списанном в
            производство сырье и произведенных партиях продукции
            невозможно. Флаг имеет смысл только при наличии элемента
            operationId в запросе, иначе игнорируется. Транзакцию нельзя
            завершить, если для указанного сырья (rawBatch) суммарный
            списанный в производство объём равен нулю. Производственная
            транзакция должна быть завершена по окончанию
            технологического процесса производства. Пока
            производственная транзакция остаётся незавершенной, все
            соответствующие ей производственные сертификаты на
            выработанный объём продукции будут оставаться незакрытыми.
            При завершении производственной транзакции все
            соответствующие ей производственные сертификаты на
            выработанный объём продукции автоматически закрываются.
        applied_process: Технологический процесс/операция. В случае
            отсутствия элемента `appliedProcess` по умолчанию
            принимается, что в процессе производственной операции
            происходит (в скобках указано значение элемента
            `appliedProcess/type`): 1. Производство (37) - если в
            операции присутствует сырьё (`rawBatch`) и выработанная
            продукция (`productiveBatch`). 2. Убой (12) + Производство
            (37) - если в операции присутствует в качестве сырья живое
            животное (по значению `productType`), а в качестве
            выработанной партии - продукция 3. Добыча (35) - если сырьё
            не используется, а в качестве выработанной партии - живое
            животное. Например, для вылова рыбы. 4. Добыча (35) +
            Производство (37) - если сырьё не используется, а в качестве
            выработанной партии - продукция. 5. Утилизация (101) - если
            сырьё присутствует в операции, а выработанной партии нет.
    """

    model_config = ConfigDict(defer_build=True)
    operation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "operationId",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 100,
        },
    )
    raw_batch: list[RawBatch] = field(
        default_factory=list,
        metadata={
            "name": "rawBatch",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    productive_batch: list[ProductiveBatch] = field(
        default_factory=list,
        metadata={
            "name": "productiveBatch",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    finalize_operation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "finalizeOperation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    applied_process: list[ProcessingProcedure] = field(
        default_factory=list,
        metadata={
            "name": "appliedProcess",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class StockDiscrepancy(BaseModel):
    """
    Операция внесения изменений в реестр предприятий.

    Attributes:
        affected_list: Входящие записи для операции. Deprecated.
        resulting_list: Получаемые в результате операции записи.
        reason: Причина несоответствия.
        id: Идентификатор, определяющий stockDiscrepancy в запросе.
            Должен быть указан, если запрос содержит несколько элементов
            stockDiscrepancy.
    """

    model_config = ConfigDict(defer_build=True)
    affected_list: Optional[StockEntryListInternalType] = field(
        default=None,
        metadata={
            "name": "affectedList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    resulting_list: Optional[StockEntryListInternalType] = field(
        default=None,
        metadata={
            "name": "resultingList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class StockEntryList(StockEntryListInternalType):
    class Meta:
        name = "stockEntryList"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)
