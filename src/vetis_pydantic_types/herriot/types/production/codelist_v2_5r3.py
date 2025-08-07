from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/codelist/v2"


class AnimalBreedingValueTypeContentType(Enum):
    """
    Тип.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        BREEDING: Племенное
        NON_BREEDING: Неплеменное
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    BREEDING = "BREEDING"
    NON_BREEDING = "NON_BREEDING"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        BREEDING: "Племенное",
        NON_BREEDING: "Неплеменное",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalBreedingValueTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalGenderContentType(Enum):
    """
    Тип.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        MALE: Самец
        FEMALE: Самка
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    MALE = "MALE"
    FEMALE = "FEMALE"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        MALE: "Самец",
        FEMALE: "Самка",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalGenderContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalIdformatContentType(Enum):
    """
    Тип.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        UNMM: Формат Уникального номера средства маркирования (УНСМ) в
            соответствии с утвержденными Правилами маркирования животных
        UNLA: Формат Уникального номера животного (УНЖ) в соответствии с
            утвержденными Правилами маркирования животных
        ISO: Формат номера в соответствии с международным форматом ISO
        OTHER: Другой формат номера
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    UNMM = "UNMM"
    UNLA = "UNLA"
    ISO = "ISO"
    OTHER = "OTHER"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        UNMM: (
            "Формат Уникального номера средства маркирования (УНСМ)\nв соответствии с "
            "утвержденными Правилами маркирования животных"
        ),
        UNLA: (
            "Формат Уникального номера животного (УНЖ)\nв соответствии с утвержденными"
            " Правилами маркирования животных"
        ),
        ISO: "Формат номера в соответствии с международным форматом ISO",
        OTHER: "Другой формат номера",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalIDFormatContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalIdentificationEventTypeContentType(Enum):
    """
    Тип.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        BIRTH: Рождение
        IMPORT: Ввоз на территорию РФ
        RELABELING: Повторное маркирование (замена средства
            маркирования)
        OTHER: Иное событие идентификации животного
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    BIRTH = "BIRTH"
    IMPORT = "IMPORT"
    RELABELING = "RELABELING"
    OTHER = "OTHER"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        BIRTH: "Рождение",
        IMPORT: "Ввоз на территорию РФ",
        RELABELING: "Повторное маркирование (замена средства маркирования)",
        OTHER: "Иное событие идентификации животного",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalIdentificationEventTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalIdentityStatusContentType(Enum):
    """
    Статус идентификации (маркировки животного)

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        PREPARING: В обработке
        ACTIVE: Действующий, действительна
        TERMINATED: Недействующий, завершена
        WITHDRAWN: Аннулирована
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    PREPARING = "PREPARING"
    ACTIVE = "ACTIVE"
    TERMINATED = "TERMINATED"
    WITHDRAWN = "WITHDRAWN"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        PREPARING: "В обработке",
        ACTIVE: "Действующий, действительна",
        TERMINATED: "Недействующий, завершена",
        WITHDRAWN: "Аннулирована",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalIdentityStatusContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalIdentityTypeContentType(Enum):
    """
    Тип.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        INDIVIDUAL: Индивидуальная идентификация
        GROUP: Групповая идентификация
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    INDIVIDUAL = "INDIVIDUAL"
    GROUP = "GROUP"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        INDIVIDUAL: "Индивидуальная идентификация",
        GROUP: "Групповая идентификация",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalIdentityTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalLabelTypeContentType(Enum):
    """
    Тип.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        MAIN: Основное средство маркирования
        ADDITIONAL: Дополнительное средство маркирования
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    MAIN = "MAIN"
    ADDITIONAL = "ADDITIONAL"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        MAIN: "Основное средство маркирования",
        ADDITIONAL: "Дополнительное средство маркирования",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalLabelTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalLifecycleEventReasonContentType(Enum):
    """
    Тип.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        WITHOUT_DISEASES: Падёж/убой животного, у которого не выявлено
            заразных или незаразных болезней
        IDENTIFIED_CONTAGIOUS_DISEASE: Падёж/убой животного, у которого
            выявлена заразная болезнь
        IDENTIFIED_NON_CONTAGIOUS_DISEASE: Падёж/убой животного, у
            которого выявлена незаразная болезнь
        DISEASE_ERADICATION: Убой здорового животного в рамках
            ликвидации болезни
        RESEARCH_OBJECTIVES: Убой животного в научно-исследовательских
            целях
        USELESSNESS: Убой животного за ненадобностью в будущем
            (лабораторные животные, непродуктивные и т.п.)
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    WITHOUT_DISEASES = "WITHOUT_DISEASES"
    IDENTIFIED_CONTAGIOUS_DISEASE = "IDENTIFIED_CONTAGIOUS_DISEASE"
    IDENTIFIED_NON_CONTAGIOUS_DISEASE = "IDENTIFIED_NON_CONTAGIOUS_DISEASE"
    DISEASE_ERADICATION = "DISEASE_ERADICATION"
    RESEARCH_OBJECTIVES = "RESEARCH_OBJECTIVES"
    USELESSNESS = "USELESSNESS"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        WITHOUT_DISEASES: (
            "Падёж/убой животного, у которого не выявлено заразных или незаразных "
            "болезней"
        ),
        IDENTIFIED_CONTAGIOUS_DISEASE: "Падёж/убой животного, у которого выявлена заразная болезнь",
        IDENTIFIED_NON_CONTAGIOUS_DISEASE: "Падёж/убой животного, у которого выявлена незаразная болезнь",
        DISEASE_ERADICATION: "Убой здорового животного в рамках ликвидации болезни",
        RESEARCH_OBJECTIVES: "Убой животного в научно-исследовательских целях",
        USELESSNESS: (
            "Убой животного за ненадобностью в будущем (лабораторные животные, "
            "непродуктивные и т.п.)"
        ),
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalLifecycleEventReasonContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalMarkingEventReasonContentType(Enum):
    """
    Тип.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        TERMINATED: Прекращение экплуатации средства маркирования по
            причине выбытия животного
        LOSS: Средство маркирования утеряно
        BROKEN: Средство маркирования повреждено (сломано)
        EXPIRATION: Истёк срок действия средства маркирования
        REMOVED: Средство маркирования удалено владельцем животного
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    TERMINATED = "TERMINATED"
    LOSS = "LOSS"
    BROKEN = "BROKEN"
    EXPIRATION = "EXPIRATION"
    REMOVED = "REMOVED"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        TERMINATED: "Прекращение экплуатации средства маркирования по причине выбытия животного",
        LOSS: "Средство маркирования утеряно",
        BROKEN: "Средство маркирования повреждено (сломано)",
        EXPIRATION: "Истёк срок действия средства маркирования",
        REMOVED: "Средство маркирования удалено владельцем животного",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalMarkingEventReasonContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalMarkingMeansTypeContentType(Enum):
    """
    Тип.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        LABEL: Бирка
        MICROCHIP: Вживляемый микрочип
        BRAND: Тавро/Клеймо
        TATTOO: Татуировка
        RING: Кольцо
        ELECTRONIC_RING: Электронное кольцо
        ELECTRONIC_COLLAR: Электронный ошейник
        COLLAR: Ошейник
        RESPONDER: Респондер
        TRANSPONDER: Транспондер
        BOLUS: Болюс
        NAMEPLATE: Табло
        WING_TAG: Крыло-метка
        ELECTRONIC_WING_TAG: Электронное крыло-метка
        ELECTRONIC_TAG: Электронная метка
        TISSUE_SECTION: Вырез тканей
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    LABEL = "LABEL"
    MICROCHIP = "MICROCHIP"
    BRAND = "BRAND"
    TATTOO = "TATTOO"
    RING = "RING"
    ELECTRONIC_RING = "ELECTRONIC_RING"
    ELECTRONIC_COLLAR = "ELECTRONIC_COLLAR"
    COLLAR = "COLLAR"
    RESPONDER = "RESPONDER"
    TRANSPONDER = "TRANSPONDER"
    BOLUS = "BOLUS"
    NAMEPLATE = "NAMEPLATE"
    WING_TAG = "WING_TAG"
    ELECTRONIC_WING_TAG = "ELECTRONIC_WING_TAG"
    ELECTRONIC_TAG = "ELECTRONIC_TAG"
    TISSUE_SECTION = "TISSUE_SECTION"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        LABEL: "Бирка",
        MICROCHIP: "Вживляемый микрочип",
        BRAND: "Тавро/Клеймо",
        TATTOO: "Татуировка",
        RING: "Кольцо",
        ELECTRONIC_RING: "Электронное кольцо",
        ELECTRONIC_COLLAR: "Электронный ошейник",
        COLLAR: "Ошейник",
        RESPONDER: "Респондер",
        TRANSPONDER: "Транспондер",
        BOLUS: "Болюс",
        NAMEPLATE: "Табло",
        WING_TAG: "Крыло-метка",
        ELECTRONIC_WING_TAG: "Электронное крыло-метка",
        ELECTRONIC_TAG: "Электронная метка",
        TISSUE_SECTION: "Вырез тканей",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalMarkingMeansTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalMedicationEventReasonContentType(Enum):
    """
    Основания применения лекарственных препаратов в отношении животных.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        PLANNED: Плановое применение
        FORCED: Вынужденное применение
        PREVENTIVE: Профилактическое применение
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    PLANNED = "PLANNED"
    FORCED = "FORCED"
    PREVENTIVE = "PREVENTIVE"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        PLANNED: "Плановое применение",
        FORCED: "Вынужденное применение",
        PREVENTIVE: "Профилактическое применение",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalMedicationEventReasonContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalPlaceKindContentType(Enum):
    """
    Вид размещения живых животных.

    Attributes:
        UNKNOWN: Неизвестный вид
        UNDEFINED: Не определено
        TEMPORARY_KEEPING: Временная передержка
        CULTIVATION: Выращивание
        INCUBATION: Инкубирование
        QUARANTINE: Карантинирование
        KEEPING: Размещение
        SLAUGHTER: Убой
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    TEMPORARY_KEEPING = "TEMPORARY_KEEPING"
    CULTIVATION = "CULTIVATION"
    INCUBATION = "INCUBATION"
    QUARANTINE = "QUARANTINE"
    KEEPING = "KEEPING"
    SLAUGHTER = "SLAUGHTER"

    __descriptions = {
        UNKNOWN: "Неизвестный вид",
        UNDEFINED: "Не определено",
        TEMPORARY_KEEPING: "Временная передержка",
        CULTIVATION: "Выращивание",
        INCUBATION: "Инкубирование",
        QUARANTINE: "Карантинирование",
        KEEPING: "Размещение",
        SLAUGHTER: "Убой",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalPlaceKindContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalRegistrationStatusContentType(Enum):
    """
    Статус регистрации животного (учётной карточки)

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        PREPARING: В обработке. Сведения о животном приняты на
            регистрацию. Изменение сведений не допускается до окончания
            процедуры регистрации.
        ACTIVE: Действующий, действительна. Сведения о животном
            зарегистрированы. Допускается изменение сведений о животном
        RELOCATING: В состоянии перемещения. Животное перемещается на
            другой поднадзорный объект (физическое перемещение, смена
            собственности без перемещения, смена собственности с
            перемещением). Изменение сведений о животном не допускаются.
        SUSPENDED: Приостановлена регистрация. Изменение сведений о
            животном не допускается.
        TERMINATED: Недействующий, регистрация завершена (например, по
            причине выбытия животного). Изменение сведений о животном не
            допускается.
        WITHDRAWN: Аннулирована. Регистрация животного аннулирована
            (например, вследствие технической ошибки при внесении
            сведений). Изменение сведений о животном не допускается.
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    PREPARING = "PREPARING"
    ACTIVE = "ACTIVE"
    RELOCATING = "RELOCATING"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"
    WITHDRAWN = "WITHDRAWN"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        PREPARING: (
            "В обработке. Сведения о животном приняты на регистрацию.\nИзменение "
            "сведений не допускается до окончания процедуры регистрации."
        ),
        ACTIVE: (
            "Действующий, действительна. Сведения о животном "
            "зарегистрированы.\nДопускается изменение сведений о животном"
        ),
        RELOCATING: (
            "В состоянии перемещения. Животное перемещается на другой поднадзорный "
            "объект\n(физическое перемещение, смена собственности без перемещения, "
            "смена собственности с перемещением).\nИзменение сведений о животном не "
            "допускаются."
        ),
        SUSPENDED: "Приостановлена регистрация.\nИзменение сведений о животном не допускается.",
        TERMINATED: (
            "Недействующий, регистрация завершена (например, по причине выбытия "
            "животного).\nИзменение сведений о животном не допускается."
        ),
        WITHDRAWN: (
            "Аннулирована. Регистрация животного аннулирована\n(например, вследствие "
            "технической ошибки при внесении сведений).\nИзменение сведений о животном"
            " не допускается."
        ),
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalRegistrationStatusContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class AnimalSpentPeriodContentType(Enum):
    """
    Сколько времени животные находились на территории ТС.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        FROM_BIRTH: Животные находились на территории ТС с рождения
        NOT_LESS_SIX_MONTHS: Животные находились на территории ТС не
            менее 6 месяцев
        IN_MONTHS: Животные находились на территории ТС указанное кол-во
            месяцев
        ZERO: Животные не находились на территории ТС
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    FROM_BIRTH = "FROM_BIRTH"
    NOT_LESS_SIX_MONTHS = "NOT_LESS_SIX_MONTHS"
    IN_MONTHS = "IN_MONTHS"
    ZERO = "ZERO"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        FROM_BIRTH: "Животные находились на территории ТС с рождения",
        NOT_LESS_SIX_MONTHS: "Животные находились на территории ТС не менее 6 месяцев",
        IN_MONTHS: "Животные находились на территории ТС указанное кол-во месяцев",
        ZERO: "Животные не находились на территории ТС",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        AnimalSpentPeriodContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ApprovalStatusTypeContentType(Enum):
    """
    Статус аттестации предприятия.

    Attributes:
        UNKNOWN: Неизвестный статус
        UNDEFINED: Статус не определен
        WITHOUT_RESTRICTION: Без ограничений
        ENHANCED_MONITORING: Усиленный лабораторный контроль
        SPECIFIC_REQUIREMENTS: Специальные требования
        CAUTION: Предупреждение
        TEMPORARY_RESTRICTIONS: Временные ограничения
        NOT_MEET_REQUIREMENTS: Не соответствует требованиям
        EXCLUDED: Исключено
        NO_OFFICIAL_ADMITTANCE: Отсутствует официальное право доступа
            компетентного ведомства страны-импортера
        PENDING_ADMITTANCE: Ограничено до получения права доступа от
            компетентного ведомства страны-импортера
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    WITHOUT_RESTRICTION = "WITHOUT_RESTRICTION"
    ENHANCED_MONITORING = "ENHANCED_MONITORING"
    SPECIFIC_REQUIREMENTS = "SPECIFIC_REQUIREMENTS"
    CAUTION = "CAUTION"
    TEMPORARY_RESTRICTIONS = "TEMPORARY_RESTRICTIONS"
    NOT_MEET_REQUIREMENTS = "NOT_MEET_REQUIREMENTS"
    EXCLUDED = "EXCLUDED"
    NO_OFFICIAL_ADMITTANCE = "NO_OFFICIAL_ADMITTANCE"
    PENDING_ADMITTANCE = "PENDING_ADMITTANCE"

    __descriptions = {
        UNKNOWN: "Неизвестный статус",
        UNDEFINED: "Статус не определен",
        WITHOUT_RESTRICTION: "Без ограничений",
        ENHANCED_MONITORING: "Усиленный лабораторный контроль",
        SPECIFIC_REQUIREMENTS: "Специальные требования",
        CAUTION: "Предупреждение",
        TEMPORARY_RESTRICTIONS: "Временные ограничения",
        NOT_MEET_REQUIREMENTS: "Не соответствует требованиям",
        EXCLUDED: "Исключено",
        NO_OFFICIAL_ADMITTANCE: (
            "Отсутствует официальное право доступа компетентного ведомства страны-"
            "импортера"
        ),
        PENDING_ADMITTANCE: (
            "Ограничено до получения права доступа от компетентного ведомства страны-"
            "импортера"
        ),
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ApprovalStatusTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class BusinessEntityStatusContentType(Enum):
    """
    Тип, описывающий статус предприятия в реестре.

    Attributes:
        UNKNOWN: Неизвестный статус / другой.
        UNDEFINED: Статус не определен, отсутствует.
        UNVERIFIED: Не подтверджен (не в реестре).
        VERIFIED: Подтвержден (включен в реестр).
        CANCELED: Исключен из реестра.
        DELETED: Удален.
        ELIMINATED: Прекратил деятельность (исключен из реестра).
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    CANCELED = "CANCELED"
    DELETED = "DELETED"
    ELIMINATED = "ELIMINATED"

    __descriptions = {
        UNKNOWN: "Неизвестный статус / другой.",
        UNDEFINED: "Статус не определен, отсутствует.",
        UNVERIFIED: "Не подтверджен (не в реестре).",
        VERIFIED: "Подтвержден (включен в реестр).",
        CANCELED: "Исключен из реестра.",
        DELETED: "Удален.",
        ELIMINATED: "Прекратил деятельность (исключен из реестра).",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        BusinessEntityStatusContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class BusinessEntityTypeContentType(Enum):
    """
    Тип, описывающий тип ХС.

    Attributes:
        VALUE_0: Неизвестный тип.
        VALUE_1: JURIDICAL - юридическое лицо.
        VALUE_2: PHYSICAL - физическое лицо.
        VALUE_3: SELF_EMPLOYED - индивидуальный предприниматель.
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

    __descriptions = {
        VALUE_0: "Неизвестный тип.",
        VALUE_1: "JURIDICAL - юридическое лицо.",
        VALUE_2: "PHYSICAL - физическое лицо.",
        VALUE_3: "SELF_EMPLOYED - индивидуальный предприниматель.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        BusinessEntityTypeContentType.VALUE_0.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ControlSampleIndicatorContentType(Enum):
    """
    Наличие контрольного образца.

    Attributes:
        UNKNOWN: Неизвестный тип / другое
        UNDEFINED: Не определено / не задано
        EXISTS: Присутствует
        NOT_EXISTS: Отсутствует
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    EXISTS = "EXISTS"
    NOT_EXISTS = "NOT_EXISTS"

    __descriptions = {
        UNKNOWN: "Неизвестный тип / другое",
        UNDEFINED: "Не определено / не задано",
        EXISTS: "Присутствует",
        NOT_EXISTS: "Отсутствует",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ControlSampleIndicatorContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class DocumentNatureContentType(Enum):
    """
    Природа (тип) документа.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        ELECTRONIC: Электронный документ
        PAPER: Бумажный документ
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    ELECTRONIC = "ELECTRONIC"
    PAPER = "PAPER"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        ELECTRONIC: "Электронный документ",
        PAPER: "Бумажный документ",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        DocumentNatureContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class DocumentTypeContentType(Enum):
    """
    Тип документа.

    Attributes:
        VALUE_0: Неизвестный тип документа
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
        VALUE_25: Свидетельство о государственной регистрации
        VALUE_26: Сертификат подтверждения соответствия продукта
            требованиям и стандартам Халяль
        VALUE_27: Ветеринарное разрешение на экспорт продукции с
            территории ТС в третьи страны.
        VALUE_28: Сертификат качества продукции, а также иной документ,
            подтверждающий качество
        VALUE_29: Контракт на поставку продукции (копия контракта)
        VALUE_30: Упаковочный лист
        VALUE_31: Заключение или иной документ, подтверждающий факт
            проведения дезинфекции транспортного средства
        VALUE_32: Заключение о соответствии продукции установленным
            требованиям
        VALUE_33: Протокол лабораторных исследований
        VALUE_34: Разрешение на вылов водных биологических ресурсов
        VALUE_35: Договор фрахтования судна
        VALUE_36: Ветеринарный паспорт животного
        VALUE_37: Заключение о ветеринарно-санитарном соответствии
            экспортируемой партии рыбной продукции и нерыбных объектов
            промысла требованиям страны-импортера
        VALUE_38: Регистрационное удостоверение лекарственного препарата
            или фармацевтической субстанции
        VALUE_39: Анкета-вопросник для обследования предприятия
        VALUE_40: Декларация о соответствии
        VALUE_41: Сертификат соответствия
        VALUE_42: Образец маркировки продукции
        VALUE_43: Технологический журнал производства продукции
        VALUE_44: Дополнительная документация к контракту на поставку
            продукции (Доп.соглашение, Агентский договор и т.п.)
        VALUE_45: Учетные документы на основе НАССР
        VALUE_46: Счет на оплату
        VALUE_47: Договор на оказание услуг
        VALUE_48: Акт выполненных работ
        VALUE_49: Спецификация к счету на оплату
        VALUE_50: Договор с визуализацией подписей УКЭП
        VALUE_51: Разрешение на добычу охотничьих ресурсов
        VALUE_52: Акт возврата товара поставщику
        VALUE_53: Электронная карточка животного ФГИС ВетИС
        VALUE_54: Сведения об идентификации животного ФГИС ВетИС
        VALUE_55: Учётная карточка животного хозяйства
        VALUE_56: Зарубежный идентификационный номер животного
    """

    VALUE_0 = 0
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
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33
    VALUE_34 = 34
    VALUE_35 = 35
    VALUE_36 = 36
    VALUE_37 = 37
    VALUE_38 = 38
    VALUE_39 = 39
    VALUE_40 = 40
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_55 = 55
    VALUE_56 = 56

    __descriptions = {
        VALUE_0: "Неизвестный тип документа",
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
        VALUE_25: "Свидетельство о государственной регистрации",
        VALUE_26: (
            "Сертификат подтверждения соответствия продукта требованиям и стандартам "
            "Халяль"
        ),
        VALUE_27: (
            "Ветеринарное разрешение на экспорт продукции с территории ТС в третьи "
            "страны."
        ),
        VALUE_28: (
            "Сертификат качества продукции, а также иной документ, подтверждающий "
            "качество"
        ),
        VALUE_29: "Контракт на поставку продукции (копия контракта)",
        VALUE_30: "Упаковочный лист",
        VALUE_31: (
            "Заключение или иной документ, подтверждающий факт проведения дезинфекции "
            "транспортного средства"
        ),
        VALUE_32: "Заключение о соответствии продукции установленным требованиям",
        VALUE_33: "Протокол лабораторных исследований",
        VALUE_34: "Разрешение на вылов водных биологических ресурсов",
        VALUE_35: "Договор фрахтования судна",
        VALUE_36: "Ветеринарный паспорт животного",
        VALUE_37: (
            "Заключение о ветеринарно-санитарном соответствии экспортируемой партии "
            "рыбной продукции\nи нерыбных объектов промысла требованиям страны-"
            "импортера"
        ),
        VALUE_38: (
            "Регистрационное удостоверение лекарственного препарата или "
            "фармацевтической субстанции"
        ),
        VALUE_39: "Анкета-вопросник для обследования предприятия",
        VALUE_40: "Декларация о соответствии",
        VALUE_41: "Сертификат соответствия",
        VALUE_42: "Образец маркировки продукции",
        VALUE_43: "Технологический журнал производства продукции",
        VALUE_44: (
            "Дополнительная документация к контракту на поставку продукции "
            "(Доп.соглашение, Агентский договор и т.п.)"
        ),
        VALUE_45: "Учетные документы на основе НАССР",
        VALUE_46: "Счет на оплату",
        VALUE_47: "Договор на оказание услуг",
        VALUE_48: "Акт выполненных работ",
        VALUE_49: "Спецификация к счету на оплату",
        VALUE_50: "Договор с визуализацией подписей УКЭП",
        VALUE_51: "Разрешение на добычу охотничьих ресурсов",
        VALUE_52: "Акт возврата товара поставщику",
        VALUE_53: "Электронная карточка животного ФГИС ВетИС",
        VALUE_54: "Сведения об идентификации животного ФГИС ВетИС",
        VALUE_55: "Учётная карточка животного хозяйства",
        VALUE_56: "Зарубежный идентификационный номер животного",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        DocumentTypeContentType.VALUE_0.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class EnterpriseActivityTypeContentType(Enum):
    """
    Вид аттестованной деятельности.

    Attributes:
        UNKNOWN: Неизвестный вид
        UNDEFINED: Вид деятельности не определен
        HARVESTING: заготовка
        PACKING: фасовка
        KEEPING: содержание
        CUTTING: разделка
        SLAUGHTER: убой
        TRADING: реализация
        PROCESSING: переработка
        PRODUCING: выращивание
        MANUFACTURING: производство
        BREEDING: разведение
        TRANSFERRING: перемещение
        STORING: хранение
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    HARVESTING = "HARVESTING"
    PACKING = "PACKING"
    KEEPING = "KEEPING"
    CUTTING = "CUTTING"
    SLAUGHTER = "SLAUGHTER"
    TRADING = "TRADING"
    PROCESSING = "PROCESSING"
    PRODUCING = "PRODUCING"
    MANUFACTURING = "MANUFACTURING"
    BREEDING = "BREEDING"
    TRANSFERRING = "TRANSFERRING"
    STORING = "STORING"

    __descriptions = {
        UNKNOWN: "Неизвестный вид",
        UNDEFINED: "Вид деятельности не определен",
        HARVESTING: "заготовка",
        PACKING: "фасовка",
        KEEPING: "содержание",
        CUTTING: "разделка",
        SLAUGHTER: "убой",
        TRADING: "реализация",
        PROCESSING: "переработка",
        PRODUCING: "выращивание",
        MANUFACTURING: "производство",
        BREEDING: "разведение",
        TRANSFERRING: "перемещение",
        STORING: "хранение",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        EnterpriseActivityTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class EnterpriseRoleContentType(Enum):
    """
    Тип, описывающий роль пердприятия.

    Attributes:
        UNKNOWN: Неизвестная роль.
        UNDEFINED: Роль не определена.
        PRODUCER: Является производителем продукции (в том числе
            выращивание).
        SLAUGHTER_HOUSE: Бойня (мясокомбинат).
        CUTTING_PLANT: Разделочное предприятие.
        COLD_STORE: Холодильник.
        PACKAGING_PLANT: Упаковочное предприятие.
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    PRODUCER = "PRODUCER"
    SLAUGHTER_HOUSE = "SLAUGHTER_HOUSE"
    CUTTING_PLANT = "CUTTING_PLANT"
    COLD_STORE = "COLD_STORE"
    PACKAGING_PLANT = "PACKAGING_PLANT"

    __descriptions = {
        UNKNOWN: "Неизвестная роль.",
        UNDEFINED: "Роль не определена.",
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
        EnterpriseRoleContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class EnterpriseStatusContentType(Enum):
    """
    Тип, описывающий статус предприятия в реестре.

    Attributes:
        UNKNOWN: Неизвестный статус.
        UNDEFINED: Статус не определен.
        UNVERIFIED: Не подтверджен (не в реестре).
        VERIFIED: Подтвержден (включен в реестр).
        CANCELED: Исключен из реестра.
        DELETED: Удален.
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    CANCELED = "CANCELED"
    DELETED = "DELETED"

    __descriptions = {
        UNKNOWN: "Неизвестный статус.",
        UNDEFINED: "Статус не определен.",
        UNVERIFIED: "Не подтверджен (не в реестре).",
        VERIFIED: "Подтвержден (включен в реестр).",
        CANCELED: "Исключен из реестра.",
        DELETED: "Удален.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        EnterpriseStatusContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class FmpregistryStatusContentType(Enum):
    """
    Тип решения (разрешение, запрет)

    Attributes:
        VALUE_0: Не определено/другое
        VALUE_1: Статус: Принята Описание: Заявка принята отделом
            организационно-методической работы Россельхознадзора
            Соответствует состоянию записи: Заявка (регистрация
            отсутствует)
        VALUE_2: Статус: Направлена в ФГБУ ВГНКИ Описание:
            Регистрационное досье и образцы направлены в ФГБУ для
            проведения регистрационных испытаний Соответствует состоянию
            записи: Заявка (регистрация отсутствует)
        VALUE_5: Статус: Проведение экспертизы Описание: ФГБУ ВГНКИ
            проводит регистрационные испытания образцов Соответствует
            состоянию записи: Заявка (регистрация отсутствует)
        VALUE_6: Статус: Подготовка экспертного заключения /
            Рассмотрение документов Описание: На основании
            регистрационных испытаний, ФГБУ ВГНКИ готовит экспертное
            заключение Соответствует состоянию записи: Заявка
            (регистрация отсутствует)
        VALUE_7: Статус: Запрос дополнительных материалов Описание:
            Заявителю рекомендовано представить дополнительную
            информацию/внести изменения в документацию Соответствует
            состоянию записи: Заявка (регистрация отсутствует)
        VALUE_8: Статус: Заключение ФГБУ ВГНКИ Описание: По результатам
            испытаний ФГБУ дает заключение о возможности регистрации
            лекарственного средства/кормовой добавки Соответствует
            состоянию записи: Заявка (регистрация отсутствует)
        VALUE_9: Статус: Документы переданы в Россельхознадзор Описание:
            После проведения регистрационных испытаний в ФГБУ ВГНКИ,
            документы переданы на рассмотрение в "Отдел организации
            деятельности подведомственных учреждений в области
            ветеринарии" Россельхознадзора Соответствует состоянию
            записи: Заявка (регистрация отсутствует)
        VALUE_10: Статус: Согласование документов Описание: Начальник
            управления ветеринарного надзора Россельхознадзора проводит
            согласование нормативно-технической документации и
            инструкций по применению Соответствует состоянию записи:
            Заявка (регистрация отсутствует)
        VALUE_13: Статус: Зарегистрировано / Внесено в реестр Описание:
            Дата государственной регистрации лекарственного
            средства/кормовой добавки Соответствует состоянию записи: В
            реестре (регистрация подтверждена)
        VALUE_14: Статус: Отмена госрегистрации Описание: Заявка снята с
            регистрации по просьбе заявителя или по решению
            Россельхознадзора Соответствует состоянию записи: Не в
            реестре (регистрация отменена)
        VALUE_15: Статус: Регистрация приостановлена Описание: Процедура
            государственной регистрации приостановлена Соответствует
            состоянию записи: Не в реестре (регистрация отменена)
        VALUE_16: Статус: Применение приостановлено Описание: Применение
            приостановлено Соответствует состоянию записи: Не в реестре
            (регистрация отменена)
        VALUE_17: Статус: Отказано в госрегистрации Описание: По
            заключению комиссии экспертов отказано в государственной
            регистрации Соответствует состоянию записи: Не в реестре
            (регистрация отменена)
        VALUE_18: Статус: Регистрация отменена Описание: Регистрация
            отменена Соответствует состоянию записи: Не в реестре
            (регистрация отменена)
        VALUE_19: Статус: Подтверждение госрегистрации Описание: Подана
            заявка на подтверждение госрегистрации Соответствует
            состоянию записи: В реестре (регистрация подтверждена)
        VALUE_20: Статус: Внесение изменений Описание: Подана заявка на
            внесение изменений Соответствует состоянию записи: В реестре
            (регистрация подтверждена)
        VALUE_21: Статус: Отказ подтверждения госрегистрации Описание:
            Отказ подтверждения госрегистрации Соответствует состоянию
            записи: Не в реестре (регистрация отменена)
        VALUE_22: Статус: Отказ во внесении изменений Описание: Отказ во
            внесении изменений Соответствует состоянию записи: В реестре
            (регистрация подтверждена)
        VALUE_23: Статус: Срок регистрации истек Описание: Срок
            регистрации истек Соответствует состоянию записи: Не в
            реестре (регистрация отменена)
        VALUE_24: Статус: Отказ во включении в реестр Описание: Отказ во
            включении в реестр Соответствует состоянию записи: Не в
            реестре (регистрация отменена)
        VALUE_25: Статус: Регистрация прекращена Описание: Регистрация
            прекращена Соответствует состоянию записи: Не в реестре
            (регистрация отменена)
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9 = "9"
    VALUE_10 = "10"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"

    __descriptions = {
        VALUE_0: "Не определено/другое",
        VALUE_1: (
            "Статус: Принята\nОписание: Заявка принята отделом организационно-"
            "методической работы Россельхознадзора\nСоответствует состоянию записи: "
            "Заявка (регистрация отсутствует)"
        ),
        VALUE_2: (
            "Статус: Направлена в ФГБУ ВГНКИ\nОписание: Регистрационное досье и "
            "образцы направлены в ФГБУ для проведения "
            "регистрационных\nиспытаний\nСоответствует состоянию записи: Заявка "
            "(регистрация отсутствует)"
        ),
        VALUE_5: (
            "Статус: Проведение экспертизы\nОписание: ФГБУ ВГНКИ проводит "
            "регистрационные испытания образцов\nСоответствует состоянию записи: "
            "Заявка (регистрация отсутствует)"
        ),
        VALUE_6: (
            "Статус: Подготовка экспертного заключения / Рассмотрение "
            "документов\nОписание: На основании регистрационных испытаний, ФГБУ ВГНКИ "
            "готовит экспертное заключение\nСоответствует состоянию записи: Заявка "
            "(регистрация отсутствует)"
        ),
        VALUE_7: (
            "Статус: Запрос дополнительных материалов\nОписание: Заявителю "
            "рекомендовано представить дополнительную информацию/внести изменения "
            "в\nдокументацию\nСоответствует состоянию записи: Заявка (регистрация "
            "отсутствует)"
        ),
        VALUE_8: (
            "Статус: Заключение ФГБУ ВГНКИ\nОписание: По результатам испытаний ФГБУ "
            "дает заключение о возможности регистрации "
            "лекарственного\nсредства/кормовой добавки\nСоответствует состоянию "
            "записи: Заявка (регистрация отсутствует)"
        ),
        VALUE_9: (
            "Статус: Документы переданы в Россельхознадзор\nОписание: После проведения"
            " регистрационных испытаний в ФГБУ ВГНКИ, документы переданы "
            'на\nрассмотрение в "Отдел организации деятельности подведомственных '
            'учреждений в области\nветеринарии" Россельхознадзора\nСоответствует '
            "состоянию записи: Заявка (регистрация отсутствует)"
        ),
        VALUE_10: (
            "Статус: Согласование документов\nОписание: Начальник управления "
            "ветеринарного надзора Россельхознадзора проводит "
            "согласование\nнормативно-технической документации и инструкций по "
            "применению\nСоответствует состоянию записи: Заявка (регистрация "
            "отсутствует)"
        ),
        VALUE_13: (
            "Статус: Зарегистрировано / Внесено в реестр\nОписание: Дата "
            "государственной регистрации лекарственного средства/кормовой "
            "добавки\nСоответствует состоянию записи: В реестре (регистрация "
            "подтверждена)"
        ),
        VALUE_14: (
            "Статус: Отмена госрегистрации\nОписание: Заявка снята с регистрации по "
            "просьбе заявителя или по решению Россельхознадзора\nСоответствует "
            "состоянию записи: Не в реестре (регистрация отменена)"
        ),
        VALUE_15: (
            "Статус: Регистрация приостановлена\nОписание: Процедура государственной "
            "регистрации приостановлена\nСоответствует состоянию записи: Не в реестре "
            "(регистрация отменена)"
        ),
        VALUE_16: (
            "Статус: Применение приостановлено\nОписание: Применение "
            "приостановлено\nСоответствует состоянию записи: Не в реестре (регистрация"
            " отменена)"
        ),
        VALUE_17: (
            "Статус: Отказано в госрегистрации\nОписание: По заключению комиссии "
            "экспертов отказано в государственной регистрации\nСоответствует состоянию"
            " записи: Не в реестре (регистрация отменена)"
        ),
        VALUE_18: (
            "Статус: Регистрация отменена\nОписание: Регистрация "
            "отменена\nСоответствует состоянию записи: Не в реестре (регистрация "
            "отменена)"
        ),
        VALUE_19: (
            "Статус: Подтверждение госрегистрации\nОписание: Подана заявка на "
            "подтверждение госрегистрации\nСоответствует состоянию записи: В реестре "
            "(регистрация подтверждена)"
        ),
        VALUE_20: (
            "Статус: Внесение изменений\nОписание: Подана заявка на внесение "
            "изменений\nСоответствует состоянию записи: В реестре (регистрация "
            "подтверждена)"
        ),
        VALUE_21: (
            "Статус: Отказ подтверждения госрегистрации\nОписание: Отказ подтверждения"
            " госрегистрации\nСоответствует состоянию записи: Не в реестре "
            "(регистрация отменена)"
        ),
        VALUE_22: (
            "Статус: Отказ во внесении изменений\nОписание: Отказ во внесении "
            "изменений\nСоответствует состоянию записи: В реестре (регистрация "
            "подтверждена)"
        ),
        VALUE_23: (
            "Статус: Срок регистрации истек\nОписание: Срок регистрации "
            "истек\nСоответствует состоянию записи: Не в реестре (регистрация "
            "отменена)"
        ),
        VALUE_24: (
            "Статус: Отказ во включении в реестр\nОписание: Отказ во включении в "
            "реестр\nСоответствует состоянию записи: Не в реестре (регистрация "
            "отменена)"
        ),
        VALUE_25: (
            "Статус: Регистрация прекращена\nОписание: Регистрация "
            "прекращена\nСоответствует состоянию записи: Не в реестре (регистрация "
            "отменена)"
        ),
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        FMPRegistryStatusContentType.VALUE_0.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class IntendedUseContentType(Enum):
    """
    Тип, описывающий назначение партии продукции.

    Attributes:
        UNKNOWN: Неизвестный тип назначения / другой. назначение
            известно, но среди значений в этом списке нет подходящего
            варианта
        UNDEFINED: Назначение не определено. данные о назначении не
            представлены (NULL)
        UNIDENTIFIED: Неустановленное назначение не смогли определить
            назначение партии продукции
        HUMAN_CONSUMPTION: в пищу людям подконтрольный товар выпускается
            с целью использования в пищу людям в натуральном виде или
            после кулинарной обработки/доработки подпункт «а»
            Методических указаний
        MANUFACTURING_HUMAN_CONSUMPTION: для переработки с целью
            получения подконтрольных товаров, предназначенных в пищу
            людям подконтрольный товар не предназначается производителем
            для использования непосредственно в пищу людям и
            предназначен для переработки с целью получения
            подконтрольных товаров, предназначенных в пищу людям
            подпункт «б» Методических указаний
        DECONTAMINATION_HUMAN_CONSUMPTION: для переработки с
            обеззараживанием с целью получения подконтрольных товаров,
            предназначенных в пищу людям подконтрольный товар не
            предназначается производителем для использования
            непосредственно в пищу людям и предназначен для переработки
            с целью получения подконтрольных товаров, предназначенных в
            пищу людям подпункт «в» Методических указаний
        ANIMAL_FEED: в корм животным подконтрольный товар выпускается с
            целью использования в корм животным в натуральном виде или
            после кормовой обработки/доработки подпункт «г» Методических
            указаний
        MANUFACTURING_ANIMAL_FEED: для переработки с целью получения
            подконтрольных товаров, предназначенных в корм животным
            подконтрольный товар не предназначается производителем
            непосредственно в корм животным и предназначен для
            переработки с целью получения подконтрольных товаров,
            предназначенных в корм животным подпункт «д» Методических
            указаний
        MEDICAL_USE: для медицинских целей подконтрольный товар
            вырабатывается для производства лекарственных средств и
            медицинских изделий подпункт «е» Методических указаний
        MANUFACTURING_MEDICAL_USE: для переработки с целью получения
            подконтрольных товаров, предназначенных для медицинских
            целей подконтрольный товар не может быть использован
            непосредственно для медицинских целей и выпускается для
            последующей переработки с целью производства лекарственных
            средств и медицинских изделий подпункт «ж» Методических
            указаний
        SCIENTIFIC_PURPOSES: для биологических, ветеринарных и
            биотехнологических целей подконтрольный товар выпускается
            для непосредственного использования в биологии, ветеринарии
            и биотехнологии подпункт «з» Методических указаний
        MANUFACTURING_SCIENTIFIC_PURPOSES: для переработки с целью
            получения подконтрольных товаров, предназначенных для
            биологических, ветеринарных и биотехнологических целей
            подконтрольный товар не может быть использован
            непосредственно для биологических, ветеринарных и
            биотехнологических целей и выпускается для последующей
            переработки с целью производства товаров для биологии,
            ветеринарии и биотехнологии подпункт «и» Методических
            указаний
        LABORATORY_TESTS: для диагностических и иных лабораторных
            исследований подконтрольный товар представляет собой пробы
            органов и тканей животных, растений, окружающей среды,
            контаминированных материалов, подконтрольных товаров,
            отбираемых для лабораторных и научных исследований подпункт
            «к» Методических указаний
        TECHNICAL_PURPOSES: для технических целей подпункт «л»
            Методических указаний
        DISPOSAL: для утилизации подконтрольный товар не может быть
            использован для каких-либо целей, кроме технических целей и
            производства удобрений подпункт «м» Методических указаний
        DESTRUCTION: для уничтожения подконтрольный товар не может быть
            использован для каких-либо целей и должен быть уничтожен
            после производства подпункт «н» Методических указаний
        EXAMINATION: для проведения ветеринарно-санитарной экспертизы
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    UNIDENTIFIED = "UNIDENTIFIED"
    HUMAN_CONSUMPTION = "HUMAN_CONSUMPTION"
    MANUFACTURING_HUMAN_CONSUMPTION = "MANUFACTURING_HUMAN_CONSUMPTION"
    DECONTAMINATION_HUMAN_CONSUMPTION = "DECONTAMINATION_HUMAN_CONSUMPTION"
    ANIMAL_FEED = "ANIMAL_FEED"
    MANUFACTURING_ANIMAL_FEED = "MANUFACTURING_ANIMAL_FEED"
    MEDICAL_USE = "MEDICAL_USE"
    MANUFACTURING_MEDICAL_USE = "MANUFACTURING_MEDICAL_USE"
    SCIENTIFIC_PURPOSES = "SCIENTIFIC_PURPOSES"
    MANUFACTURING_SCIENTIFIC_PURPOSES = "MANUFACTURING_SCIENTIFIC_PURPOSES"
    LABORATORY_TESTS = "LABORATORY_TESTS"
    TECHNICAL_PURPOSES = "TECHNICAL_PURPOSES"
    DISPOSAL = "DISPOSAL"
    DESTRUCTION = "DESTRUCTION"
    EXAMINATION = "EXAMINATION"

    __descriptions = {
        UNKNOWN: (
            "Неизвестный тип назначения / другой.\nназначение известно, но среди "
            "значений в этом списке нет подходящего варианта"
        ),
        UNDEFINED: "Назначение не определено.\nданные о назначении не представлены (NULL)",
        UNIDENTIFIED: "Неустановленное назначение\nне смогли определить назначение партии продукции",
        HUMAN_CONSUMPTION: (
            "в пищу людям\nподконтрольный товар выпускается с целью использования в "
            "пищу людям в натуральном виде\nили после кулинарной "
            "обработки/доработки\nподпункт «а» Методических указаний"
        ),
        MANUFACTURING_HUMAN_CONSUMPTION: (
            "для переработки с целью получения подконтрольных товаров, предназначенных"
            " в пищу\nлюдям\nподконтрольный товар не предназначается производителем "
            "для использования\nнепосредственно в пищу людям и предназначен для "
            "переработки с целью получения подконтрольных товаров,\nпредназначенных в "
            "пищу людям\nподпункт «б» Методических указаний"
        ),
        DECONTAMINATION_HUMAN_CONSUMPTION: (
            "для переработки с обеззараживанием с целью получения подконтрольных "
            "товаров,\nпредназначенных в пищу людям\nподконтрольный товар не "
            "предназначается производителем для использования\nнепосредственно в пищу "
            "людям и предназначен для переработки с целью получения подконтрольных "
            "товаров,\nпредназначенных в пищу людям\nподпункт «в» Методических "
            "указаний"
        ),
        ANIMAL_FEED: (
            "в корм животным\nподконтрольный товар выпускается с целью использования в"
            " корм животным в натуральном\nвиде или после кормовой "
            "обработки/доработки\nподпункт «г» Методических указаний"
        ),
        MANUFACTURING_ANIMAL_FEED: (
            "для переработки с целью получения подконтрольных товаров, предназначенных"
            " в корм\nживотным\nподконтрольный товар не предназначается производителем"
            " непосредственно в корм животным\nи предназначен для переработки с целью "
            "получения подконтрольных товаров, предназначенных в "
            "корм\nживотным\nподпункт «д» Методических указаний"
        ),
        MEDICAL_USE: (
            "для медицинских целей\nподконтрольный товар вырабатывается для "
            "производства лекарственных средств и\nмедицинских изделий\nподпункт «е» "
            "Методических указаний"
        ),
        MANUFACTURING_MEDICAL_USE: (
            "для переработки с целью получения подконтрольных товаров, предназначенных"
            " для\nмедицинских целей\nподконтрольный товар не может быть использован "
            "непосредственно для медицинских целей и\nвыпускается для последующей "
            "переработки с целью производства лекарственных средств и "
            "медицинских\nизделий\nподпункт «ж» Методических указаний"
        ),
        SCIENTIFIC_PURPOSES: (
            "для биологических, ветеринарных и биотехнологических "
            "целей\nподконтрольный товар выпускается для непосредственного "
            "использования в биологии,\nветеринарии и биотехнологии\nподпункт «з» "
            "Методических указаний"
        ),
        MANUFACTURING_SCIENTIFIC_PURPOSES: (
            "для переработки с целью получения подконтрольных товаров, предназначенных"
            " для\nбиологических, ветеринарных и биотехнологических "
            "целей\nподконтрольный товар не может быть использован непосредственно для"
            " биологических,\nветеринарных и биотехнологических целей и выпускается "
            "для последующей переработки с целью производства\nтоваров для биологии, "
            "ветеринарии и биотехнологии\nподпункт «и» Методических указаний"
        ),
        LABORATORY_TESTS: (
            "для диагностических и иных лабораторных исследований\nподконтрольный "
            "товар представляет собой пробы органов и тканей животных, "
            "растений,\nокружающей среды, контаминированных материалов, подконтрольных"
            " товаров, отбираемых для лабораторных и\nнаучных исследований\nподпункт "
            "«к» Методических указаний"
        ),
        TECHNICAL_PURPOSES: "для технических целей\nподпункт «л» Методических указаний",
        DISPOSAL: (
            "для утилизации\nподконтрольный товар не может быть использован для каких-"
            "либо целей, кроме технических\nцелей и производства удобрений\nподпункт "
            "«м» Методических указаний"
        ),
        DESTRUCTION: (
            "для уничтожения\nподконтрольный товар не может быть использован для "
            "каких-либо целей и должен быть\nуничтожен после производства\nподпункт "
            "«н» Методических указаний"
        ),
        EXAMINATION: "для проведения ветеринарно-санитарной экспертизы",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        IntendedUseContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class NonFoodProductSourceTypeContentType(Enum):
    """
    Attributes:
        CATTLE_SLAUGHTER: Боенское.
        LOSS_OF_CATTLE: Палое.
        MANUFACTURED: Промышленное.
        MIXED: Сборное.
        FROM_HEALTHY_ANIMALS: Полученное от здоровых животных.
        FROM_SICK_ANIMALS: Полученное от больных животных.
        UNKNOWN: Неизвестный тип
        UNDEFINED: Не определено/другое
    """

    CATTLE_SLAUGHTER = "CATTLE_SLAUGHTER"
    LOSS_OF_CATTLE = "LOSS_OF_CATTLE"
    MANUFACTURED = "MANUFACTURED"
    MIXED = "MIXED"
    FROM_HEALTHY_ANIMALS = "FROM_HEALTHY_ANIMALS"
    FROM_SICK_ANIMALS = "FROM_SICK_ANIMALS"
    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"

    __descriptions = {
        CATTLE_SLAUGHTER: "Боенское.",
        LOSS_OF_CATTLE: "Палое.",
        MANUFACTURED: "Промышленное.",
        MIXED: "Сборное.",
        FROM_HEALTHY_ANIMALS: "Полученное от здоровых животных.",
        FROM_SICK_ANIMALS: "Полученное от больных животных.",
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Не определено/другое",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        NonFoodProductSourceTypeContentType.CATTLE_SLAUGHTER.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class PackageLevelTypeContentType(Enum):
    """
    Тип, описывающий уровень упаковки.

    Attributes:
        VALUE_0: Неизвестный уровень
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

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

    __descriptions = {
        VALUE_0: "Неизвестный уровень",
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
        PackageLevelTypeContentType.VALUE_0.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class PackingCodeTypeContentType(Enum):
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
        PackingCodeTypeContentType.VALUE_1_A.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class PermitDecisionContentType(Enum):
    """
    Тип решения (разрешение, запрет)

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        AUTHORIZED: Разрешение
        FORBIDDEN: Запрет
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    AUTHORIZED = "AUTHORIZED"
    FORBIDDEN = "FORBIDDEN"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        AUTHORIZED: "Разрешение",
        FORBIDDEN: "Запрет",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        PermitDecisionContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class PharmaceuticalTypeContentType(Enum):
    """
    Тип лекарственного средства.

    Attributes:
        UNKNOWN: Неизвестный тип.
        UNDEFINED: Не определено.
        VACCINE: Вакцина.
        OTHER: Прочие лекарственные средства.
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    VACCINE = "VACCINE"
    OTHER = "OTHER"

    __descriptions = {
        UNKNOWN: "Неизвестный тип.",
        UNDEFINED: "Не определено.",
        VACCINE: "Вакцина.",
        OTHER: "Прочие лекарственные средства.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        PharmaceuticalTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ProcessingProcedureTypeContentType(Enum):
    """
    Attributes:
        VALUE_0: Неизвестный тип
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
        VALUE_44: Перемещение
        VALUE_51: Сжигание (утилизация)
        VALUE_73: Временное хранения
        VALUE_95: Термическая обработка
        VALUE_10101: Утилизация (метод не определен или отличается от
            обозначенных выше вариантов)
        VALUE_10102: Сортировка и упаковка
        VALUE_101: Пастеризация
        VALUE_10103: Деминерализация
        VALUE_10104: Кристаллизация
        VALUE_93: Сушка
        VALUE_86: Консервация
        VALUE_32: Охлаждение
        VALUE_10105: Копчение
        VALUE_10000: Другое
    """

    VALUE_0 = "0"
    VALUE_7 = "7"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_37 = "37"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_51 = "51"
    VALUE_73 = "73"
    VALUE_95 = "95"
    VALUE_10101 = "10101"
    VALUE_10102 = "10102"
    VALUE_101 = "101"
    VALUE_10103 = "10103"
    VALUE_10104 = "10104"
    VALUE_93 = "93"
    VALUE_86 = "86"
    VALUE_32 = "32"
    VALUE_10105 = "10105"
    VALUE_10000 = "10000"

    __descriptions = {
        VALUE_0: "Неизвестный тип",
        VALUE_7: "Замораживание",
        VALUE_12: "Убой",
        VALUE_13: "Упаковка/фасовка",
        VALUE_34: "Нарезка/разделка",
        VALUE_35: "Добыча (собирать, ловить, охотиться)",
        VALUE_37: "Производство (из сырья вручную или с помощью машин)",
        VALUE_39: "Обработка/переработка (посредством, как правило, рутинных процедур)",
        VALUE_40: "Выращивание",
        VALUE_43: "Хранение",
        VALUE_44: "Перемещение",
        VALUE_51: "Сжигание (утилизация)",
        VALUE_73: "Временное хранения",
        VALUE_95: "Термическая обработка",
        VALUE_10101: (
            "Утилизация (метод не определен или отличается от обозначенных выше "
            "вариантов)"
        ),
        VALUE_10102: "Сортировка и упаковка",
        VALUE_101: "Пастеризация",
        VALUE_10103: "Деминерализация",
        VALUE_10104: "Кристаллизация",
        VALUE_93: "Сушка",
        VALUE_86: "Консервация",
        VALUE_32: "Охлаждение",
        VALUE_10105: "Копчение",
        VALUE_10000: "Другое",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ProcessingProcedureTypeContentType.VALUE_0.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ProductMarkingClassContentType(Enum):
    """
    Тип, описывающий тип маркировки.

    Attributes:
        UNKNOWN: Неизвестный тип.
        UNDEFINED: Класс не определен.
        BN: Номер производственной партии.
        SSCC: SSCC-код.
        EAN8: Маркировка в соответствии с EAN-8.
        EAN13: Маркировка в соответствии с EAN-13.
        EAN128: Маркировка в соответствии с EAN-128.
        BUNDLE: Маркировка вышестоящей групповой упаковки, например,
            паллеты. Может использоваться для поиска группы
            вет.сертификатов для партий, находящихся на данной паллете.
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    BN = "BN"
    SSCC = "SSCC"
    EAN8 = "EAN8"
    EAN13 = "EAN13"
    EAN128 = "EAN128"
    BUNDLE = "BUNDLE"

    __descriptions = {
        UNKNOWN: "Неизвестный тип.",
        UNDEFINED: "Класс не определен.",
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
        ProductMarkingClassContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ProductTypeContentType(Enum):
    """
    Тип, описывающий тип продукции.

    Attributes:
        VALUE_0: Неизвестный тип
        VALUE_1: Мясо и мясопродукты
        VALUE_2: Корма и кормовые добавки
        VALUE_3: Живые животные
        VALUE_4: Лекарственные средства
        VALUE_5: Пищевые продукты
        VALUE_6: Непищевые продукты и другое
        VALUE_7: Рыба и морепродукты
        VALUE_8: Продукция, не требующая разрешения
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8

    __descriptions = {
        VALUE_0: "Неизвестный тип",
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
        ProductTypeContentType.VALUE_0.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ProsperityTypeContentType(Enum):
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
        ProsperityTypeContentType.UNDEFINED.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ReferenceTypeContentType(Enum):
    """
    Attributes:
        VALUE_0: Неизвестный тип связи
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

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

    __descriptions = {
        VALUE_0: "Неизвестный тип связи",
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
        ReferenceTypeContentType.VALUE_0.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class RegionalizationDecisionContentType(Enum):
    """
    Вид требования: перемещение запрещено, перемещение разрешено или перемещение
    разрешено при обязательном соблюдении условий.

    Attributes:
        VALUE_0: Неизвестный вид требования.
        VALUE_1: Перемещение разрешено
        VALUE_2: Перемещение разрешено при обязательном соблюдении
            условий
        VALUE_3: Перемещение запрещено
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"

    __descriptions = {
        VALUE_0: "Неизвестный вид требования.",
        VALUE_1: "Перемещение разрешено",
        VALUE_2: "Перемещение разрешено при обязательном соблюдении условий",
        VALUE_3: "Перемещение запрещено",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        RegionalizationDecisionContentType.VALUE_0.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class ResearchResultContentType(Enum):
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
        UNACCEPTABLE_AB_LEVEL: Недопустимый уровень поствакцинальных
            антител
        POSITIVE_POSTINFECTIOUS: Положительный постинфекционный
        UNCERTAIN: Сомнительный
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    UNFULFILLED = "UNFULFILLED"
    VSERAW = "VSERAW"
    VSEFULL = "VSEFULL"
    UNACCEPTABLE_AB_LEVEL = "UNACCEPTABLE_AB_LEVEL"
    POSITIVE_POSTINFECTIOUS = "POSITIVE_POSTINFECTIOUS"
    UNCERTAIN = "UNCERTAIN"

    __descriptions = {
        UNKNOWN: "Результат неизвестен",
        UNDEFINED: "Результат невозможно определить (не нормируется)",
        POSITIVE: "Положительный результат",
        NEGATIVE: "Отрицательный результат",
        UNFULFILLED: "Не проводилось",
        VSERAW: "ВСЭ подвергнуто сырьё, из которого произведена продукция",
        VSEFULL: "Продукция подвергнута ВСЭ в полном объеме",
        UNACCEPTABLE_AB_LEVEL: "Недопустимый уровень поствакцинальных антител",
        POSITIVE_POSTINFECTIOUS: "Положительный постинфекционный",
        UNCERTAIN: "Сомнительный",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        ResearchResultContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class SampleReturnTypeContentType(Enum):
    """
    Тип возврата пробы.

    Attributes:
        UNKNOWN: Неизвестно / другое
        UNDEFINED: Не определено / отсутствует
        RETURNABLE: Возвращаемая
        NO_RETURN: Без возврата
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    RETURNABLE = "RETURNABLE"
    NO_RETURN = "NO_RETURN"

    __descriptions = {
        UNKNOWN: "Неизвестно / другое",
        UNDEFINED: "Не определено / отсутствует",
        RETURNABLE: "Возвращаемая",
        NO_RETURN: "Без возврата",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        SampleReturnTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class SamplingReasonTypeContentType(Enum):
    """
    Типы оснований для проведения лабораторных исследований.

    Attributes:
        UNKNOWN: Неизвестный тип / другое
        UNDEFINED: Не определено / отсутствует
        OWNER_APPLICATION: Oбращение владельца перемещаемого
            (перевозимого) груза
        PRODUCTION_CONTROL: Производственный контроль
        EXPORT_MONITORING: В рамках гос.программы "Экспорт АПК"
        FOOD_MONITORING: В рамках пищевого мониторинга
        EPIZOOTIC_MONITORING: В рамках эпизоотического мониторинга
        SARS_COV2_TESTING: Исследование упаковки на наличие
            генетического материала коронавируса SARS-CoV-2
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    OWNER_APPLICATION = "OWNER_APPLICATION"
    PRODUCTION_CONTROL = "PRODUCTION_CONTROL"
    EXPORT_MONITORING = "EXPORT_MONITORING"
    FOOD_MONITORING = "FOOD_MONITORING"
    EPIZOOTIC_MONITORING = "EPIZOOTIC_MONITORING"
    SARS_COV2_TESTING = "SARS_COV2_TESTING"

    __descriptions = {
        UNKNOWN: "Неизвестный тип / другое",
        UNDEFINED: "Не определено / отсутствует",
        OWNER_APPLICATION: "Oбращение владельца перемещаемого (перевозимого) груза",
        PRODUCTION_CONTROL: "Производственный контроль",
        EXPORT_MONITORING: 'В рамках гос.программы "Экспорт АПК"',
        FOOD_MONITORING: "В рамках пищевого мониторинга",
        EPIZOOTIC_MONITORING: "В рамках эпизоотического мониторинга",
        SARS_COV2_TESTING: (
            "Исследование упаковки на наличие генетического материала коронавируса "
            "SARS-CoV-2"
        ),
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        SamplingReasonTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class SamplingReportStatusContentType(Enum):
    """
    Статус акта отбора проб.

    Attributes:
        UNKNOWN: Неизвестный статус
        UNDEFINED: Статус не определен
        CREATED: Создан
        CONFIRMED: Оформлен
        WITHDRAWN: Аннулирован
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    CREATED = "CREATED"
    CONFIRMED = "CONFIRMED"
    WITHDRAWN = "WITHDRAWN"

    __descriptions = {
        UNKNOWN: "Неизвестный статус",
        UNDEFINED: "Статус не определен",
        CREATED: "Создан",
        CONFIRMED: "Оформлен",
        WITHDRAWN: "Аннулирован",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        SamplingReportStatusContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class SupervisedObjectStatusContentType(Enum):
    """
    Тип, описывающий статус поднадзорного объекта в реестре.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Не определен
        UNVERIFIED: Не подтверджен (не в реестре)
        VERIFIED: Подтвержден (включен в реестр)
        CANCELED: Исключен из реестра
        DELETED: Удален
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    CANCELED = "CANCELED"
    DELETED = "DELETED"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Не определен",
        UNVERIFIED: "Не подтверджен (не в реестре)",
        VERIFIED: "Подтвержден (включен в реестр)",
        CANCELED: "Исключен из реестра",
        DELETED: "Удален",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        SupervisedObjectStatusContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class TransferTypeContentType(Enum):
    """
    Тип транспортировки.

    Attributes:
        VALUE_0: Неизвестный тип
        VALUE_1: Ввоз (импорт на территорию ТС)
        VALUE_2: Вывоз (экспорт из ТС в третьи страны)
        VALUE_3: Транзит через территорию ТС
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

    __descriptions = {
        VALUE_0: "Неизвестный тип",
        VALUE_1: "Ввоз (импорт на территорию ТС)",
        VALUE_2: "Вывоз (экспорт из ТС в третьи страны)",
        VALUE_3: "Транзит через территорию ТС",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        TransferTypeContentType.VALUE_0.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class TransportTypeContentType(Enum):
    """
    Тип транспорта.

    Attributes:
        VALUE_0: Неизвестный тип транспорта
        VALUE_1: Автомобильный
        VALUE_2: Железнодорожный
        VALUE_3: Авиатранспортный
        VALUE_4: Морской (контейнер)
        VALUE_5: Морской (трюм)
        VALUE_6: Речной (inland water)
        VALUE_7: Перегон (скота)
        VALUE_8: Трубопровод
        VALUE_9: Конвейер
        VALUE_10: Безмоторное ТС
        VALUE_11: Ручное перемещение
        VALUE_12: Общественный транспорт
    """

    VALUE_0 = 0
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

    __descriptions = {
        VALUE_0: "Неизвестный тип транспорта",
        VALUE_1: "Автомобильный",
        VALUE_2: "Железнодорожный",
        VALUE_3: "Авиатранспортный",
        VALUE_4: "Морской (контейнер)",
        VALUE_5: "Морской (трюм)",
        VALUE_6: "Речной (inland water)",
        VALUE_7: "Перегон (скота)",
        VALUE_8: "Трубопровод",
        VALUE_9: "Конвейер",
        VALUE_10: "Безмоторное ТС",
        VALUE_11: "Ручное перемещение",
        VALUE_12: "Общественный транспорт",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        TransportTypeContentType.VALUE_0.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class TransportationStorageTypeContentType(Enum):
    """
    Способ хранения при перевозке.

    Attributes:
        UNKNOWN: Неизвестный типа.
        UNDEFINED: Способ не определен.
        FROZEN: Замороженный тип перевозки
        CHILLED: Охлажденный тип перевозки
        COOLED: Охлаждаемый тип перевозки
        VENTILATED: Вентилируемый тип перевозки
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    FROZEN = "FROZEN"
    CHILLED = "CHILLED"
    COOLED = "COOLED"
    VENTILATED = "VENTILATED"

    __descriptions = {
        UNKNOWN: "Неизвестный типа.",
        UNDEFINED: "Способ не определен.",
        FROZEN: "Замороженный тип перевозки",
        CHILLED: "Охлажденный тип перевозки",
        COOLED: "Охлаждаемый тип перевозки",
        VENTILATED: "Вентилируемый тип перевозки",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        TransportationStorageTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VatmodeContentType(Enum):
    """
    НДС включен в сумму.

    Attributes:
        UNKNOWN: Неизвестный тип / другое
        UNDEFINED: Тип НДС не определен
        NOT_INCLUDED: Не включен
        INCLUDED: Включен
        WITHOUT_VAT: Без НДС
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    NOT_INCLUDED = "NOT_INCLUDED"
    INCLUDED = "INCLUDED"
    WITHOUT_VAT = "WITHOUT_VAT"

    __descriptions = {
        UNKNOWN: "Неизвестный тип / другое",
        UNDEFINED: "Тип НДС не определен",
        NOT_INCLUDED: "Не включен",
        INCLUDED: "Включен",
        WITHOUT_VAT: "Без НДС",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VATModeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VaccinationTypeContentType(Enum):
    """
    Статус применения вакцины.

    Attributes:
        UNKNOWN: Неизвестный статус
        UNDEFINED: Статус не определен
        APPLIED: Вакцинация проводится
        UNVACCINATED: Вакцинация не проводится
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    APPLIED = "APPLIED"
    UNVACCINATED = "UNVACCINATED"

    __descriptions = {
        UNKNOWN: "Неизвестный статус",
        UNDEFINED: "Статус не определен",
        APPLIED: "Вакцинация проводится",
        UNVACCINATED: "Вакцинация не проводится",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VaccinationTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VetDocumentFormContentType(Enum):
    """
    Тип, описывающий форму ВСД.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип ВСД не определен
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

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
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
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип ВСД не определен",
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
        VetDocumentFormContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VetDocumentStatusContentType(Enum):
    """
    Статус ветсертификата.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
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

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    CREATED = "CREATED"
    CONFIRMED = "CONFIRMED"
    WITHDRAWN = "WITHDRAWN"
    UTILIZED = "UTILIZED"
    FINALIZED = "FINALIZED"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        CREATED: "Создан. Неоформленный проект сертификата",
        CONFIRMED: (
            "Оформлен. Действующий сертификат, по которому разрешено совершать "
            "транзакцию с\nгрузом."
        ),
        WITHDRAWN: "Аннулирован. Не действующий более сертификат.",
        UTILIZED: "Погашен. Действующий сертификат, по которому транзакция уже была совершена.",
        FINALIZED: (
            "Закрыт. Действующий производственный сертификат.\nСтатус проставляется "
            "при завершении производственной смены, изменение "
            "финализированного\nвет.сертификата не допускается.\nСтатус `FINALIZED` не"
            " используется в атрибуте `vetDStatus` сертификата, признак того, "
            "что\nпроизводственный сертификат финализирован\nопределяется логическим "
            "атрибутом `finalized` сертификата. При этом сертификат всегда "
            "находится\nв статусе `CONFIRMED`."
        ),
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VetDocumentStatusContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VetDocumentTypeContentType(Enum):
    """
    Тип ветсертификата.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        TRANSPORT: Транспортный
        PRODUCTIVE: Производственный
        RETURNABLE: Возвратный
        INCOMING: Входящий
        OUTGOING: Исходящий
        REDIRECTING: Сертификат перенаправления
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    TRANSPORT = "TRANSPORT"
    PRODUCTIVE = "PRODUCTIVE"
    RETURNABLE = "RETURNABLE"
    INCOMING = "INCOMING"
    OUTGOING = "OUTGOING"
    REDIRECTING = "REDIRECTING"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        TRANSPORT: "Транспортный",
        PRODUCTIVE: "Производственный",
        RETURNABLE: "Возвратный",
        INCOMING: "Входящий",
        OUTGOING: "Исходящий",
        REDIRECTING: "Сертификат перенаправления",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VetDocumentTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VeterinaryEventStatusContentType(Enum):
    """
    Тип.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        ACTIVE: Действующий
        DRAFT: Черновик
        WITHDRAWN: Аннулирован
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    ACTIVE = "ACTIVE"
    DRAFT = "DRAFT"
    WITHDRAWN = "WITHDRAWN"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        ACTIVE: "Действующий",
        DRAFT: "Черновик",
        WITHDRAWN: "Аннулирован",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VeterinaryEventStatusContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VeterinaryEventTypeContentType(Enum):
    """
    Тип мероприятия.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        UND: Не определен
        LBR: Лабораторные исследования
        VSE: Ветеринарно-санитарная экспертиза
        IMM: Иммунизация живого животного
        MED: Обработка живого животного
        QRT: Карантин
        VAC: Вакцинация живого животного
        AMA: Иное применение лекарственных средств в отношении живого
            животного
        AME: Маркирование животного или группы животных (нанесение
            маркировки)
        AIR: Выбытие средства маркирования для животного или группы
            животных
        APS: Плановый убой животного
        ADS: Диагностический убой животного
        AFS: Вынужденный убой животного
        DTH: Падёж животного
        LSS: Пропажа животного (сбежало, украдено и т.п.)
        RLS: Выпуск животного в среду обитания (мальки, личинки, тигры и
            т.п.)
        EXP: Экспорт животного
        IMP: Импорт животного
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    UND = "UND"
    LBR = "LBR"
    VSE = "VSE"
    IMM = "IMM"
    MED = "MED"
    QRT = "QRT"
    VAC = "VAC"
    AMA = "AMA"
    AME = "AME"
    AIR = "AIR"
    APS = "APS"
    ADS = "ADS"
    AFS = "AFS"
    DTH = "DTH"
    LSS = "LSS"
    RLS = "RLS"
    EXP = "EXP"
    IMP = "IMP"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        UND: "Не определен",
        LBR: "Лабораторные исследования",
        VSE: "Ветеринарно-санитарная экспертиза",
        IMM: "Иммунизация живого животного",
        MED: "Обработка живого животного",
        QRT: "Карантин",
        VAC: "Вакцинация живого животного",
        AMA: "Иное применение лекарственных средств в отношении живого животного",
        AME: "Маркирование животного или группы животных (нанесение маркировки)",
        AIR: "Выбытие средства маркирования для животного или группы животных",
        APS: "Плановый убой животного",
        ADS: "Диагностический убой животного",
        AFS: "Вынужденный убой животного",
        DTH: "Падёж животного",
        LSS: "Пропажа животного (сбежало, украдено и т.п.)",
        RLS: "Выпуск животного в среду обитания (мальки, личинки, тигры и т.п.)",
        EXP: "Экспорт животного",
        IMP: "Импорт животного",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VeterinaryEventTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class VeterinaryServiceTypeContentType(Enum):
    """
    Вид ветеринарной услуги.

    Attributes:
        UNKNOWN: Неизвестный вид / другое
        UNDEFINED: Не определено
        WBR_COMPLIENCE_STATEMENT: Выдача заключений ВБР
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    WBR_COMPLIENCE_STATEMENT = "WBR_COMPLIENCE_STATEMENT"

    __descriptions = {
        UNKNOWN: "Неизвестный вид / другое",
        UNDEFINED: "Не определено",
        WBR_COMPLIENCE_STATEMENT: "Выдача заключений ВБР",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        VeterinaryServiceTypeContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class WbrcomplianceDecisionContentType(Enum):
    """
    Тип решения в заключении о соответствии уловов ВБР требованиям.

    Attributes:
        UNKNOWN: Неизвестный тип
        UNDEFINED: Тип не определен
        MEET_REQUIREMENTS: Соответствует
        NOT_MEET_REQUIREMENTS: Не соответствует
    """

    UNKNOWN = "UNKNOWN"
    UNDEFINED = "UNDEFINED"
    MEET_REQUIREMENTS = "MEET_REQUIREMENTS"
    NOT_MEET_REQUIREMENTS = "NOT_MEET_REQUIREMENTS"

    __descriptions = {
        UNKNOWN: "Неизвестный тип",
        UNDEFINED: "Тип не определен",
        MEET_REQUIREMENTS: "Соответствует",
        NOT_MEET_REQUIREMENTS: "Не соответствует",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        WBRComplianceDecisionContentType.UNKNOWN.verbose_name
        """

        return type(self).__descriptions.get(self.value)
