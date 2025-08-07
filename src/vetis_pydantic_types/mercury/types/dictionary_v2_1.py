from __future__ import annotations

from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict

from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.mercury.types.base_v2_0 import (
    EntityList,
    GenericEntity,
    GenericVersioningEntity,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/dictionary/v2"


class BusinessEntityType(Enum):
    """
    Тип, описывающий тип ХС.

    Attributes:
        VALUE_1: JURIDICAL - юридическое лицо.
        VALUE_2: PHYSICAL - физическое лицо.
        VALUE_3: SELF_EMPLOYED - индивидуальный предприниматель.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

    __descriptions = {
        VALUE_1: "JURIDICAL - юридическое лицо.",
        VALUE_2: "PHYSICAL - физическое лицо.",
        VALUE_3: "SELF_EMPLOYED - индивидуальный предприниматель.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        BusinessEntityType.VALUE_1.verbose_name
        """

        return type(self).__descriptions.get(self.value)


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
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "pattern": r"[1-2][0-9][0-9][0-9]",
        },
    )
    month: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "min_inclusive": 1,
            "max_inclusive": 12,
        },
    )
    day: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "min_inclusive": 1,
            "max_inclusive": 31,
        },
    )
    hour: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "min_inclusive": 0,
            "max_inclusive": 23,
        },
    )
    minute: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "min_inclusive": 0,
            "max_inclusive": 59,
        },
    )


class DocumentNature(Enum):
    """
    Природа (тип) документа.

    Attributes:
        ELECTRONIC: Электронный документ
        PAPER: Бумажный документ
    """

    ELECTRONIC = "ELECTRONIC"
    PAPER = "PAPER"

    __descriptions = {
        ELECTRONIC: "Электронный документ",
        PAPER: "Бумажный документ",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        DocumentNature.ELECTRONIC.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class DocumentType(Enum):
    """
    Тип документа.

    Attributes:
        VALUE_1: Товарно-транспортная накладная
        VALUE_2: Конасамент
        VALUE_3: CMR
        VALUE_4: Авианакладная
        VALUE_5: Транспортная накладная
        VALUE_6: ТОРГ-12
        VALUE_7: Ветеринарное разрешение на импорт продукции на
            территорию ТС.
        VALUE_8: Разрешение ветеринарного управления субъекта РФ на ввоз
            продукции на территорию субъекта.
        VALUE_9: Акт отбора пробы на исследование.
        VALUE_10: ТОРГ-13
        VALUE_11: Ветеринарный сертификат на перемещение внутри РФ
        VALUE_12: Ветеринарный сертификат третьих стран на ввоз
            продукции на территорию РФ
        VALUE_13: Ветеринарный сертификат страны ТС на ввоз продукции на
            территорию РФ
        VALUE_14: Ветеринарный сертификат РФ на вывоз продукции на
            территорию стран ТС
        VALUE_15: Ветеринарный сертификат РФ на вывоз продукции на
            территорию третьих стран
        VALUE_16: Заказ
        VALUE_17: Паспорт РФ
        VALUE_18: Паспорт иностранного гражданина
        VALUE_19: Паспорт гражданина Республики Казахстан
        VALUE_20: Паспорт гражданина Республики Беларусь
        VALUE_21: Паспорт гражданина Республики Армения
        VALUE_22: Паспорт гражданина Республики Киргизия
        VALUE_23: Универсальный передаточный документ (УПД)
        VALUE_24: Электронный ветеринарный производственный сертификат
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24

    __descriptions = {
        VALUE_1: "Товарно-транспортная накладная",
        VALUE_2: "Конасамент",
        VALUE_3: "CMR",
        VALUE_4: "Авианакладная",
        VALUE_5: "Транспортная накладная",
        VALUE_6: "ТОРГ-12",
        VALUE_7: "Ветеринарное разрешение на импорт продукции на территорию ТС.",
        VALUE_8: (
            "Разрешение ветеринарного управления субъекта РФ на ввоз продукции на "
            "территорию субъекта."
        ),
        VALUE_9: "Акт отбора пробы на исследование.",
        VALUE_10: "ТОРГ-13",
        VALUE_11: "Ветеринарный сертификат на перемещение внутри РФ",
        VALUE_12: "Ветеринарный сертификат третьих стран на ввоз продукции на территорию РФ",
        VALUE_13: "Ветеринарный сертификат страны ТС на ввоз продукции на территорию РФ",
        VALUE_14: "Ветеринарный сертификат РФ на вывоз продукции на территорию стран ТС",
        VALUE_15: "Ветеринарный сертификат РФ на вывоз продукции на территорию третьих стран",
        VALUE_16: "Заказ",
        VALUE_17: "Паспорт РФ",
        VALUE_18: "Паспорт иностранного гражданина",
        VALUE_19: "Паспорт гражданина Республики Казахстан",
        VALUE_20: "Паспорт гражданина Республики Беларусь",
        VALUE_21: "Паспорт гражданина Республики Армения",
        VALUE_22: "Паспорт гражданина Республики Киргизия",
        VALUE_23: "Универсальный передаточный документ (УПД)",
        VALUE_24: "Электронный ветеринарный производственный сертификат",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        DocumentType.VALUE_1.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class EnterpriseGroupInternalType(Enum):
    """
    Тип, описывающий параметра запроса зарубежных пердприятий.

    Attributes:
        VALUE_0: ALL - все предприятия.
        VALUE_1: LICENSED - аттестованные предприятия.
        VALUE_2: NOTLICENSED - неаттестованные предприятия.
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

    __descriptions = {
        VALUE_0: "ALL - все предприятия.",
        VALUE_1: "LICENSED - аттестованные предприятия.",
        VALUE_2: "NOTLICENSED - неаттестованные предприятия.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        EnterpriseGroup_1.VALUE_0.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class EnterpriseNumberList(BaseModel):
    """
    Тип, описывающий список номеров предприятий.
    """

    model_config = ConfigDict(defer_build=True)
    enterprise_number: list[str] = field(
        default_factory=list,
        metadata={
            "name": "enterpriseNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )


class EnterpriseRole(Enum):
    """
    Тип, описывающий роль пердприятия.

    Attributes:
        UNKNOWN: Роль не определена.
        PRODUCER: Является производителем продукции (в том числе
            выращивание).
        SLAUGHTER_HOUSE: Бойня (мясокомбинат).
        CUTTING_PLANT: Разделочное предприятие.
        COLD_STORE: Холодильник.
        PACKAGING_PLANT: Упаковочное предприятие.
    """

    UNKNOWN = "UNKNOWN"
    PRODUCER = "PRODUCER"
    SLAUGHTER_HOUSE = "SLAUGHTER_HOUSE"
    CUTTING_PLANT = "CUTTING_PLANT"
    COLD_STORE = "COLD_STORE"
    PACKAGING_PLANT = "PACKAGING_PLANT"

    __descriptions = {
        UNKNOWN: "Роль не определена.",
        PRODUCER: "Является производителем продукции (в том числе выращивание).",
        SLAUGHTER_HOUSE: "Бойня (мясокомбинат).",
        CUTTING_PLANT: "Разделочное предприятие.",
        COLD_STORE: "Холодильник.",
        PACKAGING_PLANT: "Упаковочное предприятие.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        EnterpriseRole.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class EnterpriseStatus(Enum):
    """
    Тип, описывающий статус предприятия в реестре.

    Attributes:
        UNVERIFIED: Не подтверджен (не в реестре).
        VERIFIED: Подтвержден (включен в реестр).
        CANCELED: Исключен из реестра.
        DELETED: Удален.
    """

    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    CANCELED = "CANCELED"
    DELETED = "DELETED"

    __descriptions = {
        UNVERIFIED: "Не подтверджен (не в реестре).",
        VERIFIED: "Подтвержден (включен в реестр).",
        CANCELED: "Исключен из реестра.",
        DELETED: "Удален.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        EnterpriseStatus.UNVERIFIED.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class PackageLevelType(Enum):
    """
    Тип, описывающий уровень упаковки.

    Attributes:
        VALUE_1: Внутренний уровень Уровень, при котором упаковка
            отсутствует, но тем не менее есть необходимость наносить
            маркировку. Например, яйцо, шкуры, мясо, сыр. Явно
            указывается, что упаковка отсутствует.
        VALUE_2: Потребительский уровень Товар в упаковке для розничной
            торговли, маркированный штриховым кодом для сканирования на
            кассе.
        VALUE_3: Промежуточный уровень Уровень упаковки, если он
            существует, который находится между потребительским и
            торговым уровнем.
        VALUE_4: Торговый уровень Товар в упаковке, предназначенной для
            заказа, оплаты и доставки. Это согласованный между
            ритейлером и изготовителем (или другим участником) уровень
            упаковки товара, в котором товар заказывается, оплачивается
            и доставляется.
        VALUE_5: Дополнительный уровень Товар в упаковке, которую нельзя
            однозначно отнести к торговому или транспортному уровню.
        VALUE_6: Транспортный (Логистический) уровень Товар в упаковке,
            предназначенной для отгрузки покупателю (ритейлеру) при
            выполнении заказа.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

    __descriptions = {
        VALUE_1: (
            "Внутренний уровень\nУровень, при котором упаковка отсутствует, но тем не "
            "менее есть необходимость наносить маркировку.\nНапример, яйцо, шкуры, "
            "мясо, сыр. Явно указывается, что упаковка отсутствует."
        ),
        VALUE_2: (
            "Потребительский уровень\nТовар в упаковке для розничной торговли, "
            "маркированный штриховым кодом для сканирования на кассе."
        ),
        VALUE_3: (
            "Промежуточный уровень\nУровень упаковки, если он существует, который "
            "находится между потребительским и торговым уровнем."
        ),
        VALUE_4: (
            "Торговый уровень\nТовар в упаковке, предназначенной для заказа, оплаты и "
            "доставки.\nЭто согласованный между ритейлером и изготовителем (или другим"
            " участником) уровень упаковки товара,\nв котором товар заказывается, "
            "оплачивается и доставляется."
        ),
        VALUE_5: (
            "Дополнительный уровень\nТовар в упаковке, которую нельзя однозначно "
            "отнести к торговому или транспортному уровню."
        ),
        VALUE_6: (
            "Транспортный (Логистический) уровень\nТовар в упаковке, предназначенной "
            "для отгрузки покупателю (ритейлеру) при выполнении заказа."
        ),
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        PackageLevelType.VALUE_1.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class PackingCodeType(Enum):
    """Тип для представления Packing Code в соответствии с
    "ЕК 013-2010 (ред.1) - Классификатор видов груза, упаковки и упаковочных материалов".
    См. https://eomi.eaeunion.org/ru/#/repository/nsi/173

    Attributes:
        VALUE_1_A: Барабан стальной Drum, steel
        VALUE_1_B: Барабан, алюминиевый Drum, aluminium
        VALUE_1_D: Барабан фанерный Drum, plywood
        VALUE_1_F: Контейнер, гибкий Container, flexible
        VALUE_1_G: Барабан фибровый Drum, fibre
        VALUE_1_W: Барабан, деревянный Drum, wooden
        VALUE_2_C: Бочка (емкостью около 164 л) деревянная Barrel,
            wooden
        VALUE_3_A: Канистра, стальная Jerrycan, steel
        VALUE_3_H: Канистра, пластмассовая Jerrycan, plastic
        VALUE_43: Мешок большой для крупноразмерных навалочных грузов
            Bag, super bulk
        VALUE_44: Мешок полиэтиленовый Bag, polybag
        VALUE_4_A: Коробка, стальная Box, steel
        VALUE_4_B: Коробка, алюминиевая Box, aluminium
        VALUE_4_C: Коробка из естественной древесины Box, natural wood
        VALUE_4_D: Коробка, фанерная Box, plywood
        VALUE_4_F: Коробка из древесного материала Box, reconstituted
            wood
        VALUE_4_G: Коробка из фибрового картона Box, fibreboard
        VALUE_4_H: Коробка, пластмассовая Box, plastic
        VALUE_5_H: Мешок из полимерной ткани Bag, woven plastic
        VALUE_5_L: Мешок текстильный Bag, textile
        VALUE_5_M: Мешок, бумажный Bag, paper
        VALUE_6_H: Комбинированная упаковка: пластмассовый сосуд
            Composite packaging, plastic receptacle
        VALUE_6_P: Комбинированная упаковка: стеклянный сосуд Composite
            packaging, glass receptacle
        VALUE_7_A: Ящик автомобильный Case, car
        VALUE_7_B: Ящик деревянный Case, wooden
        VALUE_8_A: Поддон деревянный Pallet, wooden
        VALUE_8_B: Ящик деревянный Crate, wooden
        VALUE_8_C: Пачка деревянная Bundle, wooden
        AA: Контейнер средней грузоподъемности для массовых грузов из
            жесткой пластмассы Intermediate bulk container, rigid
            plastic
        AB: Сосуд, фибровый Receptacle, fibre
        AC: Сосуд, бумажный Receptacle, paper
        AD: Сосуд, деревянный Receptacle, wooden
        AE: Аэрозольная упаковка Aerosol
        AF: Поддон модульный с обечайкой 80 x 60 см Pallet, modular,
            collars 80 cm x 60 cm
        AG: Поддон в термоусадочной пленке Pallet, shrink-wrapped
        AH: Поддон 100 x 110 см Pallet, 100 cm x 110 cm
        AI: Грейферный ковш Clamshell
        AJ: Кулек Cone
        AL: Шар Ball
        AM: Ампула, незащищенная Ampoule, non-protected
        AP: Ампула, защищенная Ampoule, protected
        AT: Пульверизатор Atomizer
        AV: Капсула Capsule
        B4: Лента Belt
        BA: Бочка (емкостью около 164 л) Barrel
        BB: Бобина Bobbin
        BC: Ящик решетчатый для бутылок Bottlecrate/bottlerack
        BD: Доска Board
        BE: Пакет (пачка/связка) Bundle
        BF: Баллон, незащищенный Balloon, non-protected
        BG: Мешок Bag
        BH: Пачка (пакет/связка) Bunch
        BI: Бункер Bin
        BJ: Бадья Bucket
        BK: Корзина Basket
        BL: Кипа, спрессованная Bale, compressed
        BM: Чан Basin
        BN: Кипа, неспрессованная Bale, non-compressed
        BO: Бутылка цилиндрическая незащищенная Bottle, non-protected,
            cylindrical
        BP: Баллон, защищенный Balloon, protected
        BQ: Бутылка цилиндрическая защищенная Bottle, protected
            cylindrical
        BR: Брус (брусок) Bar
        BS: Бутылка с выпуклыми стенками незащищенная Bottle, non-
            protected, bulbous
        BT: Рулон (обивочного или настилочного материала) Bolt
        BU: Бочка для вина или пива Butt
        BV: Бутылка с выпуклыми стенками защищенная Bottle, protected
            bulbous
        BW: Коробка для жидкостей Box, for liquids
        BX: Коробка Box
        BY: Доска в пакете/пачке/связке Board, in bundle/bunch/truss
        BZ: Брус (брусок) в пакете/пачке/связке Bars, in
            bundle/bunch/truss
        CA: Банка (емкостью менее 5 л) жестяная прямоугольная Can,
            rectangular
        CB: Ящик решетчатый для пива Crate, beer
        CC: Бидон Churn
        CD: Банка (емкостью менее 5 л) жестяная с ручкой и выпускным
            отверстием Can, with handle and spout
        CE: Корзина, рыбацкая Creel
        CF: Кофр Coffer
        CG: Клеть Cage
        CH: Сундук Chest
        CI: Банка жестяная для сухих продуктов (массой до 2,2 кг)
            Canister
        CJ: Гроб Coffin
        CK: Бочка Cask
        CL: Бухта Coil
        CM: Кардная лента Card
        CN: Контейнер, прочее транспортировочное оборудование, кроме
            поименованного Container, not otherwise specified as
            transport equipment
        CO: Бутыль оплетенная незащищенная Carboy, non-protected
        CP: Бутыль оплетенная защищенная Carboy, protected
        CQ: Кассета Cartridge
        CR: Ящик, решетчатый (или обрешетка) Crate
        CS: Ящик Case
        CT: Коробка, картонная Carton
        CU: Чаша Cup
        CV: Чехол Cover
        CW: Клеть, роликовая Cage, roll
        CX: Банка (емкостью менее 5 л) жестяная цилиндрическая Can,
            cylindrical
        CY: Цилиндр Cylinder
        CZ: Брезент Canvas
        DA: Ящик решетчатый (или обрешетка) многослойный пластмассовый
            Crate, multiple layer, plastic
        DB: Ящик решетчатый (или обрешетка) многослойный деревянный
            Crate, multiple layer, wooden
        DC: Ящик решетчатый (или обрешетка) многослойный картонный
            Crate, multiple layer, cardboard
        DG: Клеть (многооборотная) Общего фонда транспортировочного
            оборудования EC Cage, Commonwealth Handling Equipment Pool
            (CHEP)
        DH: Коробка (многооборотная) из Общего фонда транспортировочного
            оборудования ЕС, Еврокоробка Box, Commonwealth Handling
            Equipment Pool (CHEP), Eurobox
        DI: Барабан, железный Drum, iron
        DJ: Бутыль оплетенная большая (емкостью от 9 до 54 л)
            незащищенная Demijohn, non-protected
        DK: Ящик решетчатый для массовых грузов картонный Crate, bulk,
            cardboard
        DL: Ящик решетчатый для массовых грузов пластмассовый Crate,
            bulk, plastic
        DM: Ящик решетчатый для массовых грузов деревянный Crate, bulk,
            wooden
        DN: Дозатор Dispenser
        DP: Бутыль оплетенная большая (емкостью от 9 до 54 л) защищенная
            Demijohn, protected
        DR: Барабан Drum
        DS: Лоток с одним настилом без покрытия пластмассовый Tray, one
            layer no cover, plastic
        DT: Лоток с одним настилом без покрытия деревянный Tray, one
            layer no cover, wooden
        DU: Лоток с одним настилом без покрытия полистироловый Tray, one
            layer no cover, polystyrene
        DV: Лоток с одним настилом без покрытия картонный Tray, one
            layer no cover, cardboard
        DW: Лоток с двумя настилами без покрытия пластмассовый Tray, two
            layers no cover, plastic tray
        DX: Лоток с двумя настилами без покрытия деревянный Tray, two
            layers no cover, wooden
        DY: Лоток с двумя настилами без покрытия картонный Tray, two
            layers no cover, cardboard
        EC: Мешок, пластмассовый Bag, plastic
        ED: Ящик с поддоном Case, with pallet base
        EE: Ящик с поддоном деревянный Case, with pallet base, wooden
        EF: Ящик с поддоном картонный Case, with pallet base, cardboard
        EG: Ящик с поддоном пластмассовый Case, with pallet base,
            plastic
        EH: Ящик с поддоном металлический Case, with pallet base, metal
        EI: Ящик, изотермический Case, isothermic
        EN: Конверт Envelope
        FC: Ящик решетчатый для фруктов Crate, fruit
        FD: Ящик решетчатый (или обрешетка) рамный Crate, framed
        FE: Мягкий мешок, Гибкая цистерна Flexitank, Flexibag
        FI: Бочонок (емкостью около 41 л) Firkin
        FL: Фляга Flask
        FO: Сундучок Footlocker
        FP: Кассета с пленкой (фильмпак) Filmpack
        FR: Рама Frame
        FT: Контейнер для пищевых продуктов Foodtainer
        FX: Мешок, гибкий контейнер Bag, flexible container
        GB: Баллон, газовый Bottle, gas
        GI: Балка Girder
        GL: Контейнер, галлон Container, gallon
        GR: Сосуд, стеклянный Receptacle, glass
        GY: Мешок из мешковины Bag, gunny
        GZ: Балка в пакете/пачке/связке Girders, in bundle/bunch/truss
        HA: Корзина с ручкой, пластмассовая Basket, with handle, plastic
        HB: Корзина с ручкой из древесины Basket, with handle, wooden
        HC: Корзина с ручкой, картонная Basket, with handle, cardboard
        HG: Бочка емкостью 238 л (хогсхед) Hogshead
        HN: Крюк Hanger
        HR: Корзина с крышкой Hamper
        IA: Упаковка демонстрационная деревянная Package, display,
            wooden
        IB: Упаковка демонстрационная картонная Package, display,
            cardboard
        IC: Упаковка демонстрационная пластмассовая Package, display,
            plastic
        ID: Упаковка демонстрационная металлическая Package, display,
            metal
        IE: Упаковка, выставочная Package, show
        IF: Упаковка, выпрессованная Package, flow
        IG: Упаковка в оберточной бумаге Package, paper wrapped
        IH: Барабан, пластмассовый Drum, plastic
        IK: Упаковка картонная с отверстиями для бутылок Package,
            cardboard, with bottle grip-holes
        IN: Слиток Ingot
        IZ: Слитки в пакете/пачке/связке Ingots, in bundle/bunch/truss
        JB: Мешок большой, Bag, jumbo
        JC: Канистра, прямоугольная Jerrican, rectangular
        JG: Кувшин, маленький Jug
        JR: Банка широкогорлая (емкостью около 4,5 литров) Jar
        JT: Мешок, джутовый Jute bag
        JY: Канистра, цилиндрическая Jerrican, cylindrical
        KG: Бочонок (емкостью около 46 л) Keg
        KI: Набор Kit
        LE: Багаж Luggage
        LG: Бревно Log
        LT: Грузовая партия (лот) Lot
        LU: Ящик Lug
        LV: Короб деревянный (лифтван) размером около 220 см (длина) x
            115 см (ширина) x 220 см (высота) Liftvan
        LZ: Бревно в пакете/пачке/связке Logs, in bundle/bunch/truss
        MA: Ящик металлический Crate, metal
        MB: Пакет бумажный многослойный Bag, multiply
        MC: Ящик решетчатый для молока Crate, milk
        ME: Контейнер металлический Container, metal
        MR: Сосуд, металлический Receptacle, metal
        MS: Мешок (куль) многослойный Sack, multi-wall
        MT: Мешок, рогожный Mat
        MW: Сосуд с пластмассовым покрытием Receptacle, plastic wrapped
        MX: Спичечный коробок Matchbox
        NA: Нет сведений Not available
        NE: Неупакованный или нерасфасованный Unpacked or unpackaged
        NF: Неупакованный или нерасфасованный одноместный груз Unpacked
            or unpackaged, single unit
        NG: Неупакованный или нерасфасованный многоместный груз Unpacked
            or unpackaged, multiple units
        NS: Гнездо (ячейка) Nest
        NT: Сетка Net
        NU: Сетка трубчатая пластмассовая Net, tube, plastic
        NV: Сетка трубчатая текстильная Net, tube, textile
        OT: Октабин Octabin
        OU: Контейнер наружный Container, outer
        P2: Лоток Pan
        PA: Пакет Packet
        PB: Поддон, ящичный Pallet, box
        PC: Бандероль Parcel
        PD: Поддон модульный с обечайкой 80 x 100 см Pallet, modular,
            collars 80 cm x 100 cm
        PE: Поддон модульный с обечайкой 80 х 120 см Pallet, modular,
            collars 80 cm x 120 cm
        PF: Штабель Pen
        PG: Плита Plate
        PH: Кувшин, большой Pitcher
        PI: Труба Pipe
        PJ: Корзина из шпона для ягод и фруктов Punnet
        PK: Упаковка Package
        PL: Ведро Pail
        PN: Доска, толстая Plank
        PO: Пакет (мешочек) Pouch
        PP: Штука Piece
        PR: Сосуд, пластмассовый Receptacle, plastic
        PT: Горшок Pot
        PU: Лоток Tray
        PV: Труба в пакете/пачке/связке Pipes, in bundle/bunch/truss
        PX: Поддон Pallet
        PY: Плиты в пакете/пачке/связке Plates, in bundle/bunch/truss
        PZ: Доска толстая в пакете/пачке/связке Planks, in
            bundle/bunch/truss
        QA: Барабан стальной с несъемным днищем Drum, steel, non -
            removable head
        QB: Барабан стальной со съемным днищем Drum, steel, removable
            head
        QC: Барабан алюминиевый с несъемным днищем Drum, aluminium, non-
            removable head
        QD: Барабан алюминиевый со съемным днищем Drum, aluminium,
            removable head
        QF: Барабан пластмассовый с несъемным днищем Drum, plastic, non-
            removable head
        QG: Барабан пластмассовый со съемным днищем Drum, plastic,
            removable head
        QH: Бочка (емкостью около 164 л) деревянная шпунтованная Barrel,
            wooden, bung type
        QJ: Бочка (емкостью около 164 л) деревянная со съемным днищем
            Barrel, wooden, removable head
        QK: Канистра стальная с несъемным днищем Jerrican, steel, non-
            removable head
        QL: Канистра стальная со съемным днищем Jerrican, steel,
            removable head
        QM: Канистра пластмассовая с несъемным днищем Jerrican, plastic,
            non-removable head
        QN: Канистра пластмассовая со съемным днищем Jerrican, plastic,
            removable head
        QP: Коробка деревянная из естественной древесины обыкновенная
            Box, wooden, natural wood, ordinary
        QQ: Коробка деревянная из естественной древесины с плотно
            пригнанными стенками Box, wooden, natural wood, with sift
            proof walls
        QR: Коробка, пенопластовая Box, plastic, expanded
        QS: Коробка из твердой пластмассы Box, plastic, solid
        RD: Прут Rod
        RG: Кольцо Ring
        RJ: Стойка, вешалка для одежды Rack, clothing hanger
        RK: Стойка Rack
        RL: Катушка Reel
        RO: Рулон (полосового материала) Roll
        RT: Сетка типа используемой для овощей или фруктов Rednet
        RZ: Прут в пакете/пачке/связке Rods, in bundle/bunch/truss
        SA: Мешок (куль) Sack
        SB: Сляб Slab
        SC: Ящик решетчатый (или обрешетка) мелкий Crate, shallow
        SD: Шпиндель Spindle
        SE: Сундук, морской Sea-chest
        SH: Пакетик Sachet
        SI: Стеллаж Skid
        SK: Ящик, каркасный Case, skeleton
        SL: Лист, прокладной Slipsheet
        SM: Лист, металлический Sheet metal
        SO: Шпулька Spool
        SP: Лист с пластмассовым покрытием Sheet, plastic wrapping
        SS: Ящик, стальной Case, steel
        ST: Лист Sheet
        SU: Чемодан Suitcase
        SV: Конверт, стальной Envelope, steel
        SW: В термоусадочной пленке Shrink-wrapped
        SX: Комплект Set
        SY: Гильза Sleeve
        SZ: Лист в пакете/пачке/связке Sheets, in bundle/bunch/truss
        T1: Таблетка Tablet
        TB: Кадка Tub
        TC: Чайная коробка Tea-chest
        TD: Трубка или туба, складывающаяся Tube, collapsible
        TE: Шина Tyre
        TG: Цистерна контейнер универсальный Tank container, generic
        TI: Бочка деревянная (емкостью около 200 л) Tierce
        TK: Цистерна, прямоугольная Tank, rectangular
        TL: Кадка с крышкой Tub, with lid
        TN: Банка, жестяная (консервная) Tin
        TO: Бочка для вина или пива большая (емкостью около 1146 л)
            (тан) Tun
        TR: Сундук, дорожный Trunk
        TS: Связка Truss
        TT: Мешок Bag, tote
        TU: Трубка или туба Tube
        TV: Трубка или туба с насадкой Tube, with nozzle
        TW: Поддон Pallet, triwall
        TY: Цистерна, цилиндрическая Tank, cylindrical
        TZ: Трубка или туба в пакете/пачке/связке Tubes, in
            bundle/bunch/truss
        UC: Без клети Uncaged
        UN: Единица Unit
        VA: Бак Vat
        VG: Наливом газ (при 1031 мБар и 15°C) Bulk, gas (at 1 031 mbar
            and 15° C)
        VI: Флакон Vial
        VK: Консоль для оборудования, помещающаяся в минифургон Vanpack
        VL: Наливом жидкость Bulk, liquid
        VO: Насыпью твердые крупные частицы (мелкие куски) Bulk, solid,
            large particles (nodules)
        VP: В вакуумной упаковке Vacuum-packed
        VQ: Наливом газ сжиженный (при температуре/давлении,
            отличающихся от нормальных) Bulk, liquefied gas (at abnormal
            temperature/pressure)
        VR: Насыпью твердые гранулированные частицы (гранулы) Bulk,
            solid, granular particles (grains)
        VS: Навалом металлолом Bulk, scrap metal
        VY: Насыпью твердые мелкие частицы (порошки) Bulk, solid, fine
            particles (powders)
        WA: Контейнер средней грузоподъемности для массовых грузов
            Intermediate bulk container
        WB: Бутылка оплетенная Wicker bottle
        WC: Контейнер средней грузоподъемности для массовых грузов
            стальной Intermediate bulk container, steel
        WD: Контейнер средней грузоподъемности для массовых грузов
            алюминиевый Intermediate bulk container, aluminium
        WF: Контейнер средней грузоподъемности для массовых грузов
            металлический Intermediate bulk container, metal
        WG: Контейнер средней грузоподъемности для массовых грузов
            герметизированный свыше 10 КПа Intermediate bulk container,
            steel, pressurised &gt; 10 kpa
        WH: Контейнер средней грузоподъемности для массовых грузов
            алюминиевый герметизированный свыше 10 КПа Intermediate bulk
            container, aluminium, pressurised &gt; 10 kpa
        WJ: Контейнер средней грузоподъемности для массовых грузов
            герметизированный 10 Кпа Intermediate bulk container, metal,
            pressure 10 kpa
        WK: Контейнер средней грузоподъемности для наливных грузов
            стальной Intermediate bulk container, steel, liquid
        WL: Контейнер средней грузоподъемности для наливных грузов
            алюминиевый Intermediate bulk container, aluminium, liquid
        WM: Контейнер средней грузоподъемности для наливных грузов
            металлический Intermediate bulk container, metal, liquid
        WN: Контейнер средней грузоподъемности для массовых грузов из
            полимерной ткани без покрытия/вкладыша Intermediate bulk
            container, woven plastic, without coat/liner
        WP: Контейнер средней грузоподъемности для массовых грузов из
            полимерной ткани с покрытием Intermediate bulk container,
            woven plastic, coated
        WQ: Контейнер средней грузоподъемности для массовых грузов из
            полимерной ткани с вкладышем Intermediate bulk container,
            woven plastic, with liner
        WR: Контейнер средней грузоподъемности для массовых грузов из
            пластикового волокна с покрытием и вкладышем Intermediate
            bulk container, woven plastic, coated and liner
        WS: Контейнер средней грузоподъемности для массовых грузов из
            полимерной пленки Intermediate bulk container, plastic film
        WT: Контейнер средней грузоподъемности для массовых грузов
            текстильный без покрытия/вкладыша Intermediate bulk
            container, textile without coat/liner
        WU: Контейнер средней грузоподъемности для массовых грузов из
            естественной древесины с внутренним вкладышем Intermediate
            bulk container, natural wood, with inner liner
        WV: Контейнер средней грузоподъемности для массовых грузов
            текстильный с покрытием Intermediate bulk container,
            textile, coated
        WW: Контейнер средней грузоподъемности для массовых грузов
            текстильный с вкладышем Intermediate bulk container,
            textile, with liner
        WX: Контейнер средней грузоподъемности для массовых грузов
            текстильный с покрытием и вкладышем Intermediate bulk
            container, textile, coated and liner
        WY: Контейнер средней грузоподъемности для массовых грузов
            фанерный с внутренним вкладышем Intermediate bulk container,
            plywood, with inner liner
        WZ: Контейнер средней грузоподъемности для массовых грузов из
            древесного материала с внутренним вкладышем Intermediate
            bulk container, reconstituted wood, with inner liner
        XA: Мешок из полимерной ткани без внутреннего покрытия/вкладыша
            Bag, woven plastic, without inner coat/liner
        XB: Мешок из полимерной ткани, плотный Bag, woven plastic, sift
            proof
        XC: Мешок из полимерной ткани влагонепроницаемый Bag, woven
            plastic, water resistant
        XD: Мешок из полимерной пленки Bag, plastics film
        XF: Мешок текстильный без внутреннего покрытия/вкладыша Bag,
            textile, without inner coat/liner
        XG: Мешок текстильный плотный Bag, textile, sift proof
        XH: Мешок текстильный влагонепроницаемый Bag, textile, water
            resistant
        XJ: Мешок бумажный многослойный Bag, paper, multi-wall
        XK: Мешок бумажный многослойный влагонепроницаемый Bag, paper,
            multi-wall, water resistant
        YA: Комбинированная упаковка: пластмассовый сосуд в барабане
            стальном Composite packaging, plastic receptacle in steel
            drum
        YB: Комбинированная упаковка: пластмассовый сосуд в ящике
            решетчатом (или обрешетке) из стали Composite packaging,
            plastic receptacle in steel crate box
        YC: Комбинированная упаковка: пластмассовый сосуд в барабане
            алюминиевом Composite packaging, plastic receptacle in
            aluminium drum
        YD: Комбинированная упаковка: пластмассовый сосуд в ящике
            решетчатом (или обрешетке) из алюминия Composite packaging,
            plastic receptacle in aluminium crate
        YF: Комбинированная упаковка: пластмассовый сосуд в деревянной
            коробке Composite packaging, plastic receptacle in wooden
            box
        YH: Комбинированная упаковка: пластмассовый сосуд в коробке
            фанерной Composite packaging, plastic receptacle in plywood
            box
        YJ: Комбинированная упаковка: пластмассовый сосуд в барабане
            фибровом Composite packaging, plastic receptacle in fibre
            drum
        YK: Комбинированная упаковка: пластмассовый сосуд в коробке из
            фибрового картона Composite packaging, plastic receptacle in
            fibreboard box
        YL: Комбинированная упаковка: пластмассовый сосуд в барабане
            пластмассовом Composite packaging, plastic receptacle in
            plastic drum
        YM: Комбинированная упаковка: пластмассовый сосуд в коробке из
            твердой пластмассы Composite packaging, plastic receptacle
            in solid plastic box
        YN: Комбинированная упаковка: стеклянный сосуд в стальном
            барабане Composite packaging, glass receptacle in steel drum
        YP: Комбинированная упаковка: стеклянный сосуд в ящике
            решетчатом (или обрешетке) из стали Composite packaging,
            glass receptacle in steel crate box
        YQ: Комбинированная упаковка: стеклянный сосуд в барабане
            алюминиевом Composite packaging, glass receptacle in
            aluminium drum
        YR: Комбинированная упаковка: стеклянный сосуд в ящике
            решетчатом (или обрешетке) из алюминия Composite packaging,
            glass receptacle in aluminium crate
        YS: Комбинированная упаковка: стеклянный сосуд в коробке
            деревянной Composite packaging, glass receptacle in wooden
            box
        YT: Комбинированная упаковка: стеклянный сосуд в барабане
            фанерном Composite packaging, glass receptacle in plywood
            drum
        YV: Комбинированная упаковка: стеклянный сосуд в корзине
            плетеной с крышкой Composite packaging, glass receptacle in
            wickerwork hamper
        YW: Комбинированная упаковка: стеклянный сосуд в барабане
            фибровом Composite packaging, glass receptacle in fibre drum
        YX: Комбинированная упаковка: стеклянный сосуд в коробке из
            фибрового картона Composite packaging, glass receptacle in
            fibreboard box
        YY: Комбинированная упаковка: стеклянный сосуд в пакете
            пенопластовом Composite packaging, glass receptacle in
            expandable plastic pack
        YZ: Комбинированная упаковка: стеклянный сосуд в пакете из
            твердой пластмассы Composite packaging, glass receptacle in
            solid plastic pack
        ZA: Контейнер средней грузоподъемности для массовых грузов
            бумажный многослойный Intermediate bulk container, paper,
            multi-wall
        ZB: Мешок, большой Bag, large
        ZC: Контейнер средней грузоподъемности для массовых грузов
            бумажный многослойный влагонепроницаемый Intermediate bulk
            container, paper, multi-wall, water resistant
        ZD: Контейнер средней грузоподъемности для твердых
            навалочных/насыпных грузов из жесткой пластмассы с
            конструкционным оснащением Intermediate bulk container,
            rigid plastic, with structural equipment, solids
        ZF: Контейнер средней грузоподъемности для твердых
            навалочных/насыпных грузов из жесткой пластмассы автономный
            Intermediate bulk container, rigid plastic, freestanding,
            solids
        ZG: Контейнер средней грузоподъемности для массовых грузов из
            жесткой пластмассы с конструкционным оснащением
            герметизированный Intermediate bulk container, rigid
            plastic, with structural equipment, pressurised
        ZH: Контейнер средней грузоподъемности для массовых грузов из
            жесткой пластмассы автономный герметизированный Intermediate
            bulk container, rigid plastic, freestanding, pressurised
        ZJ: Контейнер средней грузоподъемности для наливных грузов из
            жесткой пластмассы с конструкционным оснащением Intermediate
            bulk container, rigid plastic, with structural equipment,
            liquids
        ZK: Контейнер средней грузоподъемности для наливных грузов из
            жесткой пластмассы автономный Intermediate bulk container,
            rigid plastic, freestanding, liquids
        ZL: Контейнер средней грузоподъемности для твердых
            навалочных/насыпных грузов составной из жесткой пластмассы
            Intermediate bulk container, composite, rigid plastic,
            solids
        ZM: Контейнер средней грузоподъемности для твердых
            навалочных/насыпных грузов составной из гибкой пластмассы
            Intermediate bulk container, composite, flexible plastic,
            solids
        ZN: Контейнер средней грузоподъемности для массовых грузов
            составной из жесткой пластмассы герметизированный
            Intermediate bulk container, composite, rigid plastic,
            pressurised
        ZP: Контейнер средней грузоподъемности для массовых грузов
            составной из гибкой пластмассы герметизированный
            Intermediate bulk container, composite, flexible plastic,
            pressurised
        ZQ: Контейнер средней грузоподъемности для наливных грузов
            составной из жесткой пластмассы Intermediate bulk container,
            composite, rigid plastic, liquids
        ZR: Контейнер средней грузоподъемности для наливных грузов
            составной из гибкой пластмассы Intermediate bulk container,
            composite, flexible plastic, liquids
        ZS: Контейнер средней грузоподъемности для массовых грузов
            составной Intermediate bulk container, composite
        ZT: Контейнер средней грузоподъемности для массовых грузов из
            фибрового картона Intermediate bulk container, fibreboard
        ZU: Контейнер средней грузоподъемности для массовых грузов
            гибкий Intermediate bulk container, flexible
        ZV: Контейнер средней грузоподъемности для массовых грузов из
            прочего металла, кроме стали Intermediate bulk container,
            metal, other than steel
        ZW: Контейнер средней грузоподъемности для массовых грузов из
            естественной древесины Intermediate bulk container, natural
            wood
        ZX: Контейнер средней грузоподъемности для массовых грузов
            фанерный Intermediate bulk container, plywood
        ZY: Контейнер средней грузоподъемности для массовых грузов из
            древесного материала Intermediate bulk container,
            reconstituted wood
        ZZ: По взаимному определению Mutually defined
    """

    VALUE_1_A = "1A"
    VALUE_1_B = "1B"
    VALUE_1_D = "1D"
    VALUE_1_F = "1F"
    VALUE_1_G = "1G"
    VALUE_1_W = "1W"
    VALUE_2_C = "2C"
    VALUE_3_A = "3A"
    VALUE_3_H = "3H"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_4_A = "4A"
    VALUE_4_B = "4B"
    VALUE_4_C = "4C"
    VALUE_4_D = "4D"
    VALUE_4_F = "4F"
    VALUE_4_G = "4G"
    VALUE_4_H = "4H"
    VALUE_5_H = "5H"
    VALUE_5_L = "5L"
    VALUE_5_M = "5M"
    VALUE_6_H = "6H"
    VALUE_6_P = "6P"
    VALUE_7_A = "7A"
    VALUE_7_B = "7B"
    VALUE_8_A = "8A"
    VALUE_8_B = "8B"
    VALUE_8_C = "8C"
    AA = "AA"
    AB = "AB"
    AC = "AC"
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AH = "AH"
    AI = "AI"
    AJ = "AJ"
    AL = "AL"
    AM = "AM"
    AP = "AP"
    AT = "AT"
    AV = "AV"
    B4 = "B4"
    BA = "BA"
    BB = "BB"
    BC = "BC"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BK = "BK"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BP = "BP"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BU = "BU"
    BV = "BV"
    BW = "BW"
    BX = "BX"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CB = "CB"
    CC = "CC"
    CD = "CD"
    CE = "CE"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CJ = "CJ"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CP = "CP"
    CQ = "CQ"
    CR = "CR"
    CS = "CS"
    CT = "CT"
    CU = "CU"
    CV = "CV"
    CW = "CW"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DA = "DA"
    DB = "DB"
    DC = "DC"
    DG = "DG"
    DH = "DH"
    DI = "DI"
    DJ = "DJ"
    DK = "DK"
    DL = "DL"
    DM = "DM"
    DN = "DN"
    DP = "DP"
    DR = "DR"
    DS = "DS"
    DT = "DT"
    DU = "DU"
    DV = "DV"
    DW = "DW"
    DX = "DX"
    DY = "DY"
    EC = "EC"
    ED = "ED"
    EE = "EE"
    EF = "EF"
    EG = "EG"
    EH = "EH"
    EI = "EI"
    EN = "EN"
    FC = "FC"
    FD = "FD"
    FE = "FE"
    FI = "FI"
    FL = "FL"
    FO = "FO"
    FP = "FP"
    FR = "FR"
    FT = "FT"
    FX = "FX"
    GB = "GB"
    GI = "GI"
    GL = "GL"
    GR = "GR"
    GY = "GY"
    GZ = "GZ"
    HA = "HA"
    HB = "HB"
    HC = "HC"
    HG = "HG"
    HN = "HN"
    HR = "HR"
    IA = "IA"
    IB = "IB"
    IC = "IC"
    ID = "ID"
    IE = "IE"
    IF = "IF"
    IG = "IG"
    IH = "IH"
    IK = "IK"
    IN = "IN"
    IZ = "IZ"
    JB = "JB"
    JC = "JC"
    JG = "JG"
    JR = "JR"
    JT = "JT"
    JY = "JY"
    KG = "KG"
    KI = "KI"
    LE = "LE"
    LG = "LG"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LZ = "LZ"
    MA = "MA"
    MB = "MB"
    MC = "MC"
    ME = "ME"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MW = "MW"
    MX = "MX"
    NA = "NA"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NS = "NS"
    NT = "NT"
    NU = "NU"
    NV = "NV"
    OT = "OT"
    OU = "OU"
    P2 = "P2"
    PA = "PA"
    PB = "PB"
    PC = "PC"
    PD = "PD"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PI = "PI"
    PJ = "PJ"
    PK = "PK"
    PL = "PL"
    PN = "PN"
    PO = "PO"
    PP = "PP"
    PR = "PR"
    PT = "PT"
    PU = "PU"
    PV = "PV"
    PX = "PX"
    PY = "PY"
    PZ = "PZ"
    QA = "QA"
    QB = "QB"
    QC = "QC"
    QD = "QD"
    QF = "QF"
    QG = "QG"
    QH = "QH"
    QJ = "QJ"
    QK = "QK"
    QL = "QL"
    QM = "QM"
    QN = "QN"
    QP = "QP"
    QQ = "QQ"
    QR = "QR"
    QS = "QS"
    RD = "RD"
    RG = "RG"
    RJ = "RJ"
    RK = "RK"
    RL = "RL"
    RO = "RO"
    RT = "RT"
    RZ = "RZ"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SH = "SH"
    SI = "SI"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SO = "SO"
    SP = "SP"
    SS = "SS"
    ST = "ST"
    SU = "SU"
    SV = "SV"
    SW = "SW"
    SX = "SX"
    SY = "SY"
    SZ = "SZ"
    T1 = "T1"
    TB = "TB"
    TC = "TC"
    TD = "TD"
    TE = "TE"
    TG = "TG"
    TI = "TI"
    TK = "TK"
    TL = "TL"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TS = "TS"
    TT = "TT"
    TU = "TU"
    TV = "TV"
    TW = "TW"
    TY = "TY"
    TZ = "TZ"
    UC = "UC"
    UN = "UN"
    VA = "VA"
    VG = "VG"
    VI = "VI"
    VK = "VK"
    VL = "VL"
    VO = "VO"
    VP = "VP"
    VQ = "VQ"
    VR = "VR"
    VS = "VS"
    VY = "VY"
    WA = "WA"
    WB = "WB"
    WC = "WC"
    WD = "WD"
    WF = "WF"
    WG = "WG"
    WH = "WH"
    WJ = "WJ"
    WK = "WK"
    WL = "WL"
    WM = "WM"
    WN = "WN"
    WP = "WP"
    WQ = "WQ"
    WR = "WR"
    WS = "WS"
    WT = "WT"
    WU = "WU"
    WV = "WV"
    WW = "WW"
    WX = "WX"
    WY = "WY"
    WZ = "WZ"
    XA = "XA"
    XB = "XB"
    XC = "XC"
    XD = "XD"
    XF = "XF"
    XG = "XG"
    XH = "XH"
    XJ = "XJ"
    XK = "XK"
    YA = "YA"
    YB = "YB"
    YC = "YC"
    YD = "YD"
    YF = "YF"
    YH = "YH"
    YJ = "YJ"
    YK = "YK"
    YL = "YL"
    YM = "YM"
    YN = "YN"
    YP = "YP"
    YQ = "YQ"
    YR = "YR"
    YS = "YS"
    YT = "YT"
    YV = "YV"
    YW = "YW"
    YX = "YX"
    YY = "YY"
    YZ = "YZ"
    ZA = "ZA"
    ZB = "ZB"
    ZC = "ZC"
    ZD = "ZD"
    ZF = "ZF"
    ZG = "ZG"
    ZH = "ZH"
    ZJ = "ZJ"
    ZK = "ZK"
    ZL = "ZL"
    ZM = "ZM"
    ZN = "ZN"
    ZP = "ZP"
    ZQ = "ZQ"
    ZR = "ZR"
    ZS = "ZS"
    ZT = "ZT"
    ZU = "ZU"
    ZV = "ZV"
    ZW = "ZW"
    ZX = "ZX"
    ZY = "ZY"
    ZZ = "ZZ"

    __descriptions = {
        VALUE_1_A: "Барабан стальной\nDrum, steel",
        VALUE_1_B: "Барабан, алюминиевый\nDrum, aluminium",
        VALUE_1_D: "Барабан фанерный\nDrum, plywood",
        VALUE_1_F: "Контейнер, гибкий\nContainer, flexible",
        VALUE_1_G: "Барабан фибровый\nDrum, fibre",
        VALUE_1_W: "Барабан, деревянный\nDrum, wooden",
        VALUE_2_C: "Бочка (емкостью около 164 л) деревянная\nBarrel, wooden",
        VALUE_3_A: "Канистра, стальная\nJerrycan, steel",
        VALUE_3_H: "Канистра, пластмассовая\nJerrycan, plastic",
        VALUE_43: "Мешок большой для крупноразмерных навалочных грузов\nBag, super bulk",
        VALUE_44: "Мешок полиэтиленовый\nBag, polybag",
        VALUE_4_A: "Коробка, стальная\nBox, steel",
        VALUE_4_B: "Коробка, алюминиевая\nBox, aluminium",
        VALUE_4_C: "Коробка из естественной древесины\nBox, natural wood",
        VALUE_4_D: "Коробка, фанерная\nBox, plywood",
        VALUE_4_F: "Коробка из древесного материала\nBox, reconstituted wood",
        VALUE_4_G: "Коробка из фибрового картона\nBox, fibreboard",
        VALUE_4_H: "Коробка, пластмассовая\nBox, plastic",
        VALUE_5_H: "Мешок из полимерной ткани\nBag, woven plastic",
        VALUE_5_L: "Мешок текстильный\nBag, textile",
        VALUE_5_M: "Мешок, бумажный\nBag, paper",
        VALUE_6_H: (
            "Комбинированная упаковка: пластмассовый сосуд\nComposite packaging, "
            "plastic receptacle"
        ),
        VALUE_6_P: (
            "Комбинированная упаковка: стеклянный сосуд\nComposite packaging, glass "
            "receptacle"
        ),
        VALUE_7_A: "Ящик автомобильный\nCase, car",
        VALUE_7_B: "Ящик деревянный\nCase, wooden",
        VALUE_8_A: "Поддон деревянный\nPallet, wooden",
        VALUE_8_B: "Ящик деревянный\nCrate, wooden",
        VALUE_8_C: "Пачка деревянная\nBundle, wooden",
        AA: (
            "Контейнер средней грузоподъемности для массовых грузов из жесткой "
            "пластмассы\nIntermediate bulk container, rigid plastic"
        ),
        AB: "Сосуд, фибровый\nReceptacle, fibre",
        AC: "Сосуд, бумажный\nReceptacle, paper",
        AD: "Сосуд, деревянный\nReceptacle, wooden",
        AE: "Аэрозольная упаковка\nAerosol",
        AF: (
            "Поддон модульный с обечайкой 80 x 60 см\nPallet, modular, collars 80 cm x"
            " 60 cm"
        ),
        AG: "Поддон в термоусадочной пленке\nPallet, shrink-wrapped",
        AH: "Поддон 100 x 110 см\nPallet, 100 cm x 110 cm",
        AI: "Грейферный ковш\nClamshell",
        AJ: "Кулек\nCone",
        AL: "Шар\nBall",
        AM: "Ампула, незащищенная\nAmpoule, non-protected",
        AP: "Ампула, защищенная\nAmpoule, protected",
        AT: "Пульверизатор\nAtomizer",
        AV: "Капсула\nCapsule",
        B4: "Лента\nBelt",
        BA: "Бочка (емкостью около 164 л)\nBarrel",
        BB: "Бобина\nBobbin",
        BC: "Ящик решетчатый для бутылок\nBottlecrate/bottlerack",
        BD: "Доска\nBoard",
        BE: "Пакет (пачка/связка)\nBundle",
        BF: "Баллон, незащищенный\nBalloon, non-protected",
        BG: "Мешок\nBag",
        BH: "Пачка (пакет/связка)\nBunch",
        BI: "Бункер\nBin",
        BJ: "Бадья\nBucket",
        BK: "Корзина\nBasket",
        BL: "Кипа, спрессованная\nBale, compressed",
        BM: "Чан\nBasin",
        BN: "Кипа, неспрессованная\nBale, non-compressed",
        BO: "Бутылка цилиндрическая незащищенная\nBottle, non-protected, cylindrical",
        BP: "Баллон, защищенный\nBalloon, protected",
        BQ: "Бутылка цилиндрическая защищенная\nBottle, protected cylindrical",
        BR: "Брус (брусок)\nBar",
        BS: "Бутылка с выпуклыми стенками незащищенная\nBottle, non-protected, bulbous",
        BT: "Рулон (обивочного или настилочного материала)\nBolt",
        BU: "Бочка для вина или пива\nButt",
        BV: "Бутылка с выпуклыми стенками защищенная\nBottle, protected bulbous",
        BW: "Коробка для жидкостей\nBox, for liquids",
        BX: "Коробка\nBox",
        BY: "Доска в пакете/пачке/связке\nBoard, in bundle/bunch/truss",
        BZ: "Брус (брусок) в пакете/пачке/связке\nBars, in bundle/bunch/truss",
        CA: "Банка (емкостью менее 5 л) жестяная прямоугольная\nCan, rectangular",
        CB: "Ящик решетчатый для пива\nCrate, beer",
        CC: "Бидон\nChurn",
        CD: (
            "Банка (емкостью менее 5 л) жестяная с ручкой и выпускным отверстием\nCan,"
            " with handle and spout"
        ),
        CE: "Корзина, рыбацкая\nCreel",
        CF: "Кофр\nCoffer",
        CG: "Клеть\nCage",
        CH: "Сундук\nChest",
        CI: "Банка жестяная для сухих продуктов (массой до 2,2 кг)\nCanister",
        CJ: "Гроб\nCoffin",
        CK: "Бочка\nCask",
        CL: "Бухта\nCoil",
        CM: "Кардная лента\nCard",
        CN: (
            "Контейнер, прочее транспортировочное оборудование, кроме "
            "поименованного\nContainer, not otherwise specified as transport equipment"
        ),
        CO: "Бутыль оплетенная незащищенная\nCarboy, non-protected",
        CP: "Бутыль оплетенная защищенная\nCarboy, protected",
        CQ: "Кассета\nCartridge",
        CR: "Ящик, решетчатый (или обрешетка)\nCrate",
        CS: "Ящик\nCase",
        CT: "Коробка, картонная\nCarton",
        CU: "Чаша\nCup",
        CV: "Чехол\nCover",
        CW: "Клеть, роликовая\nCage, roll",
        CX: "Банка (емкостью менее 5 л) жестяная цилиндрическая\nCan, cylindrical",
        CY: "Цилиндр\nCylinder",
        CZ: "Брезент\nCanvas",
        DA: (
            "Ящик решетчатый (или обрешетка) многослойный пластмассовый\nCrate, "
            "multiple layer, plastic"
        ),
        DB: (
            "Ящик решетчатый (или обрешетка) многослойный деревянный\nCrate, multiple "
            "layer, wooden"
        ),
        DC: (
            "Ящик решетчатый (или обрешетка) многослойный картонный\nCrate, multiple "
            "layer, cardboard"
        ),
        DG: (
            "Клеть (многооборотная) Общего фонда транспортировочного оборудования "
            "EC\nCage, Commonwealth Handling Equipment Pool (CHEP)"
        ),
        DH: (
            "Коробка (многооборотная) из Общего фонда транспортировочного оборудования"
            " ЕС, Еврокоробка\nBox, Commonwealth Handling Equipment Pool (CHEP), "
            "Eurobox"
        ),
        DI: "Барабан, железный\nDrum, iron",
        DJ: (
            "Бутыль оплетенная большая (емкостью от 9 до 54 л) незащищенная\nDemijohn,"
            " non-protected"
        ),
        DK: "Ящик решетчатый для массовых грузов картонный\nCrate, bulk, cardboard",
        DL: "Ящик решетчатый для массовых грузов пластмассовый\nCrate, bulk, plastic",
        DM: "Ящик решетчатый для массовых грузов деревянный\nCrate, bulk, wooden",
        DN: "Дозатор\nDispenser",
        DP: (
            "Бутыль оплетенная большая (емкостью от 9 до 54 л) защищенная\nDemijohn, "
            "protected"
        ),
        DR: "Барабан\nDrum",
        DS: (
            "Лоток с одним настилом без покрытия пластмассовый\nTray, one layer no "
            "cover, plastic"
        ),
        DT: (
            "Лоток с одним настилом без покрытия деревянный\nTray, one layer no cover,"
            " wooden"
        ),
        DU: (
            "Лоток с одним настилом без покрытия полистироловый\nTray, one layer no "
            "cover, polystyrene"
        ),
        DV: (
            "Лоток с одним настилом без покрытия картонный\nTray, one layer no cover, "
            "cardboard"
        ),
        DW: (
            "Лоток с двумя настилами без покрытия пластмассовый\nTray, two layers no "
            "cover, plastic tray"
        ),
        DX: (
            "Лоток с двумя настилами без покрытия деревянный\nTray, two layers no "
            "cover, wooden"
        ),
        DY: (
            "Лоток с двумя настилами без покрытия картонный\nTray, two layers no "
            "cover, cardboard"
        ),
        EC: "Мешок, пластмассовый\nBag, plastic",
        ED: "Ящик с поддоном\nCase, with pallet base",
        EE: "Ящик с поддоном деревянный\nCase, with pallet base, wooden",
        EF: "Ящик с поддоном картонный\nCase, with pallet base, cardboard",
        EG: "Ящик с поддоном пластмассовый\nCase, with pallet base, plastic",
        EH: "Ящик с поддоном металлический\nCase, with pallet base, metal",
        EI: "Ящик, изотермический\nCase, isothermic",
        EN: "Конверт\nEnvelope",
        FC: "Ящик решетчатый для фруктов\nCrate, fruit",
        FD: "Ящик решетчатый (или обрешетка) рамный\nCrate, framed",
        FE: "Мягкий мешок, Гибкая цистерна\nFlexitank, Flexibag",
        FI: "Бочонок (емкостью около 41 л)\nFirkin",
        FL: "Фляга\nFlask",
        FO: "Сундучок\nFootlocker",
        FP: "Кассета с пленкой (фильмпак)\nFilmpack",
        FR: "Рама\nFrame",
        FT: "Контейнер для пищевых продуктов\nFoodtainer",
        FX: "Мешок, гибкий контейнер\nBag, flexible container",
        GB: "Баллон, газовый\nBottle, gas",
        GI: "Балка\nGirder",
        GL: "Контейнер, галлон\nContainer, gallon",
        GR: "Сосуд, стеклянный\nReceptacle, glass",
        GY: "Мешок из мешковины\nBag, gunny",
        GZ: "Балка в пакете/пачке/связке\nGirders, in bundle/bunch/truss",
        HA: "Корзина с ручкой, пластмассовая\nBasket, with handle, plastic",
        HB: "Корзина с ручкой из древесины\nBasket, with handle, wooden",
        HC: "Корзина с ручкой, картонная\nBasket, with handle, cardboard",
        HG: "Бочка емкостью 238 л (хогсхед)\nHogshead",
        HN: "Крюк\nHanger",
        HR: "Корзина с крышкой\nHamper",
        IA: "Упаковка демонстрационная деревянная\nPackage, display, wooden",
        IB: "Упаковка демонстрационная картонная\nPackage, display, cardboard",
        IC: "Упаковка демонстрационная пластмассовая\nPackage, display, plastic",
        ID: "Упаковка демонстрационная металлическая\nPackage, display, metal",
        IE: "Упаковка, выставочная\nPackage, show",
        IF: "Упаковка, выпрессованная\nPackage, flow",
        IG: "Упаковка в оберточной бумаге\nPackage, paper wrapped",
        IH: "Барабан, пластмассовый\nDrum, plastic",
        IK: (
            "Упаковка картонная с отверстиями для бутылок\nPackage, cardboard, with "
            "bottle grip-holes"
        ),
        IN: "Слиток\nIngot",
        IZ: "Слитки в пакете/пачке/связке\nIngots, in bundle/bunch/truss",
        JB: "Мешок большой,\nBag, jumbo",
        JC: "Канистра, прямоугольная\nJerrican, rectangular",
        JG: "Кувшин, маленький\nJug",
        JR: "Банка широкогорлая (емкостью около 4,5 литров)\nJar",
        JT: "Мешок, джутовый\nJute bag",
        JY: "Канистра, цилиндрическая\nJerrican, cylindrical",
        KG: "Бочонок (емкостью около 46 л)\nKeg",
        KI: "Набор\nKit",
        LE: "Багаж\nLuggage",
        LG: "Бревно\nLog",
        LT: "Грузовая партия (лот)\nLot",
        LU: "Ящик\nLug",
        LV: (
            "Короб деревянный (лифтван) размером около 220 см (длина) x 115 см "
            "(ширина) x 220 см (высота)\nLiftvan"
        ),
        LZ: "Бревно в пакете/пачке/связке\nLogs, in bundle/bunch/truss",
        MA: "Ящик металлический\nCrate, metal",
        MB: "Пакет бумажный многослойный\nBag, multiply",
        MC: "Ящик решетчатый для молока\nCrate, milk",
        ME: "Контейнер металлический\nContainer, metal",
        MR: "Сосуд, металлический\nReceptacle, metal",
        MS: "Мешок (куль) многослойный\nSack, multi-wall",
        MT: "Мешок, рогожный\nMat",
        MW: "Сосуд с пластмассовым покрытием\nReceptacle, plastic wrapped",
        MX: "Спичечный коробок\nMatchbox",
        NA: "Нет сведений\nNot available",
        NE: "Неупакованный или нерасфасованный\nUnpacked or unpackaged",
        NF: (
            "Неупакованный или нерасфасованный одноместный груз\nUnpacked or "
            "unpackaged, single unit"
        ),
        NG: (
            "Неупакованный или нерасфасованный многоместный груз\nUnpacked or "
            "unpackaged, multiple units"
        ),
        NS: "Гнездо (ячейка)\nNest",
        NT: "Сетка\nNet",
        NU: "Сетка трубчатая пластмассовая\nNet, tube, plastic",
        NV: "Сетка трубчатая текстильная\nNet, tube, textile",
        OT: "Октабин\nOctabin",
        OU: "Контейнер наружный\nContainer, outer",
        P2: "Лоток\nPan",
        PA: "Пакет\nPacket",
        PB: "Поддон, ящичный\nPallet, box",
        PC: "Бандероль\nParcel",
        PD: (
            "Поддон модульный с обечайкой 80 x 100 см\nPallet, modular, collars 80 cm "
            "x 100 cm"
        ),
        PE: (
            "Поддон модульный с обечайкой 80 х 120 см\nPallet, modular, collars 80 cm "
            "x 120 cm"
        ),
        PF: "Штабель\nPen",
        PG: "Плита\nPlate",
        PH: "Кувшин, большой\nPitcher",
        PI: "Труба\nPipe",
        PJ: "Корзина из шпона для ягод и фруктов\nPunnet",
        PK: "Упаковка\nPackage",
        PL: "Ведро\nPail",
        PN: "Доска, толстая\nPlank",
        PO: "Пакет (мешочек)\nPouch",
        PP: "Штука\nPiece",
        PR: "Сосуд, пластмассовый\nReceptacle, plastic",
        PT: "Горшок\nPot",
        PU: "Лоток\nTray",
        PV: "Труба в пакете/пачке/связке\nPipes, in bundle/bunch/truss",
        PX: "Поддон\nPallet",
        PY: "Плиты в пакете/пачке/связке\nPlates, in bundle/bunch/truss",
        PZ: "Доска толстая в пакете/пачке/связке\nPlanks, in bundle/bunch/truss",
        QA: "Барабан стальной с несъемным днищем\nDrum, steel, non - removable head",
        QB: "Барабан стальной со съемным днищем\nDrum, steel, removable head",
        QC: "Барабан алюминиевый с несъемным днищем\nDrum, aluminium, non-removable head",
        QD: "Барабан алюминиевый со съемным днищем\nDrum, aluminium, removable head",
        QF: "Барабан пластмассовый с несъемным днищем\nDrum, plastic, non-removable head",
        QG: "Барабан пластмассовый со съемным днищем\nDrum, plastic, removable head",
        QH: (
            "Бочка (емкостью около 164 л) деревянная шпунтованная\nBarrel, wooden, "
            "bung type"
        ),
        QJ: (
            "Бочка (емкостью около 164 л) деревянная со съемным днищем\nBarrel, "
            "wooden, removable head"
        ),
        QK: "Канистра стальная с несъемным днищем\nJerrican, steel, non-removable head",
        QL: "Канистра стальная со съемным днищем\nJerrican, steel, removable head",
        QM: (
            "Канистра пластмассовая с несъемным днищем\nJerrican, plastic, non-"
            "removable head"
        ),
        QN: "Канистра пластмассовая со съемным днищем\nJerrican, plastic, removable head",
        QP: (
            "Коробка деревянная из естественной древесины обыкновенная\nBox, wooden, "
            "natural wood, ordinary"
        ),
        QQ: (
            "Коробка деревянная из естественной древесины с плотно пригнанными "
            "стенками\nBox, wooden, natural wood, with sift proof walls"
        ),
        QR: "Коробка, пенопластовая\nBox, plastic, expanded",
        QS: "Коробка из твердой пластмассы\nBox, plastic, solid",
        RD: "Прут\nRod",
        RG: "Кольцо\nRing",
        RJ: "Стойка, вешалка для одежды\nRack, clothing hanger",
        RK: "Стойка\nRack",
        RL: "Катушка\nReel",
        RO: "Рулон (полосового материала)\nRoll",
        RT: "Сетка типа используемой для овощей или фруктов\nRednet",
        RZ: "Прут в пакете/пачке/связке\nRods, in bundle/bunch/truss",
        SA: "Мешок (куль)\nSack",
        SB: "Сляб\nSlab",
        SC: "Ящик решетчатый (или обрешетка) мелкий\nCrate, shallow",
        SD: "Шпиндель\nSpindle",
        SE: "Сундук, морской\nSea-chest",
        SH: "Пакетик\nSachet",
        SI: "Стеллаж\nSkid",
        SK: "Ящик, каркасный\nCase, skeleton",
        SL: "Лист, прокладной\nSlipsheet",
        SM: "Лист, металлический\nSheet metal",
        SO: "Шпулька\nSpool",
        SP: "Лист с пластмассовым покрытием\nSheet, plastic wrapping",
        SS: "Ящик, стальной\nCase, steel",
        ST: "Лист\nSheet",
        SU: "Чемодан\nSuitcase",
        SV: "Конверт, стальной\nEnvelope, steel",
        SW: "В термоусадочной пленке\nShrink-wrapped",
        SX: "Комплект\nSet",
        SY: "Гильза\nSleeve",
        SZ: "Лист в пакете/пачке/связке\nSheets, in bundle/bunch/truss",
        T1: "Таблетка\nTablet",
        TB: "Кадка\nTub",
        TC: "Чайная коробка\nTea-chest",
        TD: "Трубка или туба, складывающаяся\nTube, collapsible",
        TE: "Шина\nTyre",
        TG: "Цистерна контейнер универсальный\nTank container, generic",
        TI: "Бочка деревянная (емкостью около 200 л)\nTierce",
        TK: "Цистерна, прямоугольная\nTank, rectangular",
        TL: "Кадка с крышкой\nTub, with lid",
        TN: "Банка, жестяная (консервная)\nTin",
        TO: "Бочка для вина или пива большая (емкостью около 1146 л) (тан)\nTun",
        TR: "Сундук, дорожный\nTrunk",
        TS: "Связка\nTruss",
        TT: "Мешок\nBag, tote",
        TU: "Трубка или туба\nTube",
        TV: "Трубка или туба с насадкой\nTube, with nozzle",
        TW: "Поддон\nPallet, triwall",
        TY: "Цистерна, цилиндрическая\nTank, cylindrical",
        TZ: "Трубка или туба в пакете/пачке/связке\nTubes, in bundle/bunch/truss",
        UC: "Без клети\nUncaged",
        UN: "Единица\nUnit",
        VA: "Бак\nVat",
        VG: "Наливом газ (при 1031 мБар и 15°C)\nBulk, gas (at 1 031 mbar and 15° C)",
        VI: "Флакон\nVial",
        VK: "Консоль для оборудования, помещающаяся в минифургон\nVanpack",
        VL: "Наливом жидкость\nBulk, liquid",
        VO: (
            "Насыпью твердые крупные частицы (мелкие куски)\nBulk, solid, large "
            "particles (nodules)"
        ),
        VP: "В вакуумной упаковке\nVacuum-packed",
        VQ: (
            "Наливом газ сжиженный (при температуре/давлении, отличающихся от "
            "нормальных)\nBulk, liquefied gas (at abnormal temperature/pressure)"
        ),
        VR: (
            "Насыпью твердые гранулированные частицы (гранулы)\nBulk, solid, granular "
            "particles (grains)"
        ),
        VS: "Навалом металлолом\nBulk, scrap metal",
        VY: (
            "Насыпью твердые мелкие частицы (порошки)\nBulk, solid, fine particles "
            "(powders)"
        ),
        WA: (
            "Контейнер средней грузоподъемности для массовых грузов\nIntermediate bulk"
            " container"
        ),
        WB: "Бутылка оплетенная\nWicker bottle",
        WC: (
            "Контейнер средней грузоподъемности для массовых грузов "
            "стальной\nIntermediate bulk container, steel"
        ),
        WD: (
            "Контейнер средней грузоподъемности для массовых грузов "
            "алюминиевый\nIntermediate bulk container, aluminium"
        ),
        WF: (
            "Контейнер средней грузоподъемности для массовых грузов "
            "металлический\nIntermediate bulk container, metal"
        ),
        WG: (
            "Контейнер средней грузоподъемности для массовых грузов герметизированный "
            "свыше 10 КПа\nIntermediate bulk container, steel, pressurised &gt; 10 kpa"
        ),
        WH: (
            "Контейнер средней грузоподъемности для массовых грузов алюминиевый "
            "герметизированный свыше 10 КПа\nIntermediate bulk container, aluminium, "
            "pressurised &gt; 10 kpa"
        ),
        WJ: (
            "Контейнер средней грузоподъемности для массовых грузов герметизированный "
            "10 Кпа\nIntermediate bulk container, metal, pressure 10 kpa"
        ),
        WK: (
            "Контейнер средней грузоподъемности для наливных грузов "
            "стальной\nIntermediate bulk container, steel, liquid"
        ),
        WL: (
            "Контейнер средней грузоподъемности для наливных грузов "
            "алюминиевый\nIntermediate bulk container, aluminium, liquid"
        ),
        WM: (
            "Контейнер средней грузоподъемности для наливных грузов "
            "металлический\nIntermediate bulk container, metal, liquid"
        ),
        WN: (
            "Контейнер средней грузоподъемности для массовых грузов из полимерной "
            "ткани без покрытия/вкладыша\nIntermediate bulk container, woven plastic, "
            "without coat/liner"
        ),
        WP: (
            "Контейнер средней грузоподъемности для массовых грузов из полимерной "
            "ткани с покрытием\nIntermediate bulk container, woven plastic, coated"
        ),
        WQ: (
            "Контейнер средней грузоподъемности для массовых грузов из полимерной "
            "ткани с вкладышем\nIntermediate bulk container, woven plastic, with liner"
        ),
        WR: (
            "Контейнер средней грузоподъемности для массовых грузов из пластикового "
            "волокна с покрытием и вкладышем\nIntermediate bulk container, woven "
            "plastic, coated and liner"
        ),
        WS: (
            "Контейнер средней грузоподъемности для массовых грузов из полимерной "
            "пленки\nIntermediate bulk container, plastic film"
        ),
        WT: (
            "Контейнер средней грузоподъемности для массовых грузов текстильный без "
            "покрытия/вкладыша\nIntermediate bulk container, textile without "
            "coat/liner"
        ),
        WU: (
            "Контейнер средней грузоподъемности для массовых грузов из естественной "
            "древесины с внутренним вкладышем\nIntermediate bulk container, natural "
            "wood, with inner liner"
        ),
        WV: (
            "Контейнер средней грузоподъемности для массовых грузов текстильный с "
            "покрытием\nIntermediate bulk container, textile, coated"
        ),
        WW: (
            "Контейнер средней грузоподъемности для массовых грузов текстильный с "
            "вкладышем\nIntermediate bulk container, textile, with liner"
        ),
        WX: (
            "Контейнер средней грузоподъемности для массовых грузов текстильный с "
            "покрытием и вкладышем\nIntermediate bulk container, textile, coated and "
            "liner"
        ),
        WY: (
            "Контейнер средней грузоподъемности для массовых грузов фанерный с "
            "внутренним вкладышем\nIntermediate bulk container, plywood, with inner "
            "liner"
        ),
        WZ: (
            "Контейнер средней грузоподъемности для массовых грузов из древесного "
            "материала с внутренним вкладышем\nIntermediate bulk container, "
            "reconstituted wood, with inner liner"
        ),
        XA: (
            "Мешок из полимерной ткани без внутреннего покрытия/вкладыша\nBag, woven "
            "plastic, without inner coat/liner"
        ),
        XB: "Мешок из полимерной ткани, плотный\nBag, woven plastic, sift proof",
        XC: (
            "Мешок из полимерной ткани влагонепроницаемый\nBag, woven plastic, water "
            "resistant"
        ),
        XD: "Мешок из полимерной пленки\nBag, plastics film",
        XF: (
            "Мешок текстильный без внутреннего покрытия/вкладыша\nBag, textile, "
            "without inner coat/liner"
        ),
        XG: "Мешок текстильный плотный\nBag, textile, sift proof",
        XH: "Мешок текстильный влагонепроницаемый\nBag, textile, water resistant",
        XJ: "Мешок бумажный многослойный\nBag, paper, multi-wall",
        XK: (
            "Мешок бумажный многослойный влагонепроницаемый\nBag, paper, multi-wall, "
            "water resistant"
        ),
        YA: (
            "Комбинированная упаковка: пластмассовый сосуд в барабане "
            "стальном\nComposite packaging, plastic receptacle in steel drum"
        ),
        YB: (
            "Комбинированная упаковка: пластмассовый сосуд в ящике решетчатом (или "
            "обрешетке) из стали\nComposite packaging, plastic receptacle in steel "
            "crate box"
        ),
        YC: (
            "Комбинированная упаковка: пластмассовый сосуд в барабане "
            "алюминиевом\nComposite packaging, plastic receptacle in aluminium drum"
        ),
        YD: (
            "Комбинированная упаковка: пластмассовый сосуд в ящике решетчатом (или "
            "обрешетке) из алюминия\nComposite packaging, plastic receptacle in "
            "aluminium crate"
        ),
        YF: (
            "Комбинированная упаковка: пластмассовый сосуд в деревянной "
            "коробке\nComposite packaging, plastic receptacle in wooden box"
        ),
        YH: (
            "Комбинированная упаковка: пластмассовый сосуд в коробке "
            "фанерной\nComposite packaging, plastic receptacle in plywood box"
        ),
        YJ: (
            "Комбинированная упаковка: пластмассовый сосуд в барабане "
            "фибровом\nComposite packaging, plastic receptacle in fibre drum"
        ),
        YK: (
            "Комбинированная упаковка: пластмассовый сосуд в коробке из фибрового "
            "картона\nComposite packaging, plastic receptacle in fibreboard box"
        ),
        YL: (
            "Комбинированная упаковка: пластмассовый сосуд в барабане "
            "пластмассовом\nComposite packaging, plastic receptacle in plastic drum"
        ),
        YM: (
            "Комбинированная упаковка: пластмассовый сосуд в коробке из твердой "
            "пластмассы\nComposite packaging, plastic receptacle in solid plastic box"
        ),
        YN: (
            "Комбинированная упаковка: стеклянный сосуд в стальном барабане\nComposite"
            " packaging, glass receptacle in steel drum"
        ),
        YP: (
            "Комбинированная упаковка: стеклянный сосуд в ящике решетчатом (или "
            "обрешетке) из стали\nComposite packaging, glass receptacle in steel crate"
            " box"
        ),
        YQ: (
            "Комбинированная упаковка: стеклянный сосуд в барабане "
            "алюминиевом\nComposite packaging, glass receptacle in aluminium drum"
        ),
        YR: (
            "Комбинированная упаковка: стеклянный сосуд в ящике решетчатом (или "
            "обрешетке) из алюминия\nComposite packaging, glass receptacle in "
            "aluminium crate"
        ),
        YS: (
            "Комбинированная упаковка: стеклянный сосуд в коробке "
            "деревянной\nComposite packaging, glass receptacle in wooden box"
        ),
        YT: (
            "Комбинированная упаковка: стеклянный сосуд в барабане фанерном\nComposite"
            " packaging, glass receptacle in plywood drum"
        ),
        YV: (
            "Комбинированная упаковка: стеклянный сосуд в корзине плетеной с "
            "крышкой\nComposite packaging, glass receptacle in wickerwork hamper"
        ),
        YW: (
            "Комбинированная упаковка: стеклянный сосуд в барабане фибровом\nComposite"
            " packaging, glass receptacle in fibre drum"
        ),
        YX: (
            "Комбинированная упаковка: стеклянный сосуд в коробке из фибрового "
            "картона\nComposite packaging, glass receptacle in fibreboard box"
        ),
        YY: (
            "Комбинированная упаковка: стеклянный сосуд в пакете "
            "пенопластовом\nComposite packaging, glass receptacle in expandable "
            "plastic pack"
        ),
        YZ: (
            "Комбинированная упаковка: стеклянный сосуд в пакете из твердой "
            "пластмассы\nComposite packaging, glass receptacle in solid plastic pack"
        ),
        ZA: (
            "Контейнер средней грузоподъемности для массовых грузов бумажный "
            "многослойный\nIntermediate bulk container, paper, multi-wall"
        ),
        ZB: "Мешок, большой\nBag, large",
        ZC: (
            "Контейнер средней грузоподъемности для массовых грузов бумажный "
            "многослойный влагонепроницаемый\nIntermediate bulk container, paper, "
            "multi-wall, water resistant"
        ),
        ZD: (
            "Контейнер средней грузоподъемности для твердых навалочных/насыпных грузов"
            " из жесткой пластмассы с конструкционным оснащением\nIntermediate bulk "
            "container, rigid plastic, with structural equipment, solids"
        ),
        ZF: (
            "Контейнер средней грузоподъемности для твердых навалочных/насыпных грузов"
            " из жесткой пластмассы автономный\nIntermediate bulk container, rigid "
            "plastic, freestanding, solids"
        ),
        ZG: (
            "Контейнер средней грузоподъемности для массовых грузов из жесткой "
            "пластмассы с конструкционным оснащением герметизированный\nIntermediate "
            "bulk container, rigid plastic, with structural equipment, pressurised"
        ),
        ZH: (
            "Контейнер средней грузоподъемности для массовых грузов из жесткой "
            "пластмассы автономный герметизированный\nIntermediate bulk container, "
            "rigid plastic, freestanding, pressurised"
        ),
        ZJ: (
            "Контейнер средней грузоподъемности для наливных грузов из жесткой "
            "пластмассы с конструкционным оснащением\nIntermediate bulk container, "
            "rigid plastic, with structural equipment, liquids"
        ),
        ZK: (
            "Контейнер средней грузоподъемности для наливных грузов из жесткой "
            "пластмассы автономный\nIntermediate bulk container, rigid plastic, "
            "freestanding, liquids"
        ),
        ZL: (
            "Контейнер средней грузоподъемности для твердых навалочных/насыпных грузов"
            " составной из жесткой пластмассы\nIntermediate bulk container, composite,"
            " rigid plastic, solids"
        ),
        ZM: (
            "Контейнер средней грузоподъемности для твердых навалочных/насыпных грузов"
            " составной из гибкой пластмассы\nIntermediate bulk container, composite, "
            "flexible plastic, solids"
        ),
        ZN: (
            "Контейнер средней грузоподъемности для массовых грузов составной из "
            "жесткой пластмассы герметизированный\nIntermediate bulk container, "
            "composite, rigid plastic, pressurised"
        ),
        ZP: (
            "Контейнер средней грузоподъемности для массовых грузов составной из "
            "гибкой пластмассы герметизированный\nIntermediate bulk container, "
            "composite, flexible plastic, pressurised"
        ),
        ZQ: (
            "Контейнер средней грузоподъемности для наливных грузов составной из "
            "жесткой пластмассы\nIntermediate bulk container, composite, rigid "
            "plastic, liquids"
        ),
        ZR: (
            "Контейнер средней грузоподъемности для наливных грузов составной из "
            "гибкой пластмассы\nIntermediate bulk container, composite, flexible "
            "plastic, liquids"
        ),
        ZS: (
            "Контейнер средней грузоподъемности для массовых грузов "
            "составной\nIntermediate bulk container, composite"
        ),
        ZT: (
            "Контейнер средней грузоподъемности для массовых грузов из фибрового "
            "картона\nIntermediate bulk container, fibreboard"
        ),
        ZU: (
            "Контейнер средней грузоподъемности для массовых грузов "
            "гибкий\nIntermediate bulk container, flexible"
        ),
        ZV: (
            "Контейнер средней грузоподъемности для массовых грузов из прочего "
            "металла, кроме стали\nIntermediate bulk container, metal, other than "
            "steel"
        ),
        ZW: (
            "Контейнер средней грузоподъемности для массовых грузов из естественной "
            "древесины\nIntermediate bulk container, natural wood"
        ),
        ZX: (
            "Контейнер средней грузоподъемности для массовых грузов "
            "фанерный\nIntermediate bulk container, plywood"
        ),
        ZY: (
            "Контейнер средней грузоподъемности для массовых грузов из древесного "
            "материала\nIntermediate bulk container, reconstituted wood"
        ),
        ZZ: "По взаимному определению\nMutually defined",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        PackingCodeType.VALUE_1_A.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ProductMarkingClass(Enum):
    """
    Тип, описывающий тип маркировки.

    Attributes:
        UNDEFINED: Класс неопределен.
        BN: Номер производственной партии.
        SSCC: SSCC-код.
        EAN8: Маркировка в соответствии с EAN-8.
        EAN13: Маркировка в соответствии с EAN-13.
        EAN128: Маркировка в соответствии с EAN-128.
        BUNDLE: Маркировка вышестоящей групповой упаковки, например,
            паллеты. Может использоваться для поиска группы
            вет.сертификатов для партий, находящихся на данной паллете.
    """

    UNDEFINED = "UNDEFINED"
    BN = "BN"
    SSCC = "SSCC"
    EAN8 = "EAN8"
    EAN13 = "EAN13"
    EAN128 = "EAN128"
    BUNDLE = "BUNDLE"

    __descriptions = {
        UNDEFINED: "Класс неопределен.",
        BN: "Номер производственной партии.",
        SSCC: "SSCC-код.",
        EAN8: "Маркировка в соответствии с EAN-8.",
        EAN13: "Маркировка в соответствии с EAN-13.",
        EAN128: "Маркировка в соответствии с EAN-128.",
        BUNDLE: (
            "Маркировка вышестоящей групповой упаковки, например, паллеты.\nМожет "
            "использоваться для поиска группы вет.сертификатов для партий, находящихся"
            " на данной паллете."
        ),
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ProductMarkingClass.UNDEFINED.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ProductTypeInternalType(Enum):
    """
    Тип, описывающий тип продукции.

    Attributes:
        VALUE_1: Мясо и мясопродукты
        VALUE_2: Корма и кормовые добавки
        VALUE_3: Живые животные
        VALUE_4: Лекарственные средства
        VALUE_5: Пищевые продукты
        VALUE_6: Непищевые продукты и другое
        VALUE_7: Рыба и морепродукты
        VALUE_8: Продукция, не требующая разрешения
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8

    __descriptions = {
        VALUE_1: "Мясо и мясопродукты",
        VALUE_2: "Корма и кормовые добавки",
        VALUE_3: "Живые животные",
        VALUE_4: "Лекарственные средства",
        VALUE_5: "Пищевые продукты",
        VALUE_6: "Непищевые продукты и другое",
        VALUE_7: "Рыба и морепродукты",
        VALUE_8: "Продукция, не требующая разрешения",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ProductType_1.VALUE_1.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ProsperityType(Enum):
    """
    Статус благополучия.

    Attributes:
        UNDEFINED: Неопределенный (не определялся)
        UNKNOWN: Неидентифицированный/неизвестный (статус невозможно
            определить)
        SAFE: Благополучный
        UNSAFE: Неблагополучный
    """

    UNDEFINED = "UNDEFINED"
    UNKNOWN = "UNKNOWN"
    SAFE = "SAFE"
    UNSAFE = "UNSAFE"

    __descriptions = {
        UNDEFINED: "Неопределенный (не определялся)",
        UNKNOWN: "Неидентифицированный/неизвестный (статус невозможно определить)",
        SAFE: "Благополучный",
        UNSAFE: "Неблагополучный",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ProsperityType.UNDEFINED.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ReferenceType(Enum):
    """
    Attributes:
        VALUE_1: Сопроводительный документ. Complementary accompanying
            document
        VALUE_2: Предшествующий документ. Preceding document (Ancestor)
        VALUE_3: Следующий документ. Subsequent/following document
            (Child)
        VALUE_4: Документ, взамен которого выдан текущий документ.
            Replaced document.
        VALUE_5: Документ, заменяющий текущий документ. Replaced by
            document.
        VALUE_6: Связанный документ. Related document.
        VALUE_7: Документ, подтверждающий происхождение партии
            продукции. Certificate of origin.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

    __descriptions = {
        VALUE_1: "Сопроводительный документ. Complementary accompanying document",
        VALUE_2: "Предшествующий документ. Preceding document (Ancestor)",
        VALUE_3: "Следующий документ. Subsequent/following document (Child)",
        VALUE_4: "Документ, взамен которого выдан текущий документ. Replaced document.",
        VALUE_5: "Документ, заменяющий текущий документ. Replaced by document.",
        VALUE_6: "Связанный документ. Related document.",
        VALUE_7: (
            "Документ, подтверждающий происхождение партии продукции. Certificate of "
            "origin."
        ),
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ReferenceType.VALUE_1.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class RegionalizationDecision(Enum):
    """
    Вид требования: перемещение запрещено, перемещение разрешено или перемещение
    разрешено при обязательном соблюдении условий.

    Attributes:
        VALUE_1: Перемещение разрешено
        VALUE_2: Перемещение разрешено при обязательном соблюдении
            условий
        VALUE_3: Перемещение запрещено
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"

    __descriptions = {
        VALUE_1: "Перемещение разрешено",
        VALUE_2: "Перемещение разрешено при обязательном соблюдении условий",
        VALUE_3: "Перемещение запрещено",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        RegionalizationDecision.VALUE_1.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ResearchResult(Enum):
    """
    Результат лабораторного исследования/ВСЭ.

    Attributes:
        UNKNOWN: Результат неизвестен
        UNDEFINED: Результат невозможно определить (не нормируется)
        POSITIVE: Положительный результат
        NEGATIVE: Отрицательный результат
        UNFULFILLED: Не проводилось
        VSERAW: ВСЭ подвергнуто сырьё, из которого произведена продукция
        VSEFULL: Продукция подвергнута ВСЭ в полном объеме
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    UNFULFILLED = "UNFULFILLED"
    VSERAW = "VSERAW"
    VSEFULL = "VSEFULL"

    __descriptions = {
        UNKNOWN: "Результат неизвестен",
        UNDEFINED: "Результат невозможно определить (не нормируется)",
        POSITIVE: "Положительный результат",
        NEGATIVE: "Отрицательный результат",
        UNFULFILLED: "Не проводилось",
        VSERAW: "ВСЭ подвергнуто сырьё, из которого произведена продукция",
        VSEFULL: "Продукция подвергнута ВСЭ в полном объеме",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ResearchResult.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class TransportType(Enum):
    """
    Тип транспорта.

    Attributes:
        VALUE_1: Автомобильный
        VALUE_2: Железнодорожный
        VALUE_3: Авиатранспортный
        VALUE_4: Морской (контейнер)
        VALUE_5: Морской (трюм)
        VALUE_6: Речной (inland water)
        VALUE_7: Перегон (скота)
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

    __descriptions = {
        VALUE_1: "Автомобильный",
        VALUE_2: "Железнодорожный",
        VALUE_3: "Авиатранспортный",
        VALUE_4: "Морской (контейнер)",
        VALUE_5: "Морской (трюм)",
        VALUE_6: "Речной (inland water)",
        VALUE_7: "Перегон (скота)",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        TransportType.VALUE_1.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class TransportationStorageType(Enum):
    """
    Способ хранения при перевозке.

    Attributes:
        FROZEN: Замороженный тип перевозки
        CHILLED: Охлажденный тип перевозки
        COOLED: Охлаждаемый тип перевозки
        VENTILATED: Вентилируемый тип перевозки
    """

    FROZEN = "FROZEN"
    CHILLED = "CHILLED"
    COOLED = "COOLED"
    VENTILATED = "VENTILATED"

    __descriptions = {
        FROZEN: "Замороженный тип перевозки",
        CHILLED: "Охлажденный тип перевозки",
        COOLED: "Охлаждаемый тип перевозки",
        VENTILATED: "Вентилируемый тип перевозки",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        TransportationStorageType.FROZEN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VaccinationType(Enum):
    """
    Статус применения вакцины.

    Attributes:
        UNDEFINED: Неопределенный
        APPLIED: Вакцинация проводится
        UNVACCINATED: Вакцинация не проводится
    """

    UNDEFINED = "UNDEFINED"
    APPLIED = "APPLIED"
    UNVACCINATED = "UNVACCINATED"

    __descriptions = {
        UNDEFINED: "Неопределенный",
        APPLIED: "Вакцинация проводится",
        UNVACCINATED: "Вакцинация не проводится",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VaccinationType.UNDEFINED.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class CountryGuid(BaseModel):
    class Meta:
        name = "countryGuid"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class DistrictGuid(BaseModel):
    class Meta:
        name = "districtGuid"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class EnterpriseGuid(BaseModel):
    class Meta:
        name = "enterpriseGuid"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class GlobalId(BaseModel):
    class Meta:
        name = "globalID"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 13,
        },
    )


class LocalityGuid(BaseModel):
    class Meta:
        name = "localityGuid"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class ProductGuid(BaseModel):
    class Meta:
        name = "productGuid"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class RegionGuid(BaseModel):
    class Meta:
        name = "regionGuid"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class SubProductGuid(BaseModel):
    class Meta:
        name = "subProductGuid"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class AddressObjectView(GenericVersioningEntity):
    """
    Обертка для адресных объектов различного уровня (начиная с регионов страны,
    заканчивая улицами населенных пунктов)

    Attributes:
        name: Название объекта (не содержит название типа объекта).
        english_name: Английское название объекта.
        view: Представление объекта (обычно это название + название типа
            объекта).
        region_code: Код региона. Например, 33 - Владимирский регион
        type_value: Название типа адресного объекта (например, область,
            район или город).
        country_guid: Глобальный идентификатор страны, к которой
            относится данный объект.
        has_streets: Флаг, указывающий наличие улиц.
    """

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    english_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "englishName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    view: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    region_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "regionCode",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    country_guid: Optional[str] = field(
        default=None,
        metadata={
            "name": "countryGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )
    has_streets: Optional[bool] = field(
        default=None,
        metadata={
            "name": "hasStreets",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class AnimalDisease(GenericVersioningEntity):
    """
    Заболевание.

    Attributes:
        name: Наименование заболевания
    """

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )


class CountryInternalType(GenericVersioningEntity):
    """
    Тип, описывающий страну.

    Attributes:
        name: Название страны.
        full_name: Полное название страны, если имеется.
        english_name: Английское название страны.
        code: Двухбуквенный код страны, соответствующий стандарту ISO
            3166-1. В качестве кода используются буквы латинского
            алфавита.
        code3: Трехбуквенный код страны, соответсвующий стандарту ISO
            3166-1. В качестве кода используются буквы латинского
            алфавита.
    """

    class Meta:
        name = "Country"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    full_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fullName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    english_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "englishName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 2,
        },
    )
    code3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 3,
        },
    )


class EnterpriseActivity(GenericEntity):
    """
    Вид деятельности.
    """

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class FederalDistrict(GenericVersioningEntity):
    """
    Attributes:
        full_name: Полное название (содержить "федеральный округ").
        short_name: Короткое название (без "федеральный округ").
        abbreviation: Аббревиатура.
    """

    model_config = ConfigDict(defer_build=True)
    full_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fullName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    abbreviation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )


class IncorporationForm(GenericEntity):
    """
    Тип, описывающий элементы справочника ОПФ.
    """

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )


class Indicator(GenericVersioningEntity):
    """
    Показатель безопасности.

    Attributes:
        name: Наименование показателя
    """

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )


class PackingType(GenericVersioningEntity):
    """
    Вид упаковки.

    Attributes:
        global_id: Уникальный идентификатор упаковки.
        name: Наименование упаковки.
    """

    model_config = ConfigDict(defer_build=True)
    global_id: Optional[PackingCodeType] = field(
        default=None,
        metadata={
            "name": "globalID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )


class ProductMarks(BaseModel):
    """Тип, описывающий список маркировок продукции.

    Под маркировкой понимается всё, что может быть физически нанесено на
    упаковку или непосредственно на продукцию. Для каждой маркировки
    может быть указан её тип (см. атрибут class), который также может
    определять формат маркировки. Список возможных типов см. в
    перечислении dt:ProductMarkingClass.
    """

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 255,
        },
    )
    class_value: ProductMarkingClass = field(
        default=ProductMarkingClass.UNDEFINED,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )


class ProductInternalType(GenericVersioningEntity):
    """
    Тип, описывающий продукцию.

    Attributes:
        name: Название.
        code: Код ТНВЭД.
        english_name: Английское название.
        product_type: Тип продукции, которому относится данная
            продукция.
    """

    class Meta:
        name = "Product"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    english_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "englishName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    product_type: Optional[ProductTypeInternalType] = field(
        default=None,
        metadata={
            "name": "productType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class PurposeInternalType(GenericVersioningEntity):
    """
    Тип, описывающий назначение груза.

    Attributes:
        name: Наименование назначение.
        for_substandard: Назначение для некачественных грузов.
    """

    class Meta:
        name = "Purpose"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    for_substandard: Optional[bool] = field(
        default=None,
        metadata={
            "name": "forSubstandard",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class ResearchMethodInternalType(GenericVersioningEntity):
    """
    Метод исследования.

    Attributes:
        name: Наименование метода исследования
    """

    class Meta:
        name = "ResearchMethod"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )


class SubProductInternalType(GenericVersioningEntity):
    """
    Тип, описывающий вид продукции.

    Attributes:
        name: Название.
        code: Код ТНВЭД.
        english_name: Английское название.
        product_guid: Глобальный идентификатор продукции, которому
            относится данный вид продукции.
    """

    class Meta:
        name = "SubProduct"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    english_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "englishName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    product_guid: Optional[str] = field(
        default=None,
        metadata={
            "name": "productGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class UnitInternalType(GenericVersioningEntity):
    """
    Тип, описывающий единицу измерения.

    Attributes:
        name: Наименование единицы измерения.
        full_name: Полное наименование единицы измерения, если оно
            отличается от name.
        common_unit_guid: Глобальный идентификатор базовой единицы
            измерения. Например, для центнера, тонны, тыс.тонн базовой
            единицей измерения является килограмм.
        factor: Коэффициент относительно базовой единицы измерения.
            Например, для тонны этот коэффициент равен 1000, т.к. в 1
            тонне 1000 кг. Для килограмма этот коэффициент равен
            единице.
    """

    class Meta:
        name = "Unit"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    full_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fullName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    common_unit_guid: Optional[str] = field(
        default=None,
        metadata={
            "name": "commonUnitGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )
    factor: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class EnterpriseGroup(BaseModel):
    class Meta:
        name = "enterpriseGroup"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
    value: EnterpriseGroupInternalType = field(
        metadata={
            "required": True,
        }
    )


class ProductType(BaseModel):
    class Meta:
        name = "productType"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
    value: ProductTypeInternalType = field(
        metadata={
            "required": True,
        }
    )


class AnimalDiseaseList(EntityList):
    """
    Тип, описывающий список заболеваний.
    """

    model_config = ConfigDict(defer_build=True)
    disease: list[AnimalDisease] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class CountryListInternalType(EntityList):
    """
    Тип-обертка для списка стран.
    """

    class Meta:
        name = "CountryList"

    model_config = ConfigDict(defer_build=True)
    country: list[CountryInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class DistrictInternalType(AddressObjectView):
    """
    Тип района региона (обычно второй уровень в адресной структуре).

    Attributes:
        region_guid: Глобальный идентификатор рениона, к которому
            относится данный район.
    """

    class Meta:
        name = "District"

    model_config = ConfigDict(defer_build=True)
    region_guid: Optional[str] = field(
        default=None,
        metadata={
            "name": "regionGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class EnterpriseActivityList(EntityList):
    """
    Тип, описывающий список видов деятельности.
    """

    model_config = ConfigDict(defer_build=True)
    activity: list[EnterpriseActivity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class Locality(AddressObjectView):
    """
    Тип населенного пункта (город, поселок, деревня и прочие).

    Attributes:
        region_guid: Глобальный идентификатор рениона, к которому
            относится данный населенный пункт.
        district_guid: Глобальный идентификатор района, к которому
            относится данный населенный пункт.
        city_guid: Глобальный идентификатор города, к которому относится
            данный населенный пункт.
    """

    model_config = ConfigDict(defer_build=True)
    region_guid: Optional[str] = field(
        default=None,
        metadata={
            "name": "regionGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )
    district_guid: Optional[str] = field(
        default=None,
        metadata={
            "name": "districtGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )
    city_guid: Optional[str] = field(
        default=None,
        metadata={
            "name": "cityGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class Package(BaseModel):
    """Упаковка партии продукции.

    Поддерживается указание многоуровневой упаковки и маркировки партии
    продукции. Всего предусмотрено шесть уровней упаковки (см. тип
    dt:PackageLevelType). Количество единиц упаковки и маркировка партии
    указывается для каждой упаковки конкретного уровня отдельно. На
    каждом уровне может быть произвольное количество типов упаковки, в
    том числе и ни одного, т.е. какого-то уровня упаковки в описании
    партии продукции может не быть. Если уровень упаковки однозначно
    определить не получается, например, груз перевозится в
    потребительской упаковке, т.е. эта упаковка в то же время может
    считаться и транспортной, то рекомендуется указывать наименьший
    уровень, т.е. для примера выше, упаковка будет отнесена к
    потребительскому уровню. Уровнь и тип упаковки обязательны для
    указания. Количество единиц упаковки может быть не указано. В то же
    время, для корректного оформления ветеринарного сертификата,
    рекомендуется указывать количество единиц упаковки, в которой
    перевозится продукция. Важно, что количество мест в транспортной
    партии будет определено как сумма всех упаковок на
    последнем/максимальном уровне, который указан в описании партии.
    Примеры описания упаковки для различных типов продукции и вариантов
    перевозки представлены в справочной системе.

    Attributes:
        level: Уровень упаковки
        packing_type: Тип упаковки
        quantity: Количество единиц упаковки.
        product_marks: Маркировка партии продукции
    """

    model_config = ConfigDict(defer_build=True)
    level: PackageLevelType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    packing_type: PackingType = field(
        metadata={
            "name": "packingType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    product_marks: list[ProductMarks] = field(
        default_factory=list,
        metadata={
            "name": "productMarks",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class Packaging(BaseModel):
    """
    Тип, описывающий вариант фасовки продукции.

    Attributes:
        packaging_type: Тип упаковки.
        quantity: Количество единиц упаковки.
        volume: Объём единицы упаковки товара.
        unit: Единица измерения объёма единицы упаковки товара.
    """

    model_config = ConfigDict(defer_build=True)
    packaging_type: PackingType = field(
        metadata={
            "name": "packagingType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    volume: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "fraction_digits": 6,
        },
    )
    unit: Optional[UnitInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class ProductListInternalType(EntityList):
    """
    Тип, описывающий список продукции.
    """

    class Meta:
        name = "ProductList"

    model_config = ConfigDict(defer_build=True)
    product: list[ProductInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class PurposeListInternalType(EntityList):
    """
    Тип, описывающий список целей.
    """

    class Meta:
        name = "PurposeList"

    model_config = ConfigDict(defer_build=True)
    purpose: list[PurposeInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class RegionInternalType(AddressObjectView):
    """
    Тип региона страны (обычно первый уровень в адресной структуре).
    """

    class Meta:
        name = "Region"

    model_config = ConfigDict(defer_build=True)


class RegionalizationCondition(GenericVersioningEntity):
    """
    Условие регионализации, соблюдаемое при перевозке груза.

    Attributes:
        reference_number: Номер условия
        text: Формулировка условия
        strict: Обязательность соблюдения условия
        related_disease: Заболевание, к которому относится данное
            условие
    """

    model_config = ConfigDict(defer_build=True)
    reference_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "referenceNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 100,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    strict: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    related_disease: list[AnimalDisease] = field(
        default_factory=list,
        metadata={
            "name": "relatedDisease",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class RegionalizationStatus(BaseModel):
    """
    Статус региона в соответствии с регионализацией.

    Attributes:
        related_disease: Заболевание, по которому назначен статус
        prosperity:
        vaccination:
    """

    model_config = ConfigDict(defer_build=True)
    related_disease: AnimalDisease = field(
        metadata={
            "name": "relatedDisease",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    prosperity: ProsperityType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    vaccination: VaccinationType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class ResearchMethodListInternalType(EntityList):
    """
    Тип, описывающий список методов исследований.
    """

    class Meta:
        name = "ResearchMethodList"

    model_config = ConfigDict(defer_build=True)
    method: list[ResearchMethodInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class Street(AddressObjectView):
    """
    Тип улицы.

    Attributes:
        locality_guid: Глобальный идентификатор насленного пункта, к
            которому относится данная улица.
    """

    model_config = ConfigDict(defer_build=True)
    locality_guid: Optional[str] = field(
        default=None,
        metadata={
            "name": "localityGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )


class SubProductListInternalType(EntityList):
    """
    Тип, описывающий список видов продукции.
    """

    class Meta:
        name = "SubProductList"

    model_config = ConfigDict(defer_build=True)
    sub_product: list[SubProductInternalType] = field(
        default_factory=list,
        metadata={
            "name": "subProduct",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class UnitListInternalType(EntityList):
    """
    Тип, описывающий список единиц измерений.
    """

    class Meta:
        name = "UnitList"

    model_config = ConfigDict(defer_build=True)
    unit: list[UnitInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class CargoType(SubProductInternalType):
    class Meta:
        name = "cargoType"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class Country(CountryInternalType):
    class Meta:
        name = "country"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class Disease(AnimalDisease):
    class Meta:
        name = "disease"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class Product(ProductInternalType):
    class Meta:
        name = "product"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class Purpose(PurposeInternalType):
    class Meta:
        name = "purpose"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class ResearchMethod(ResearchMethodInternalType):
    class Meta:
        name = "researchMethod"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class SubProduct(SubProductInternalType):
    class Meta:
        name = "subProduct"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class Unit(UnitInternalType):
    class Meta:
        name = "unit"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class Address(BaseModel):
    model_config = ConfigDict(defer_build=True)
    country: Optional[CountryInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    federal_district: Optional[FederalDistrict] = field(
        default=None,
        metadata={
            "name": "federalDistrict",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    region: Optional[RegionInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    district: Optional[DistrictInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    locality: Optional[Locality] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    sub_locality: Optional[Locality] = field(
        default=None,
        metadata={
            "name": "subLocality",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    street: Optional[Street] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    house: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    building: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    post_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "postIndex",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    post_box: Optional[str] = field(
        default=None,
        metadata={
            "name": "postBox",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    additional_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    address_view: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressView",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    en_address_view: Optional[str] = field(
        default=None,
        metadata={
            "name": "enAddressView",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class DistrictListInternalType(EntityList):
    """
    Тип-обертка для списка районов.
    """

    class Meta:
        name = "DistrictList"

    model_config = ConfigDict(defer_build=True)
    district: list[DistrictInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class LocalityListInternalType(EntityList):
    """
    Тип-обертка для списка населенных пунктов.
    """

    class Meta:
        name = "LocalityList"

    model_config = ConfigDict(defer_build=True)
    locality: list[Locality] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class PackageList(BaseModel):
    """
    Список физической упаковки.

    Attributes:
        package: Описание упаковки
    """

    model_config = ConfigDict(defer_build=True)
    package: list[Package] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class RegionListInternalType(EntityList):
    """
    Тип-обертка для списка регионов.
    """

    class Meta:
        name = "RegionList"

    model_config = ConfigDict(defer_build=True)
    region: list[RegionInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class RegionalizationConditionGroup(BaseModel):
    """Группа условий регионализации, соблюдаемых при перевозке груза.

    Считается, что группа условий соблюдается (выполняется), если
    соблюдается каждое условие, входящее в группу.
    """

    model_config = ConfigDict(defer_build=True)
    condition: list[RegionalizationCondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class RegionalizationConditionList(EntityList):
    """
    Тип, описывающий список условий перемещения.
    """

    model_config = ConfigDict(defer_build=True)
    condition: list[RegionalizationCondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class StreetListInternalType(EntityList):
    """
    Тип-обертка для списка улиц.
    """

    class Meta:
        name = "StreetList"

    model_config = ConfigDict(defer_build=True)
    street: list[Street] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class CountryList(CountryListInternalType):
    class Meta:
        name = "countryList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class DiseaseList(AnimalDiseaseList):
    class Meta:
        name = "diseaseList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class District(DistrictInternalType):
    class Meta:
        name = "district"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class ProductList(ProductListInternalType):
    class Meta:
        name = "productList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class PurposeList(PurposeListInternalType):
    class Meta:
        name = "purposeList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class Region(RegionInternalType):
    class Meta:
        name = "region"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class ResearchMethodList(ResearchMethodListInternalType):
    class Meta:
        name = "researchMethodList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class SubProductList(SubProductListInternalType):
    class Meta:
        name = "subProductList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class UnitList(UnitListInternalType):
    class Meta:
        name = "unitList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class Area(Address):
    """
    Территория: регион, район, город или область, ограниченная полигоном.
    """

    model_config = ConfigDict(defer_build=True)


class EnterpriseInternalType(GenericVersioningEntity):
    """
    Тип, описывающий предприятие.

    Attributes:
        name: Название предприятия.
        english_name: Название предприятия на английском языке.
        type_value: Тип российского предприятия.
        number_list: Список номеров предприятия.
        address: Адрес предприятия.
        activity_list: Деятельность, осуществляемая предприятием.
        owner: ХС-владелец.
        official_registration: Факт постановки на учёт в налоговом
            органе.
        registry_status: Статус предприятия в реестре ИС Цербер.
    """

    class Meta:
        name = "Enterprise"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    english_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "englishName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    type_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    number_list: Optional[EnterpriseNumberList] = field(
        default=None,
        metadata={
            "name": "numberList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    activity_list: Optional[EnterpriseActivityList] = field(
        default=None,
        metadata={
            "name": "activityList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    owner: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    official_registration: list[EnterpriseOfficialRegistration] = field(
        default_factory=list,
        metadata={
            "name": "officialRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    registry_status: Optional[EnterpriseStatus] = field(
        default=None,
        metadata={
            "name": "registryStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class Location(BaseModel):
    """
    Тип, описывающий вариант фасовки продукции.

    Attributes:
        name: Название пункта перегрузки.
        address: Название пункта перегрузки.
    """

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class Organization(BaseModel):
    """Организация, в т.ч.

    учреждения структуры Россельхознадзора, ветеринарных управлений
    субъектов РФ и т.д.

    Attributes:
        id: Идентификатор учреждения
        name: Наименование учреждения
        address: Адрес учреждения
    """

    model_config = ConfigDict(defer_build=True)
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 100,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class RegionalizationRequirement(BaseModel):
    """
    Требование к перемещению партии в отношении к определенному заболеванию.

    Attributes:
        related_disease: Заболевание, к которому относится данное
            требование
        type_value: Вид требования: перемещение запрещено, перемещение
            разрешено или перемещение разрешено при обязательном
            соблюдении условий.
        condition_group: Группа условий регионализации, соблюдаемых при
            перевозке продукции. Имеет смысл, если тип требования `type`
            имеет значение 3 (перемещение разрешено при обязательном
            соблюдении условий). В этом случае требование считается
            выполненным, если выполнена одна из альтернативных групп
            условий `conditionGroup`. См. условие выполнения группы в
            описании типа `dt:RegionalizationConditionGroup`.
    """

    model_config = ConfigDict(defer_build=True)
    related_disease: Optional[AnimalDisease] = field(
        default=None,
        metadata={
            "name": "relatedDisease",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    type_value: RegionalizationDecision = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    condition_group: list[RegionalizationConditionGroup] = field(
        default_factory=list,
        metadata={
            "name": "conditionGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class DistrictList(DistrictListInternalType):
    class Meta:
        name = "districtList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class LocalityList(LocalityListInternalType):
    class Meta:
        name = "localityList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class R13NConditionList(RegionalizationConditionList):
    class Meta:
        name = "r13nConditionList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class RegionList(RegionListInternalType):
    class Meta:
        name = "regionList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class StreetList(StreetListInternalType):
    class Meta:
        name = "streetList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class BusinessEntityActivityLocation(BaseModel):
    class Meta:
        global_type = False

    model_config = ConfigDict(defer_build=True)
    global_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "globalID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "length": 13,
        },
    )
    enterprise: EnterpriseInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class EnterpriseListInternalType(EntityList):
    """
    Тип, описывающий список предприятий.
    """

    class Meta:
        name = "EnterpriseList"

    model_config = ConfigDict(defer_build=True)
    enterprise: list[EnterpriseInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class ProducerInternalType(BaseModel):
    """
    Производитель продукции.
    """

    class Meta:
        name = "Producer"

    model_config = ConfigDict(defer_build=True)
    enterprise: EnterpriseInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    role: Optional[EnterpriseRole] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class ProductItemProducing(BaseModel):
    """
    Тип, описывающий выпуск номенклатурной позиции на предприятии.

    Attributes:
        location: Площадка, осуществляющая выпуск продукции.
    """

    model_config = ConfigDict(defer_build=True)
    location: EnterpriseInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class RegionalizationRegionStatus(GenericVersioningEntity):
    """
    Статус регионализации.

    Attributes:
        reference_number: Номер статуса региона в реестре.
        r13n_zone: Территория/регион
        excluded_r13n_zone: Территория/регион внутри `r13Zone` с
            отличным (другим) статусом регионализации.
        r13n_status: Статус регионализации
    """

    model_config = ConfigDict(defer_build=True)
    reference_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "referenceNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 100,
        },
    )
    r13n_zone: Optional[Area] = field(
        default=None,
        metadata={
            "name": "r13nZone",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    excluded_r13n_zone: list[Area] = field(
        default_factory=list,
        metadata={
            "name": "excludedR13nZone",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    r13n_status: list[RegionalizationStatus] = field(
        default_factory=list,
        metadata={
            "name": "r13nStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class RegionalizationShippingRule(GenericVersioningEntity):
    """
    Правило перемещения партии согласно регионализации.

    Attributes:
        reference_number: Номер правила перевозки в реестре.
        from_r13n_status: Статус территории, откуда партия отправляется
            (место отправления), согласно регионализации.
        to_r13n_status: Статус территории, куда партия направляется
            (место назначения), согласно регионализации.
        cargo_type: Ветеринарная категория груза, на которую
            распространяется правило перемещения.
        decision: Решение о возможности перемещения груза: перемещение
            запрещено, перемещение разрешено или перемещение разрешено
            при обязательном соблюдении условий.
        requirement: Требование к перемещению партии в отношении к
            определенному заболеванию.
    """

    model_config = ConfigDict(defer_build=True)
    reference_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "referenceNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 100,
        },
    )
    from_r13n_status: Optional[RegionalizationStatus] = field(
        default=None,
        metadata={
            "name": "fromR13nStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    to_r13n_status: Optional[RegionalizationStatus] = field(
        default=None,
        metadata={
            "name": "toR13nStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    cargo_type: list[SubProductInternalType] = field(
        default_factory=list,
        metadata={
            "name": "cargoType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    decision: Optional[RegionalizationDecision] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    requirement: list[RegionalizationRequirement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class Enterprise(EnterpriseInternalType):
    class Meta:
        name = "enterprise"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class R13NZone(Area):
    class Meta:
        name = "r13nZone"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class BusinessEntityInternalType(GenericVersioningEntity):
    """
    Тип, описывающий ХС.

    Attributes:
        type_value: Тип ХС
        name: Наименование хозяйствующего субъекта без ОПФ.
        incorporation_form: Организационно-правовая форма.
        full_name: Полное наименование хозяйствующего субъекта.
        fio: ФИО хозяйствующего субъекта.
        passport: Паспортные данные.
        inn: Идентификационный номер ХС (ИНН, БИН или ИИН).
        kpp: КПП субъекта.
        ogrn: ОГРН(ИП) субъекта.
        juridical_address: Юридический адрес или адрес регистрации ХС.
        activity_location: Место осуществления деятельности.
    """

    class Meta:
        name = "BusinessEntity"

    model_config = ConfigDict(defer_build=True)
    type_value: Optional[BusinessEntityType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    incorporation_form: Optional[IncorporationForm] = field(
        default=None,
        metadata={
            "name": "incorporationForm",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    full_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fullName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    fio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    passport: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    inn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    kpp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    ogrn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    juridical_address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "juridicalAddress",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    activity_location: list[BusinessEntityActivityLocation] = field(
        default_factory=list,
        metadata={
            "name": "activityLocation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class ProducerList(BaseModel):
    """
    Тип, описывающий список производителей продукции.
    """

    model_config = ConfigDict(defer_build=True)
    producer: list[ProducerInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class RegionalizationRegionStatusList(EntityList):
    """
    Тип, описывающий список статусов региона (регионализация).
    """

    model_config = ConfigDict(defer_build=True)
    status: list[RegionalizationRegionStatus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class RegionalizationShippingRuleList(EntityList):
    """
    Тип, описывающий список правил перемещения (регионализация).
    """

    model_config = ConfigDict(defer_build=True)
    rule: list[RegionalizationShippingRule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class EnterpriseList(EnterpriseListInternalType):
    class Meta:
        name = "enterpriseList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class BusinessEntityListInternalType(EntityList):
    """
    Тип, описывающий список ХС.
    """

    class Meta:
        name = "BusinessEntityList"

    model_config = ConfigDict(defer_build=True)
    business_entity: list[BusinessEntityInternalType] = field(
        default_factory=list,
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class BusinessMemberInternalType(BaseModel):
    """
    Тип, описывающий бизнес-сторону.

    Attributes:
        business_entity: Хозяйствующий субъект
        enterprise: Предприятие (площадка)
        global_id: Global Location Number - уникальный номер площадки
            хозяйствующего субъекта, на которой он осуществляет
            деятельность. См. http://www.gs1.org/gln.
    """

    class Meta:
        name = "BusinessMember"

    model_config = ConfigDict(defer_build=True)
    business_entity: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    enterprise: Optional[EnterpriseInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    global_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "globalID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "length": 13,
        },
    )


class EnterpriseOfficialRegistration(BaseModel):
    """
    Факт постановки предприятия на учёт в налоговом органе.

    Attributes:
        id: Государственный номер регистрации ФНС.
        business_entity: Хозяйствующий субъект, поставивший площадку на
            учёт в налоговом органе. Для элемента могут быть указаны
            атрибуты: UUID, GUID, (NAME + INN), (NAME + OGRN).
        kpp: Код причины постановки на учёт (КПП).
    """

    model_config = ConfigDict(defer_build=True)
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    business_entity: BusinessEntityInternalType = field(
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    kpp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
            "max_length": 255,
        }
    )


class ProductItemInternalType(GenericVersioningEntity):
    """Тип, описывающий cведения о наименовании продукции в соответствии с
    номенклатурой производителя.

    ProductItem – наименование продукции, выпускаемое ХС-производителем
    (BusinessEntity) на одной или нескольких площадках (Enterprise). Для
    ProductItem должен быть указан ХС-собственник торговой марки (ТМ).
    По умолчанию, им является ХС-производитель. Если одно наименование
    продукции (ТМ) производится одним ХС-производителем на нескольких
    площадках, в реестре должна быть зарегистрирована строго одна
    запись. Если одно наименование продукции (ТМ), принадлежащее одному
    ХС-собственнику ТМ, производится несколькими ХС-производителями, в
    реестре должно быть зарегистрировано несколько записей по одной на
    каждого ХС-производителя.

    Attributes:
        global_id: Global Trade Identification Number (GTIN) -
            уникальный идентификационный номер продукции производителя.
            В отличие от поля code GTIN уникален для продукции всех
            производителей. Уникальность обеспечивается использованием
            префикса компании-производителя в составе GTIN. См.
            http://www.gs1.org/gtin
        name: Наименование продукции.
        code: Артикул (код) продукции в соответствии с внутренним
            кодификатором производителя. Артикул продукции должен быть
            уникальным в пределах одного производителя.
        product_type: Тип продукции.
        product: Продукция.
        sub_product: Вид продукции.
        corresponds_to_gost: Соответствует ли ГОСТу.
        gost: ГОСТ.
        producer: ХС-производитель продукции.
        tm_owner: ХС-собственник торговой марки.
        producing: Список площадок, на которых выпускается данная
            продукция.
        packaging: Фасовка.
        is_public: Позиция справочника доступна для просмотра другим
            участникам.
    """

    class Meta:
        name = "ProductItem"

    model_config = ConfigDict(defer_build=True)
    global_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "globalID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "min_length": 8,
            "max_length": 14,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    product_type: Optional[ProductTypeInternalType] = field(
        default=None,
        metadata={
            "name": "productType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    product: Optional[ProductInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    sub_product: Optional[SubProductInternalType] = field(
        default=None,
        metadata={
            "name": "subProduct",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    corresponds_to_gost: Optional[bool] = field(
        default=None,
        metadata={
            "name": "correspondsToGost",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    gost: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    producer: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    tm_owner: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "name": "tmOwner",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    producing: list[ProductItemProducing] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    packaging: Optional[Packaging] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    is_public: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPublic",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class BusinessEntity(BusinessEntityInternalType):
    class Meta:
        name = "businessEntity"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class R13NRegionStatusList(RegionalizationRegionStatusList):
    class Meta:
        name = "r13nRegionStatusList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class R13NShippingRuleList(RegionalizationShippingRuleList):
    class Meta:
        name = "r13nShippingRuleList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class ActivityLocationListInternalType(EntityList):
    """
    Тип, описывающий список методов исследований.
    """

    class Meta:
        name = "ActivityLocationList"

    model_config = ConfigDict(defer_build=True)
    location: list[BusinessMemberInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class MedicinalDrug(BaseModel):
    """
    Препарат/вакцина.

    Attributes:
        id: Идентификационный (уникальный) номер препарата
        name: Наименование препарата
        series: Номер серии препарата/вакцины
        producer: Производитель препарата
    """

    model_config = ConfigDict(defer_build=True)
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 100,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    series: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    producer: Optional[BusinessMemberInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class ProductItemListInternalType(EntityList):
    """
    Тип, описывающий список наименование продукции.
    """

    class Meta:
        name = "ProductItemList"

    model_config = ConfigDict(defer_build=True)
    product_item: list[ProductItemInternalType] = field(
        default_factory=list,
        metadata={
            "name": "productItem",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class BusinessEntityList(BusinessEntityListInternalType):
    class Meta:
        name = "businessEntityList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class BusinessMember(BusinessMemberInternalType):
    class Meta:
        name = "businessMember"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class Producer(BusinessMemberInternalType):
    class Meta:
        name = "producer"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class ProductItem(ProductItemInternalType):
    class Meta:
        name = "productItem"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class ActivityLocationList(ActivityLocationListInternalType):
    class Meta:
        name = "activityLocationList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class ProductItemList(ProductItemListInternalType):
    class Meta:
        name = "productItemList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
