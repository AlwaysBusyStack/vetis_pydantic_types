from __future__ import annotations

from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration

from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.herriot.types.production.base_v2_1 import (
    ComplexDate,
    ComplexDatePeriod,
    EntityList,
    File,
    GenericEntity,
    GenericVersioningEntity,
)
from vetis_pydantic_types.herriot.types.production.codelist_v2_5r4 import (
    AnimalBreedingValueTypeContentType,
    AnimalGenderContentType,
    AnimalIdformatContentType,
    AnimalIdstatusContentType,
    AnimalLabelTypeContentType,
    AnimalMarkingMeansTypeContentType,
    AnimalPlaceKindContentType,
    ApprovalStatusTypeContentType,
    BusinessEntityStatusContentType,
    BusinessEntityTypeContentType,
    ControlSampleIndicatorContentType,
    DocumentNatureContentType,
    DocumentTypeContentType,
    EnterpriseActivityTypeContentType,
    EnterpriseRoleContentType,
    EnterpriseStatusContentType,
    IntendedUseContentType,
    PackageLevelTypeContentType,
    PackingCodeTypeContentType,
    ProductMarkingClassContentType,
    ProductTypeContentType,
    ProsperityTypeContentType,
    ReferenceTypeContentType,
    RegionalizationDecisionContentType,
    ResearchResultContentType,
    SampleReturnTypeContentType,
    SamplingReasonTypeContentType,
    SupervisedObjectStatusContentType,
    TransferTypeContentType,
    TransportationStorageTypeContentType,
    TransportTypeContentType,
    VaccinationTypeContentType,
    VatmodeContentType,
    VeterinaryServiceTypeContentType,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/dictionary/v2"


class CodeType(BaseModel):
    """
    Тип, описывающий код объекта в соответствии с определенным перечнем возможных
    значений.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


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


class RegistryLookupScope(Enum):
    """
    Тип, описывающий область поиска записей в реестре.

    Attributes:
        UNDEFINED: Не определен.
        ALL: Все записи.
        AVAILABLE: Актуальные записи.
        VALID: Проверенные записи (включенные в реестр).
        UNAVAILABLE: Неактуальные записи.
    """

    UNDEFINED = "UNDEFINED"
    ALL = "ALL"
    AVAILABLE = "AVAILABLE"
    VALID = "VALID"
    UNAVAILABLE = "UNAVAILABLE"

    __descriptions = {
        UNDEFINED: "Не определен.",
        ALL: "Все записи.",
        AVAILABLE: "Актуальные записи.",
        VALID: "Проверенные записи (включенные в реестр).",
        UNAVAILABLE: "Неактуальные записи.",
    }

    @property
    def verbose_name(self):
        """Получение описания участника перечисления.

        Использование:
        RegistryLookupScope.UNDEFINED.verbose_name
        """

        return type(self).__descriptions.get(self.value)


class TemperatureMeasure(BaseModel):
    """
    Диапазон температур, в градусах Цельсия.

    Attributes:
        min_value: Минимальное значение.
        max_value: Максимальное значение.
    """

    model_config = ConfigDict(defer_build=True)
    min_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "minValue",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "fraction_digits": 6,
        },
    )
    max_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "maxValue",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "fraction_digits": 6,
        },
    )


class TextCondition(BaseModel):
    """Текстовое описание, условие.

    Например, условие транспортировки груза.
    """

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 100,
        },
    )


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


class AdditionalAttribute(BaseModel):
    """
    Дополнительная характеристика объекта/процесса.

    Attributes:
        attr_id: Идентификатор характеристики
        attr_code: Код типа характеристики
        attr_name: Наименование характеристики
        description: Описание характеристики
    """

    model_config = ConfigDict(defer_build=True)
    attr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 100,
        },
    )
    attr_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "attrCode",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    attr_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
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


class AnimalBreedingValueType(BaseModel):
    """
    Тип, описывающий.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: AnimalBreedingValueTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class AnimalColour(GenericVersioningEntity):
    """
    Масть/окрас животного.

    Attributes:
        name: Наименование масти/окраса
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


class AnimalDisease(GenericVersioningEntity):
    """
    Заболевание.

    Attributes:
        name: Наименование заболевания
        description: Описание заболевания
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
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class AnimalGender(BaseModel):
    """
    Тип, описывающий.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: AnimalGenderContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class AnimalId(BaseModel):
    """
    Тип, описывающий идентификатор животного.

    Attributes:
        value:
        format: Формат номера
        name: Наименование формата номера
    """

    class Meta:
        name = "AnimalID"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 100,
        },
    )
    format: Optional[AnimalIdformatContentType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class AnimalIdformat(BaseModel):
    """
    Тип, описывающий.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    class Meta:
        name = "AnimalIDFormat"

    model_config = ConfigDict(defer_build=True)
    value: AnimalIdformatContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class AnimalIdstatus(BaseModel):
    """
    Тип, описывающий.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    class Meta:
        name = "AnimalIDStatus"

    model_config = ConfigDict(defer_build=True)
    value: AnimalIdstatusContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class AnimalKeepingPurposeInternalType(GenericVersioningEntity):
    """
    Цель содержания.

    Attributes:
        name: Наименование цели содержания
    """

    class Meta:
        name = "AnimalKeepingPurpose"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )


class AnimalKeepingTypeInternalType(GenericVersioningEntity):
    """
    Тип содержания животных.

    Attributes:
        name: Наименование типа содержания
    """

    class Meta:
        name = "AnimalKeepingType"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )


class AnimalLabelType(BaseModel):
    """
    Тип, описывающий.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: AnimalLabelTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class AnimalMarkingLocationInternalType(GenericVersioningEntity):
    """
    Место прикрепления/нанесения/вживления средства маркирования.

    Attributes:
        name: Наименование места маркирования
        description: Описание места маркирования
    """

    class Meta:
        name = "AnimalMarkingLocation"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class AnimalMarkingMeansType(BaseModel):
    """
    Тип, описывающий.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: AnimalMarkingMeansTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class AnimalPlaceKindInternalType(BaseModel):
    """
    Вид размещения живых животных.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    class Meta:
        name = "AnimalPlaceKind"

    model_config = ConfigDict(defer_build=True)
    value: AnimalPlaceKindContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class AnimalSpeciesInternalType(GenericVersioningEntity):
    """
    Биологический вид животного.

    Attributes:
        name: Наименование биологического вида
        code: Код биологического вида
    """

    class Meta:
        name = "AnimalSpecies"

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


class ApprovalStatusType(BaseModel):
    """
    Статус аттестации предприятия.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: ApprovalStatusTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class BusinessEntityStatus(BaseModel):
    """
    Тип, описывающий статус предприятия в реестре.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: BusinessEntityStatusContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class BusinessEntityType(BaseModel):
    """
    Тип, описывающий тип ХС.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: BusinessEntityTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class ControlSampleIndicator(BaseModel):
    """
    Наличие контрольного образца.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: ControlSampleIndicatorContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
        group: Группы, в состав которых входит страна.
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
    group: list[CountryGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class DocumentNature(BaseModel):
    """
    Природа (тип) документа.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: DocumentNatureContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class DocumentType(BaseModel):
    """
    Тип документа.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: DocumentTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class DrugActiveSubstance(GenericVersioningEntity):
    """
    Действующее вещество лекарственного препарата.

    Attributes:
        name: Наименование действующего вещества
        scientific_name: Научное наименование действующего вещества
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
    scientific_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "scientificName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
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


class EnterpriseActivityType(BaseModel):
    """
    Вид аттестованной деятельности.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: EnterpriseActivityTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class EnterpriseRole(BaseModel):
    """
    Тип, описывающий роль предприятия.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: EnterpriseRoleContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class EnterpriseStatus(BaseModel):
    """
    Тип, описывающий статус предприятия в реестре.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: EnterpriseStatusContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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


class IndicatorGroup(GenericVersioningEntity):
    """
    Группа показателей безопасности.

    Attributes:
        name: Наименование группы показателей
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


class IntendedUse(BaseModel):
    """
    Тип, описывающий назначение партии продукции.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: IntendedUseContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class LabSampleMaterialGroup(GenericVersioningEntity):
    """
    Группа материалов пробы для лабораторных исследований.

    Attributes:
        name: Наименование группы материалов
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


class PackageLevelType(BaseModel):
    """
    Тип, описывающий уровень упаковки.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: PackageLevelTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class PackingCodeType(BaseModel):
    """Тип для представления Packing Code в соответствии с
    "ЕК 013-2010 (ред.1) - Классификатор видов груза, упаковки и упаковочных материалов".
    См. https://eomi.eaeunion.org/ru/#/repository/nsi/173

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: PackingCodeTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class ProductMarkingClass(BaseModel):
    """
    Тип, описывающий тип маркировки.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: ProductMarkingClassContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
    class_value: ProductMarkingClassContentType = field(
        default=ProductMarkingClassContentType.UNDEFINED,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    class_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "className",
            "type": "Attribute",
        },
    )


class ProductTypeInternalType(BaseModel):
    """
    Тип, описывающий тип продукции.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    class Meta:
        name = "ProductType"

    model_config = ConfigDict(defer_build=True)
    value: ProductTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class ProsperityType(BaseModel):
    """
    Статус благополучия.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: ProsperityTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class ReferenceType(BaseModel):
    """
    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: ReferenceTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class RegionalizationDecision(BaseModel):
    """
    Вид требования: перемещение запрещено, перемещение разрешено или перемещение
    разрешено при обязательном соблюдении условий.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: RegionalizationDecisionContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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


class ResearchResult(BaseModel):
    """
    Результат лабораторного исследования/ВСЭ.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: ResearchResultContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class SampleReturnType(BaseModel):
    """
    Тип возврата пробы.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: SampleReturnTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class SamplingReasonType(BaseModel):
    """
    Типы оснований для проведения лабораторных исследований.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: SamplingReasonTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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


class SupervisedObjectActivityInternalType(GenericEntity):
    """
    Вид деятельности поднадзорного объекта.

    Attributes:
        name: Наименование вида деятельности.
    """

    class Meta:
        name = "SupervisedObjectActivity"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class SupervisedObjectStatus(BaseModel):
    """
    Тип, описывающий статус поднадзорного объекта в реестре.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: SupervisedObjectStatusContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class SupervisedObjectType(GenericVersioningEntity):
    """
    Вид поднадзорного объекта.

    Attributes:
        name: Наименование вида поднадзорного объекта.
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


class TransferType(BaseModel):
    """
    Тип транспортировки.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: TransferTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class TransportType(BaseModel):
    """
    Тип транспорта.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: TransportTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class TransportationStorageType(BaseModel):
    """
    Способ хранения при перевозке.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: TransportationStorageTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
        name_en: Наименование единицы измерения (англ.)
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
    name_en: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameEn",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )


class Vatmode(BaseModel):
    """
    НДС включен в сумму.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    class Meta:
        name = "VATMode"

    model_config = ConfigDict(defer_build=True)
    value: VatmodeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class VaccinationType(BaseModel):
    """
    Статус применения вакцины.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: VaccinationTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class VeterinaryServiceType(BaseModel):
    """
    Вид ветеринарной услуги.

    Attributes:
        value:
        list_id: Идентификатор списка возможных значений (справочника)
        list_agency_id: Идентификатор организации-держателя справочника
        list_name: Наименование списка возможных значений (справочника)
        list_version_id: Версия списка возможных значений (справочника)
        name: Наименование соответствующего объекта (элемента
            справочника)
    """

    model_config = ConfigDict(defer_build=True)
    value: VeterinaryServiceTypeContentType = field(
        metadata={
            "required": True,
        }
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listID",
            "type": "Attribute",
        },
    )
    list_agency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listAgencyID",
            "type": "Attribute",
        },
    )
    list_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "listName",
            "type": "Attribute",
        },
    )
    list_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listVersionID",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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


class LookupScope(BaseModel):
    class Meta:
        name = "lookupScope"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
    value: RegistryLookupScope = field(
        metadata={
            "required": True,
        }
    )


class AnimalBreedInternalType(GenericVersioningEntity):
    """
    Порода животного.

    Attributes:
        name: Наименование породы
        species: &gt;Биологический вид животного
    """

    class Meta:
        name = "AnimalBreed"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    species: Optional[AnimalSpeciesInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
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


class AnimalKeepingPurposeListInternalType(EntityList):
    """
    Список целей содержания животных.
    """

    class Meta:
        name = "AnimalKeepingPurposeList"

    model_config = ConfigDict(defer_build=True)
    animal_keeping_purpose: list[AnimalKeepingPurposeInternalType] = field(
        default_factory=list,
        metadata={
            "name": "animalKeepingPurpose",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class AnimalKeepingTypeListInternalType(EntityList):
    """
    Список типов содержания животных.
    """

    class Meta:
        name = "AnimalKeepingTypeList"

    model_config = ConfigDict(defer_build=True)
    animal_keeping_type: list[AnimalKeepingTypeInternalType] = field(
        default_factory=list,
        metadata={
            "name": "animalKeepingType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class AnimalMarkingLocationListInternalType(EntityList):
    """
    Список мест прикрепления/нанесения/вживления средства маркирования.
    """

    class Meta:
        name = "AnimalMarkingLocationList"

    model_config = ConfigDict(defer_build=True)
    animal_marking_location: list[AnimalMarkingLocationInternalType] = field(
        default_factory=list,
        metadata={
            "name": "animalMarkingLocation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class AnimalSpeciesListInternalType(EntityList):
    """
    Тип, описывающий список биологических видов животных.
    """

    class Meta:
        name = "AnimalSpeciesList"

    model_config = ConfigDict(defer_build=True)
    animal_species: list[AnimalSpeciesInternalType] = field(
        default_factory=list,
        metadata={
            "name": "animalSpecies",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class ClassificationAttribute(AdditionalAttribute):
    """
    Классификация объекта/процесса.

    Attributes:
        class_code: Код значения класса
        class_name: Наименование / значение класса
        class_value: Значение класса
    """

    model_config = ConfigDict(defer_build=True)
    class_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    class_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "className",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "classValue",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class ComplexMeasure(BaseModel):
    """Сложное значение измерения, например, вес или объём продукции.

    Включает в себя значение и единицу измерения. Может быть задано как
    точное значение или диапазон (открытый или закрытый).

    Attributes:
        value: Точное значение.
        min_value: Минимальное значение.
        max_value: Максимальное значение.
        unit: Единица измерения.
    """

    model_config = ConfigDict(defer_build=True)
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "fraction_digits": 6,
        },
    )
    min_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "minValue",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "fraction_digits": 6,
        },
    )
    max_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "maxValue",
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


class CountryGroup(GenericVersioningEntity):
    """
    Тип, описывающий группу страну.

    Attributes:
        name: Название группы стран.
        english_name: Английское название группы стран.
        code: Двухбуквенный код группы стран (при наличии),
            соответствующий стандарту ISO 3166-1.
        country: Страны, входящий в состав группы
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
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 2,
        },
    )
    country: list[CountryInternalType] = field(
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


class Indicator(GenericVersioningEntity):
    """
    Показатель безопасности.

    Attributes:
        name: Наименование показателя
        group: Группа показателей
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
    group: Optional[IndicatorGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class LabSampleMaterial(GenericVersioningEntity):
    """
    Материал пробы для лабораторных исследований.

    Attributes:
        name: Наименование материала
        group: Группа материалов
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
    group: Optional[LabSampleMaterialGroup] = field(
        default=None,
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


class Measure(BaseModel):
    """Значение измерения, например, вес или объём продукции.

    Включает в себя значение и единицу измерения.

    Attributes:
        value: Значение.
        unit: Единица измерения.
    """

    model_config = ConfigDict(defer_build=True)
    value: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
            "fraction_digits": 6,
        }
    )
    unit: UnitInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
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
    Тип, описывающий направление груза.

    Attributes:
        name: Наименование направления.
        for_substandard: Назначение для некачественных грузов.
        intended_use: Назначение груза, к которому относится данное
            направление.
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
    intended_use: Optional[IntendedUse] = field(
        default=None,
        metadata={
            "name": "intendedUse",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class RegionInternalType(AddressObjectView):
    """
    Тип региона страны (обычно первый уровень в адресной структуре).

    Attributes:
        iso_code: Код региона в соответствии с ISO 3166-2
    """

    class Meta:
        name = "Region"

    model_config = ConfigDict(defer_build=True)
    iso_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "isoCode",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "pattern": r"[A-Z]{2}-[A-Z0-9]{1,3}",
        },
    )


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


class SamplingReason(GenericEntity):
    """
    Основание для проведения лабораторных исследований.

    Attributes:
        reason_type: Основание.
        reason_name: Наименование / описание основания.
    """

    model_config = ConfigDict(defer_build=True)
    reason_type: Optional[SamplingReasonType] = field(
        default=None,
        metadata={
            "name": "reasonType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    reason_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "reasonName",
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


class SupervisedObjectActivityListInternalType(EntityList):
    """
    Тип, описывающий список видов деятельности поднадзорных объектов.
    """

    class Meta:
        name = "SupervisedObjectActivityList"

    model_config = ConfigDict(defer_build=True)
    activity: list[SupervisedObjectActivityInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class SupervisedObjectTypeListInternalType(EntityList):
    """
    Тип, описывающий список видов поднадзорных объектов.
    """

    class Meta:
        name = "SupervisedObjectTypeList"

    model_config = ConfigDict(defer_build=True)
    object_type: list[SupervisedObjectType] = field(
        default_factory=list,
        metadata={
            "name": "objectType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class TransportTypeList(BaseModel):
    """
    Список типов транспорта.
    """

    model_config = ConfigDict(defer_build=True)
    transport_type: list[TransportType] = field(
        default_factory=list,
        metadata={
            "name": "transportType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_occurs": 10,
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


class UnmeasuredAttribute(AdditionalAttribute):
    """
    Неизмеримая характеристика объекта/процесса.

    Attributes:
        attr_value: Значение неизмеримой характеристики
    """

    model_config = ConfigDict(defer_build=True)
    attr_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "attrValue",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class VeterinaryService(GenericEntity):
    """
    Услуга, оказываемая ветеринарным учреждением (лабораторией).

    Attributes:
        service_type: Вид ветеринарной услуги.
        service_name: Наименование услуги.
    """

    model_config = ConfigDict(defer_build=True)
    service_type: Optional[VeterinaryServiceType] = field(
        default=None,
        metadata={
            "name": "serviceType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    service_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )


class AnimalKeepingPurpose(AnimalKeepingPurposeInternalType):
    class Meta:
        name = "animalKeepingPurpose"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalKeepingType(AnimalKeepingTypeInternalType):
    class Meta:
        name = "animalKeepingType"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalMarkingLocation(AnimalMarkingLocationInternalType):
    class Meta:
        name = "animalMarkingLocation"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalPlaceKind(AnimalPlaceKindInternalType):
    class Meta:
        name = "animalPlaceKind"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalSpecies(AnimalSpeciesInternalType):
    class Meta:
        name = "animalSpecies"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


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


class ProductType(ProductTypeInternalType):
    class Meta:
        name = "productType"
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


class SupervisedObjectActivity(SupervisedObjectActivityInternalType):
    class Meta:
        name = "supervisedObjectActivity"
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


class AnimalBreedListInternalType(EntityList):
    """
    Тип, описывающий список пород животных.
    """

    class Meta:
        name = "AnimalBreedList"

    model_config = ConfigDict(defer_build=True)
    animal_breed: list[AnimalBreedInternalType] = field(
        default_factory=list,
        metadata={
            "name": "animalBreed",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class AnimalProductivity(BaseModel):
    """
    Сведения о продуктивности животного.

    Attributes:
        product_type: Тип получаемой продукции
        product: Получаемая продукции
        sub_product: Вид получаемой продукции
        output: Значение продуктивности животного по указанному виду
            продукции
    """

    model_config = ConfigDict(defer_build=True)
    product_type: Optional[PackingType] = field(
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
    output: Optional[ComplexMeasure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class CertificationZone(BaseModel):
    """
    Зона аттестации предприятия.

    Attributes:
        country_group: Группа стран
        country: Страна
    """

    model_config = ConfigDict(defer_build=True)
    country_group: list[CountryGroup] = field(
        default_factory=list,
        metadata={
            "name": "countryGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    country: list[CountryInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class CertifiedActivity(BaseModel):
    """
    Аттестованная деятельность предприятия.

    Attributes:
        product_type: Тип продукции
        product: Продукция
        sub_product: Вид продукции
        activity: Вид деятельности
    """

    model_config = ConfigDict(defer_build=True)
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
    activity: list[EnterpriseActivityType] = field(
        default_factory=list,
        metadata={
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


class MeasuredAttribute(AdditionalAttribute):
    """
    Измеримая характеристика объекта/процесса.

    Attributes:
        attr_value: Значение измеримой характеристики
    """

    model_config = ConfigDict(defer_build=True)
    attr_value: Optional[ComplexMeasure] = field(
        default=None,
        metadata={
            "name": "attrValue",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
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


class SamplingReasonList(EntityList):
    """Тип, описывающий список оснований для проведения лаб.

    исследований.
    """

    model_config = ConfigDict(defer_build=True)
    sampling_reason: list[SamplingReason] = field(
        default_factory=list,
        metadata={
            "name": "samplingReason",
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


class UnifiedAnimalId(BaseModel):
    """
    Сведения об УНСМ (уникальный номер средства маркирования)

    Attributes:
        animal_id: Номер средства маркирования в соответствии с форматом
        type_value: Тип средства маркирования
        status: Статус номера средства маркирования
        region: Регион, в котором зарегистрирован номер средства
            маркирования
        emission_date: Дата выпуска номера средства маркирования
        producing_date: Дата производства средства маркирования с данным
            номером
        attachment_date: Дата нанесения / прикрепления номера средства
            маркирования
        expired_date: Дата вывода номера средства маркирования из
            оборота
    """

    class Meta:
        name = "UnifiedAnimalID"

    model_config = ConfigDict(defer_build=True)
    animal_id: list[AnimalId] = field(
        default_factory=list,
        metadata={
            "name": "animalID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    type_value: Optional[AnimalMarkingMeansType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    status: Optional[AnimalIdstatus] = field(
        default=None,
        metadata={
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
    emission_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "emissionDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    producing_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "producingDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    attachment_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "attachmentDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    expired_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "expiredDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class VeterinaryServiceList(EntityList):
    """
    Тип, описывающий список услуг, оказываемых ветеринарным учреждением
    (лабораторией).
    """

    model_config = ConfigDict(defer_build=True)
    service: list[VeterinaryService] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class AnimalBreed(AnimalBreedInternalType):
    class Meta:
        name = "animalBreed"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalKeepingPurposeList(AnimalKeepingPurposeListInternalType):
    class Meta:
        name = "animalKeepingPurposeList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalKeepingTypeList(AnimalKeepingTypeListInternalType):
    class Meta:
        name = "animalKeepingTypeList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalMarkingLocationList(AnimalMarkingLocationListInternalType):
    class Meta:
        name = "animalMarkingLocationList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalSpeciesList(AnimalSpeciesListInternalType):
    class Meta:
        name = "animalSpeciesList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


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


class SupervisedObjectActivityList(SupervisedObjectActivityListInternalType):
    class Meta:
        name = "supervisedObjectActivityList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class SupervisedObjectTypeList(SupervisedObjectTypeListInternalType):
    class Meta:
        name = "supervisedObjectTypeList"
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


class BorderVetControlPostInternalType(GenericVersioningEntity):
    """
    Пограничный ветеринарный контрольный пункт (ПВКП)

    Attributes:
        name: Сокращенное название ПВКП.
        full_name: Полное название ПВКП.
        transport_type: Тип транспорта пункта пропуска: - автомобильный,
            - железнодорожный, - авиационный, - морской.
        address: Адрес пункта пропуска.
    """

    class Meta:
        name = "BorderVetControlPost"

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
    transport_type: Optional[TransportType] = field(
        default=None,
        metadata={
            "name": "transportType",
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
    Базовый тип, описывающий место отгрузки, перегрузки или хранения груза.

    Attributes:
        name: Название пункта перегрузки.
        address: Название пункта перегрузки.
        name_en: Название пункта перегрузки (англ.)
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
    name_en: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameEn",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
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
        name_en: Наименование учреждения (англ.)
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
    name_en: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameEn",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
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


class ProductItemCharacterictics(BaseModel):
    """
    Дополнительные характеристики наименования продукции.
    """

    model_config = ConfigDict(defer_build=True)
    classification: list[ClassificationAttribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    attribute: list[MeasuredAttribute] = field(
        default_factory=list,
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


class UnifiedAnimalIdlist(EntityList):
    """
    Тип, описывающий список УНСМ (уникальный номер средства маркирования)
    """

    class Meta:
        name = "UnifiedAnimalIDList"

    model_config = ConfigDict(defer_build=True)
    animal_idcontent: list[UnifiedAnimalId] = field(
        default_factory=list,
        metadata={
            "name": "animalIDContent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class VeterinaryLaboratory(GenericVersioningEntity):
    """
    Ветеринарная лаборатория.

    Attributes:
        name: Наименование лаборатории.
        full_name: Полное наименование лаборатории.
        address: Адрес лаборатории.
        service_list: Список услуг, оказываемых лабораториями.
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
    full_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fullName",
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
    service_list: Optional[VeterinaryServiceList] = field(
        default=None,
        metadata={
            "name": "serviceList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class AnimalBreedList(AnimalBreedListInternalType):
    class Meta:
        name = "animalBreedList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


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


class AnimalGeneticPassport(BaseModel):
    """
    Сведения о генетическом паспорте животного.

    Attributes:
        data: Данные генетической идентификации
        conclusion: Заключение / результат генетической идентификации
        sample_storage_location: Место хранения пробы генетического
            материала
    """

    model_config = ConfigDict(defer_build=True)
    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    conclusion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    sample_storage_location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "sampleStorageLocation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class ApprovalStatement(BaseModel):
    """
    Акт обследования предприятия.

    Attributes:
        name: Название документа.
        issue_series: Серия документа.
        issue_number: Номер документа.
        issue_date: Дата документа.
        issuer: Организация, оформившая документ.
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
    issue_series: Optional[str] = field(
        default=None,
        metadata={
            "name": "issueSeries",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    issue_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "issueNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    issuer: Optional[Organization] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class BorderVetControlPostListInternalType(EntityList):
    """
    Тип, описывающий список ветеринарных пунктов пропуска.
    """

    class Meta:
        name = "BorderVetControlPostList"

    model_config = ConfigDict(defer_build=True)
    border_vet_control_post: list[BorderVetControlPostInternalType] = field(
        default_factory=list,
        metadata={
            "name": "borderVetControlPost",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


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


class FishingLocationInternalType(Location):
    """
    Район промысла (ВБР).

    Attributes:
        fao_code: Номер ФАО.
    """

    class Meta:
        name = "FishingLocation"

    model_config = ConfigDict(defer_build=True)
    fao_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "faoCode",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
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


class VeterinaryLaboratoryListInternalType(EntityList):
    """
    Тип, описывающий список лабораторий.
    """

    class Meta:
        name = "VeterinaryLaboratoryList"

    model_config = ConfigDict(defer_build=True)
    veterinary_laboratory: list[VeterinaryLaboratory] = field(
        default_factory=list,
        metadata={
            "name": "veterinaryLaboratory",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class BorderVetControlPost(BorderVetControlPostInternalType):
    class Meta:
        name = "borderVetControlPost"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


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
        name_en: Наименование хозяйствующего субъекта (англ.)
        registry_status: Статус хозяйствующего субъекта в реестре ИС
            Цербер.
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
    name_en: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameEn",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    registry_status: Optional[BusinessEntityStatus] = field(
        default=None,
        metadata={
            "name": "registryStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class ProducerAuthentication(BaseModel):
    """
    Аттестация предприятия.

    Attributes:
        certified_activity: Аттестованный вид деятельности
        certification_zone: Зона аттестации предприятия.
        status: Действующий статус аттестации.
        approval_date: Дата установления статуса.
        approval_document: Акт обследования предприятия, подтверждающий
            аттестацию предприятия.
    """

    model_config = ConfigDict(defer_build=True)
    certified_activity: Optional[CertifiedActivity] = field(
        default=None,
        metadata={
            "name": "certifiedActivity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    certification_zone: list[CertificationZone] = field(
        default_factory=list,
        metadata={
            "name": "certificationZone",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    status: Optional[ApprovalStatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    approval_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "approvalDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    approval_document: Optional[ApprovalStatement] = field(
        default=None,
        metadata={
            "name": "approvalDocument",
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


class BorderVetControlPostList(BorderVetControlPostListInternalType):
    class Meta:
        name = "borderVetControlPostList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class EnterpriseList(EnterpriseListInternalType):
    class Meta:
        name = "enterpriseList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class FishingLocation(FishingLocationInternalType):
    class Meta:
        name = "fishingLocation"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class VeterinaryLaboratoryList(VeterinaryLaboratoryListInternalType):
    class Meta:
        name = "veterinaryLaboratoryList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class BankAccountDetails(BaseModel):
    """
    Тип, описывающий банковские реквизиты ХС.

    Attributes:
        payment_account_number: Рассчетный счет.
        correspondent_account_number: Корреспондетский счет.
        bic: БИК.
        bank_name: Наименование банка.
        payment_recipient: Получатель платежа.
    """

    model_config = ConfigDict(defer_build=True)
    payment_account_number: str = field(
        metadata={
            "name": "paymentAccountNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
            "pattern": r"[0-9]{20}",
        }
    )
    correspondent_account_number: str = field(
        metadata={
            "name": "correspondentAccountNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
            "pattern": r"[0-9]{20}",
        }
    )
    bic: str = field(
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
            "pattern": r"[0-9]{9}",
        }
    )
    bank_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "bankName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    payment_recipient: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "name": "paymentRecipient",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


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


class BusinessMemberInternalType(GenericVersioningEntity):
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
        additional_characteristics: Дополнительные характеристики
            наименования продукции.
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
    additional_characteristics: Optional[ProductItemCharacterictics] = field(
        default=None,
        metadata={
            "name": "additionalCharacteristics",
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


class BusinessMemberListInternalType(EntityList):
    """
    Тип, описывающий список поднадзорных объектов.
    """

    class Meta:
        name = "BusinessMemberList"

    model_config = ConfigDict(defer_build=True)
    business_member: list[BusinessMemberInternalType] = field(
        default_factory=list,
        metadata={
            "name": "businessMember",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class MedicinalDrug(GenericVersioningEntity):
    """
    Препарат/вакцина.

    Attributes:
        id: Идентификационный (уникальный) номер препарата
        name: Наименование препарата
        series: Номер серии препарата/вакцины
        producer: Производитель препарата
        active_substance: Действующее вещество препарата
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
    active_substance: list[DrugActiveSubstance] = field(
        default_factory=list,
        metadata={
            "name": "activeSubstance",
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


class SupervisedObjectInternalType(BusinessMemberInternalType):
    """
    Поднадзорный объект.

    Attributes:
        approval_number: Регистрационный номер предприятия в реестре
            поднадзорных объектов.
        approved_name: Наименование предприятия (поднадзорного объекта),
            установленное при включении в реестр.
        approved_name_en: Наименование предприятия (поднадзорного
            объекта) на англ.языке, установленное при включении в
            реестр. Для поднадзорных объектов, включенных в реестр
            аттестованных предприятий является обязательным.
        authentication: Сведения об аттестации предприятия (при
            наличии). Для поднадзорных объектов, включенных в реестр
            аттестованных предприятий является обязательным.
        object_type: Вид поднадзорного объекта
        activity: Вид деятельности поднадзорного объекта
        registry_status: Статус поднадзорного в реестре ИС Цербер.
    """

    class Meta:
        name = "SupervisedObject"

    model_config = ConfigDict(defer_build=True)
    approval_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "approvalNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 100,
        },
    )
    approved_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "approvedName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    approved_name_en: Optional[str] = field(
        default=None,
        metadata={
            "name": "approvedNameEn",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    authentication: list[ProducerAuthentication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    object_type: Optional[SupervisedObjectType] = field(
        default=None,
        metadata={
            "name": "objectType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    activity: list[SupervisedObjectActivityInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    registry_status: Optional[SupervisedObjectStatus] = field(
        default=None,
        metadata={
            "name": "registryStatus",
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


class AnimalKeepingLocation(BaseModel):
    """
    Сведения о месте рождения/содержания животного.

    Attributes:
        location: Место содержания животного
        supervised_object: Поднадзорный объект, на котором
            осуществляется содержание животного
    """

    model_config = ConfigDict(defer_build=True)
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    supervised_object: Optional[SupervisedObjectInternalType] = field(
        default=None,
        metadata={
            "name": "supervisedObject",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class AnimalMarkingMeans(BaseModel):
    """
    Сведения о средстве маркирования.

    Attributes:
        type_value: Тип средства маркирования
        producer: Производитель средства маркирования
    """

    model_config = ConfigDict(defer_build=True)
    type_value: Optional[AnimalMarkingMeansType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    producer: Optional[SupervisedObjectInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class CertifiedProducerInternalType(SupervisedObjectInternalType):
    """Производитель продукции, аттестованный на поставки в страну или группу
    стран.

    Реестр аттестованных предприятий является подмножеством реестра
    поднадзорных объектов компонента Цербер ФГИС ВетИС.
    """

    class Meta:
        name = "CertifiedProducer"

    model_config = ConfigDict(defer_build=True)


class StoragePointInternalType(BaseModel):
    """
    Место хранения / отгрузки.

    Attributes:
        location: Место хранения / отгрузки (текстовое представление)
        enterprise: Место хранения / отгрузки (площадка)
        supervised_object: Место хранения / отгрузки (поднадзорный
            объект)
        animal_place_kind: Вид размещения живых животных
    """

    class Meta:
        name = "StoragePoint"

    model_config = ConfigDict(defer_build=True)
    location: Optional[Location] = field(
        default=None,
        metadata={
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
    supervised_object: Optional[SupervisedObjectInternalType] = field(
        default=None,
        metadata={
            "name": "supervisedObject",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    animal_place_kind: list[AnimalPlaceKindInternalType] = field(
        default_factory=list,
        metadata={
            "name": "animalPlaceKind",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class SupervisedObjectListInternalType(EntityList):
    """
    Тип, описывающий список поднадзорных объектов.
    """

    class Meta:
        name = "SupervisedObjectList"

    model_config = ConfigDict(defer_build=True)
    supervised_object: list[SupervisedObjectInternalType] = field(
        default_factory=list,
        metadata={
            "name": "supervisedObject",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class Vaccine(MedicinalDrug):
    """
    Вакцина.
    """

    model_config = ConfigDict(defer_build=True)


class ActivityLocationList(ActivityLocationListInternalType):
    class Meta:
        name = "activityLocationList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class BusinessMemberList(BusinessMemberListInternalType):
    class Meta:
        name = "businessMemberList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class ProductItemList(ProductItemListInternalType):
    class Meta:
        name = "productItemList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class SupervisedObject(SupervisedObjectInternalType):
    class Meta:
        name = "supervisedObject"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalLabel(BaseModel):
    """
    Сведения о маркировке животного (группы животных)

    Attributes:
        animal_id: Номер, нанесенный на животное тем или иным способом с
            помощью средства маркирования, позволяющий идентифицирующий
            животное (группу животных). В качестве идентификационного
            номера может применяться Уникальный номер средства
            маркирования в соответствии с Правилами идентификации или
            другой номер, обеспечивающий идентификацию животного (группу
            животных).
        type_value: Вид маркировки: основная/дополнительная
        marking_means: Cредство маркирования
        attachment_date: Дата нанесения/прикрепления средства
            маркирования
        attachment_location: Место нанесения/прикрепления
        expired_date: Дата окончания срока действия/годности средства
            маркирования
        description: (Достаточно 255?)
        photo: Фотография средства маркирования
    """

    model_config = ConfigDict(defer_build=True)
    animal_id: Optional[AnimalId] = field(
        default=None,
        metadata={
            "name": "animalID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    type_value: Optional[AnimalLabelType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    marking_means: Optional[AnimalMarkingMeans] = field(
        default=None,
        metadata={
            "name": "markingMeans",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    attachment_date: Optional[ComplexDate] = field(
        default=None,
        metadata={
            "name": "attachmentDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    attachment_location: Optional[AnimalMarkingLocationInternalType] = field(
        default=None,
        metadata={
            "name": "attachmentLocation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    expired_date: Optional[ComplexDate] = field(
        default=None,
        metadata={
            "name": "expiredDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "max_length": 255,
        },
    )
    photo: list[File] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class CertifiedProducerListInternalType(EntityList):
    """
    Тип, описывающий список поднадзорных объектов, включенных в реестр
    аттестованных предприятий.
    """

    class Meta:
        name = "CertifiedProducerList"

    model_config = ConfigDict(defer_build=True)
    producer: list[CertifiedProducerInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class StoragePointListInternalType(EntityList):
    """
    Список мест хранения отгрузки.
    """

    class Meta:
        name = "StoragePointList"

    model_config = ConfigDict(defer_build=True)
    storage_point: list[StoragePointInternalType] = field(
        default_factory=list,
        metadata={
            "name": "storagePoint",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class CertifiedProducer(CertifiedProducerInternalType):
    class Meta:
        name = "certifiedProducer"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class StoragePoint(StoragePointInternalType):
    class Meta:
        name = "storagePoint"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class SupervisedObjectList(SupervisedObjectListInternalType):
    class Meta:
        name = "supervisedObjectList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class Animal(BaseModel):
    """
    Животное.

    Attributes:
        species: Биологический вид животного
        breed: Порода животного
        colour: Масть/окрас животного
        gender: Пол животного
        name: Кличка животного
        age: Возраст
        weight: Вес животного
        birth_date: Дата рождения животного
        death_date: Дата убоя/падежа животного
        birth_location: Место рождения
        specified_animal_label: Сведения о маркировке животного
        classification: Дополнительное свойство животного
        attribute: Дополнительная характеристика животного
        photo: Фотография животного
    """

    model_config = ConfigDict(defer_build=True)
    species: Optional[AnimalSpeciesInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    breed: Optional[AnimalBreedInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    colour: Optional[AnimalColour] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    gender: Optional[AnimalGender] = field(
        default=None,
        metadata={
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
    age: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    weight: Optional[Measure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    birth_date: Optional[ComplexDate] = field(
        default=None,
        metadata={
            "name": "birthDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    death_date: Optional[ComplexDate] = field(
        default=None,
        metadata={
            "name": "deathDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    birth_location: Optional[AnimalKeepingLocation] = field(
        default=None,
        metadata={
            "name": "birthLocation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    specified_animal_label: list[AnimalLabel] = field(
        default_factory=list,
        metadata={
            "name": "specifiedAnimalLabel",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    classification: list[ClassificationAttribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    attribute: list[MeasuredAttribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    photo: Optional[File] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class AnimalGroup(BaseModel):
    """
    Группа животных.

    Attributes:
        species: Биологический вид животных
        breed: Порода животных
        gender: Пол животных
        size: Численность группы животных
        weight: Суммарный вес животных
        birth_date_period: Интервал дат рождения животных
        death_date_period: Интервал дат убоя/падежа животных
        specified_animal_label: Сведения о маркировке животного
        classification: Дополнительное свойство животного
        attribute: Дополнительная характеристика животного
    """

    model_config = ConfigDict(defer_build=True)
    species: Optional[AnimalSpeciesInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    breed: Optional[AnimalBreedInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    gender: Optional[AnimalGender] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    size: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    weight: Optional[Measure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    birth_date_period: Optional[ComplexDatePeriod] = field(
        default=None,
        metadata={
            "name": "birthDatePeriod",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    death_date_period: Optional[ComplexDatePeriod] = field(
        default=None,
        metadata={
            "name": "deathDatePeriod",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    specified_animal_label: list[AnimalLabel] = field(
        default_factory=list,
        metadata={
            "name": "specifiedAnimalLabel",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    classification: list[ClassificationAttribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    attribute: list[MeasuredAttribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class CertifiedProducerList(CertifiedProducerListInternalType):
    class Meta:
        name = "certifiedProducerList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)


class StoragePointList(StoragePointListInternalType):
    class Meta:
        name = "storagePointList"
        namespace = "http://api.vetrf.ru/schema/cdm/dictionary/v2"

    model_config = ConfigDict(defer_build=True)
