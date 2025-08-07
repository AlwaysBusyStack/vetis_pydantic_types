from __future__ import annotations

from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate, XmlDateTime

from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.herriot.types.production.base_v2_1 import (
    ComplexDate,
    ComplexDatePeriod,
    DateInterval,
    EntityList,
    GenericEntity,
    GenericVersioningEntity,
    RegisterModificationType,
)
from vetis_pydantic_types.herriot.types.production.codelist_v2_5r4 import (
    AnimalIdentificationEventTypeContentType,
    AnimalIdentityStatusContentType,
    AnimalIdentityTypeContentType,
    AnimalMarkingEventReasonContentType,
    AnimalMedicationEventReasonContentType,
    AnimalRegistrationStatusContentType,
    AnimalSpentPeriodContentType,
    FmpregistryStatusContentType,
    NonFoodProductSourceTypeContentType,
    PermitDecisionContentType,
    PharmaceuticalTypeContentType,
    ProcessingProcedureTypeContentType,
    SamplingReportStatusContentType,
    VetDocumentFormContentType,
    VetDocumentStatusContentType,
    VetDocumentTypeContentType,
    VeterinaryEventStatusContentType,
    VeterinaryEventTypeContentType,
    WbrcomplianceDecisionContentType,
)
from vetis_pydantic_types.herriot.types.production.dictionary_v2_5 import (
    Animal,
    AnimalBreedingValueType,
    AnimalDisease,
    AnimalGeneticPassport,
    AnimalGroup,
    AnimalId,
    AnimalKeepingLocation,
    AnimalKeepingPurposeInternalType,
    AnimalKeepingTypeInternalType,
    AnimalLabel,
    AnimalProductivity,
    Area,
    BankAccountDetails,
    BorderVetControlPostListInternalType,
    BusinessEntityInternalType,
    BusinessEntityListInternalType,
    BusinessMemberInternalType,
    CertifiedProducerInternalType,
    CertifiedProducerListInternalType,
    ClassificationAttribute,
    ControlSampleIndicator,
    CountryInternalType,
    DistrictInternalType,
    DocumentNature,
    DocumentType,
    DrugActiveSubstance,
    EnterpriseInternalType,
    EnterpriseListInternalType,
    Indicator,
    LabSampleMaterial,
    Locality,
    Location,
    Measure,
    MeasuredAttribute,
    MedicinalDrug,
    Organization,
    PackageList,
    PackingType,
    ProducerInternalType,
    ProductInternalType,
    ProductItemInternalType,
    ProductItemListInternalType,
    ProductTypeInternalType,
    PurposeInternalType,
    ReferenceType,
    RegionalizationCondition,
    RegionalizationShippingRule,
    RegionInternalType,
    ResearchMethodInternalType,
    ResearchResult,
    SampleReturnType,
    SamplingReasonList,
    StoragePointInternalType,
    SubProductInternalType,
    SupervisedObjectInternalType,
    TextCondition,
    TransferType,
    TransportationStorageType,
    TransportType,
    TransportTypeList,
    UnitInternalType,
    UnmeasuredAttribute,
    Vaccine,
    Vatmode,
    VeterinaryLaboratory,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"


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


class AnimalIdentificationEventType(BaseModel):
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
    value: AnimalIdentificationEventTypeContentType = field(
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


class AnimalIdentityStatus(BaseModel):
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
    value: AnimalIdentityStatusContentType = field(
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


class AnimalIdentityStatusChangeReason(GenericVersioningEntity):
    """
    Основание изменения статуса сведений об идентификации.

    Attributes:
        name: Наименование причины изменения статуса
        description: Описание причины изменения статуса
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
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalIdentityType(BaseModel):
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
    value: AnimalIdentityTypeContentType = field(
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


class AnimalLifecycleEventReason(GenericVersioningEntity):
    """
    Основание (причина) события с животным или группой животных.

    Attributes:
        name: Наименование причины
        description: Описание причины
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
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalMarkingEventReason(BaseModel):
    """
    Тип, описывающий основание.

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
    value: AnimalMarkingEventReasonContentType = field(
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


class AnimalMedicationEventReason(BaseModel):
    """
    Тип, описывающий основание.

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
    value: AnimalMedicationEventReasonContentType = field(
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


class AnimalRegistrationStatus(BaseModel):
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
    value: AnimalRegistrationStatusContentType = field(
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


class AnimalRegistrationStatusChangeReason(GenericVersioningEntity):
    """
    Основание изменения статуса карточки животного.

    Attributes:
        name: Наименование причины изменения статуса
        description: Описание причины изменения статуса
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
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalSpentPeriod(BaseModel):
    """
    Сколько времени животные находились на территории ТС.

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
    value: AnimalSpentPeriodContentType = field(
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


class ControlSample(BaseModel):
    """
    Контрольный образец.

    Attributes:
        affixed_seal: Номер пломбы / сейф-пакета контрольного образца.
        control_sample_volume: Объем контрольного образца.
    """

    model_config = ConfigDict(defer_build=True)
    affixed_seal: Optional[str] = field(
        default=None,
        metadata={
            "name": "affixedSeal",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    control_sample_volume: Optional[Measure] = field(
        default=None,
        metadata={
            "name": "controlSampleVolume",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class DiscrepancyReason(GenericVersioningEntity):
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


class FmpregistryProduct(GenericEntity):
    """
    Тип, описывающий зарегистрированную продукцию; содержит общие для ЛП, ФС, КД и
    КГМО поля.

    Attributes:
        trade_name: Торговое наименование продукции (ЛП, ФС, КД или
            КГМО).
        chemical_name: Международное непатентованное или группировочное,
            или химическое наименование.
        producer: Информация о производителе.
        developer: Информация о разработчике.
        form_of_issue: Форма выпуска.
        product_purpose: Назначение или показания к применению.
        component_composition: Компонентный состав.
    """

    class Meta:
        name = "FMPRegistryProduct"

    model_config = ConfigDict(defer_build=True)
    trade_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "tradeName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    chemical_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "chemicalName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    producer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    developer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    form_of_issue: Optional[str] = field(
        default=None,
        metadata={
            "name": "formOfIssue",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    product_purpose: Optional[str] = field(
        default=None,
        metadata={
            "name": "productPurpose",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    component_composition: Optional[str] = field(
        default=None,
        metadata={
            "name": "componentComposition",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class FmpregistryStatus(BaseModel):
    """
    Тип решения (разрешение, запрет)

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
        name = "FMPRegistryStatus"

    model_config = ConfigDict(defer_build=True)
    value: FmpregistryStatusContentType = field(
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


class NonFoodProductSourceType(BaseModel):
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
    value: NonFoodProductSourceTypeContentType = field(
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


class PermitDecision(BaseModel):
    """
    Тип решения (разрешение, запрет)

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
    value: PermitDecisionContentType = field(
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


class PharmaceuticalType(BaseModel):
    """
    Тип лекарственного средства.

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
    value: PharmaceuticalTypeContentType = field(
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


class ProcessingProcedureType(BaseModel):
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
    value: ProcessingProcedureTypeContentType = field(
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


class ReturnReason(GenericVersioningEntity):
    """
    Причина возврата.

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


class SamplingReportStatus(BaseModel):
    """
    Статус акта отбора проб.

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
    value: SamplingReportStatusContentType = field(
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


class TransferConditionList(BaseModel):
    """
    Список условий транспортировки груза.
    """

    model_config = ConfigDict(defer_build=True)
    condition: list[TextCondition] = field(
        default_factory=list,
        metadata={
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


class VetDocumentForm(BaseModel):
    """
    Тип, описывающий форму ВСД.

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
    value: VetDocumentFormContentType = field(
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


class VetDocumentStatusInternalType(BaseModel):
    """
    Статус ветсертификата.

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
        name = "VetDocumentStatus"

    model_config = ConfigDict(defer_build=True)
    value: VetDocumentStatusContentType = field(
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


class VetDocumentTypeInternalType(BaseModel):
    """
    Тип ветсертификата.

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
        name = "VetDocumentType"

    model_config = ConfigDict(defer_build=True)
    value: VetDocumentTypeContentType = field(
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


class VeterinaryEventStatus(BaseModel):
    """
    Тип, описывающий статус ветеринарного мероприятия.

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
    value: VeterinaryEventStatusContentType = field(
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


class VeterinaryEventStatusChangeReason(GenericVersioningEntity):
    """
    Основание изменения статуса карточки животного.

    Attributes:
        name: Наименование причины изменения статуса
        description: Описание причины изменения статуса
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
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class VeterinaryEventType(BaseModel):
    """
    Тип мероприятия.

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
    value: VeterinaryEventTypeContentType = field(
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


class WbrcomplianceDecision(BaseModel):
    """
    Тип решения в заключении о соответствии уловов ВБР требованиям.

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
        name = "WBRComplianceDecision"

    model_config = ConfigDict(defer_build=True)
    value: WbrcomplianceDecisionContentType = field(
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


class AnimalRegistrationStatusList(EntityList):
    """
    Список статусов регистрационных карточек животных.
    """

    model_config = ConfigDict(defer_build=True)
    registration_status: list[AnimalRegistrationStatus] = field(
        default_factory=list,
        metadata={
            "name": "registrationStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
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


class BatchExtraInfo(BaseModel):
    """
    Дополнительные сведения о партии продукции.

    Attributes:
        non_food_source: Вид проиcхождения для непищевой продукции,
            технического сырья, кормов и кормовых добавок.
        classification:
        attribute:
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
    classification: list[ClassificationAttribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    attribute: list[MeasuredAttribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class ControlSampleList(EntityList):
    """
    Тип, описывающий список контрольных образцов.
    """

    model_config = ConfigDict(defer_build=True)
    control_sample: list[ControlSample] = field(
        default_factory=list,
        metadata={
            "name": "controlSample",
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


class FeedAdditive(FmpregistryProduct):
    """
    Тип, описывающий запись реестра для КД.
    """

    model_config = ConfigDict(defer_build=True)


class GmfeedAdditive(FmpregistryProduct):
    """
    Тип, описывающий запись реестра для КГМО.
    """

    class Meta:
        name = "GMFeedAdditive"

    model_config = ConfigDict(defer_build=True)


class Invoice(Document):
    """
    Счёт на оплату.

    Attributes:
        total_amount: Общая сумма счёта.
        sub_total_amount: Сумма товаров (работ / услуг).
        currency: Валюта счёта.
        vat_mode: НДС включен в сумму.
        vat_rate: Ставка НДС.
        vat_amount: Сумма НДС.
        payment_purpose: Назначение платежа.
        payment_recipient: Банковские реквизиты получателя.
    """

    model_config = ConfigDict(defer_build=True)
    total_amount: Decimal = field(
        metadata={
            "name": "totalAmount",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
            "fraction_digits": 6,
        }
    )
    sub_total_amount: Decimal = field(
        metadata={
            "name": "subTotalAmount",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
            "fraction_digits": 6,
        }
    )
    currency: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
            "pattern": r"[A-Z]{3}",
        }
    )
    vat_mode: Vatmode = field(
        metadata={
            "name": "vatMode",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    vat_rate: Decimal = field(
        metadata={
            "name": "vatRate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
            "total_digits": 5,
            "fraction_digits": 2,
        }
    )
    vat_amount: Decimal = field(
        metadata={
            "name": "vatAmount",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
            "fraction_digits": 6,
        }
    )
    payment_purpose: str = field(
        metadata={
            "name": "paymentPurpose",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
            "max_length": 210,
        }
    )
    payment_recipient: BankAccountDetails = field(
        metadata={
            "name": "paymentRecipient",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class PharmSubstance(FmpregistryProduct):
    """
    Тип, описывающий запись реестра для ФС.
    """

    model_config = ConfigDict(defer_build=True)


class Pharmaceutical(FmpregistryProduct):
    """
    Тип, описывающий запись реестра для ЛП.

    Attributes:
        pharmaceutical_type: Тип лекарственного средства (вакцина или
            прочие лекарственные средства).
    """

    model_config = ConfigDict(defer_build=True)
    pharmaceutical_type: Optional[PharmaceuticalType] = field(
        default=None,
        metadata={
            "name": "pharmaceuticalType",
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


class RegistrationCertificate(Document):
    """
    Свидетельство о регистрации продукции.

    Attributes:
        begin_date: Дата начала действия свидетельства.
        end_date: Дата окончания действия свидетельства.
        unlimited: Свидетельство выдано бессрочно.
        certificate_owner: Кому выдано свидетельство.
    """

    model_config = ConfigDict(defer_build=True)
    begin_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "beginDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    unlimited: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    certificate_owner: Optional[str] = field(
        default=None,
        metadata={
            "name": "certificateOwner",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
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


class VetDocumentStatus(VetDocumentStatusInternalType):
    class Meta:
        name = "vetDocumentStatus"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class VetDocumentType(VetDocumentTypeInternalType):
    class Meta:
        name = "vetDocumentType"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalIdentity(GenericVersioningEntity):
    """
    Сведения об идентификации (маркировании) животного или группы животных.

    Attributes:
        identity_type: Тип идентификации: индивидуальная/групповая
        identity_status: Статус идентификации животного (группы
            животных)
        attached_label: Сведения о маркировке животного
        specified_animal: Сведения о животном (в случае индивидуальной
            идентификации)
        specified_animal_group: Сведения о группе животных (в случае
            групповой идентификации)
        applicable_classification: Дополнительные характеристики
        specified_animal_registration_ref: Сведения о зарегистрированном
            животном
        associated_marking_event: Сведения о маркировании животного:
            маркирование, замена средства маркирования, выбытие средства
            маркирования и т.д.
        referenced_animal_identity: Связанные сведения об идентификации
            животного
        referenced_document: Связанные документы
        qualifier:
    """

    model_config = ConfigDict(defer_build=True)
    identity_type: Optional[AnimalIdentityType] = field(
        default=None,
        metadata={
            "name": "identityType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    identity_status: Optional[AnimalIdentityStatus] = field(
        default=None,
        metadata={
            "name": "identityStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    attached_label: Optional[AnimalLabel] = field(
        default=None,
        metadata={
            "name": "attachedLabel",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    specified_animal: Optional[Animal] = field(
        default=None,
        metadata={
            "name": "specifiedAnimal",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    specified_animal_group: Optional[AnimalGroup] = field(
        default=None,
        metadata={
            "name": "specifiedAnimalGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    applicable_classification: list[ClassificationAttribute] = field(
        default_factory=list,
        metadata={
            "name": "applicableClassification",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    specified_animal_registration_ref: Optional[AnimalRegistration] = field(
        default=None,
        metadata={
            "name": "specifiedAnimalRegistrationRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    associated_marking_event: list[AnimalMarkingEvent] = field(
        default_factory=list,
        metadata={
            "name": "associatedMarkingEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    referenced_animal_identity: list[ReferencedAnimalIdentity] = field(
        default_factory=list,
        metadata={
            "name": "referencedAnimalIdentity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
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
    qualifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 100,
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


class ControlSampleDetails(BaseModel):
    """
    Сведения о контрольных образцах.

    Attributes:
        control_sample_presence: Наличие контрольного образца.
        control_sample_count: Количество контрольных образцов.
        control_sample_returning: Возврат контрольных образцов.
        control_sample_list: Список контрольных образцов.
    """

    model_config = ConfigDict(defer_build=True)
    control_sample_presence: Optional[ControlSampleIndicator] = field(
        default=None,
        metadata={
            "name": "controlSamplePresence",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    control_sample_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "controlSampleCount",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    control_sample_returning: Optional[SampleReturnType] = field(
        default=None,
        metadata={
            "name": "controlSampleReturning",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    control_sample_list: Optional[ControlSampleList] = field(
        default=None,
        metadata={
            "name": "controlSampleList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class FmpregistryEntryInternalType(GenericVersioningEntity):
    """
    Тип, описывающий запись реестра ЛП, ФС, КД или КГМО.

    Attributes:
        registry_status: Статус реестровой записи.
        fmp_product: Сведения о продукции.
        registration_certificate: Сведения о регистрационном
            удостоверении.
    """

    class Meta:
        name = "FMPRegistryEntry"

    model_config = ConfigDict(defer_build=True)
    registry_status: Optional[FmpregistryStatus] = field(
        default=None,
        metadata={
            "name": "registryStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    fmp_product: Optional[FmpregistryProduct] = field(
        default=None,
        metadata={
            "name": "fmpProduct",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    registration_certificate: Optional[RegistrationCertificate] = field(
        default=None,
        metadata={
            "name": "registrationCertificate",
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


class VetPermitCargoItemDetails(BaseModel):
    """
    Дополнительная информация о грузе.

    Attributes:
        product_name: Наименование продукции.
        tnved_code: Код ТН ВЭД.
        product_purpose: Назначение продукции.
        form_of_issue: Форма выпуска.
        component_composition: Компонентный состав.
        gmo_present: Наличие ГМО.
        gmo_name: Наименование ГМО.
        plant_component_present: Наличие компонентов растительного
            происхождения.
        animal_component_present: Наличие компонентов животного
            происхождения.
        additional_info: Дополнительная информация.
        fish_catch_district: Район вылова водных биоресурсов.
        packing: Упаковка, фасовка.
        registration_required: Требуется наличие обязательной
            регистрации.
        registration_certificate: Свидетельство о регистрации.
        covered_by_cites: Груз попадает под действие СИТЕС.
        cites_document: Документ СИТЕС.
        feed_in_original_packaging: Корма и кормовые добавки в заводской
            упаковке
        feed_for_cats_or_dogs: Корма и кормовые добавки предназначены
            для кошек или собак
    """

    model_config = ConfigDict(defer_build=True)
    product_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "productName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    tnved_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "tnvedCode",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 100,
        },
    )
    product_purpose: Optional[str] = field(
        default=None,
        metadata={
            "name": "productPurpose",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    form_of_issue: Optional[str] = field(
        default=None,
        metadata={
            "name": "formOfIssue",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    component_composition: Optional[str] = field(
        default=None,
        metadata={
            "name": "componentComposition",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    gmo_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "gmoPresent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    gmo_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "gmoName",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    plant_component_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "plantComponentPresent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    animal_component_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "animalComponentPresent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    additional_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    fish_catch_district: Optional[str] = field(
        default=None,
        metadata={
            "name": "fishCatchDistrict",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    packing: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    registration_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "registrationRequired",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    registration_certificate: Optional[RegistrationCertificate] = field(
        default=None,
        metadata={
            "name": "registrationCertificate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    covered_by_cites: Optional[bool] = field(
        default=None,
        metadata={
            "name": "coveredByCites",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    cites_document: Optional[Document] = field(
        default=None,
        metadata={
            "name": "citesDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    feed_in_original_packaging: Optional[bool] = field(
        default=None,
        metadata={
            "name": "feedInOriginalPackaging",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    feed_for_cats_or_dogs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "feedForCatsOrDogs",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class ReferencedDocument(ReferencedDocumentInternalType):
    class Meta:
        name = "referencedDocument"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalIdentityList(EntityList):
    """
    Тип, описывающий список сведений об идентификации животного.
    """

    model_config = ConfigDict(defer_build=True)
    animal_identity: list[AnimalIdentity] = field(
        default_factory=list,
        metadata={
            "name": "animalIdentity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalIdentityStatusChange(BaseModel):
    """
    Сведения об изменении статуса сведений об идентификации.

    Attributes:
        status: Установленный статус документа.
        specified_person: Пользователь, изменивший статус
        actual_date_time: Дата и время изменения статуса
        reason: Основание изменения статуса
    """

    model_config = ConfigDict(defer_build=True)
    status: AnimalIdentityStatus = field(
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
    reason: Optional[AnimalIdentityStatusChangeReason] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalRegistrationStatusChange(BaseModel):
    """
    Сведения об изменении статуса карточки животного.

    Attributes:
        status: Установленный статус документа.
        specified_person: Пользователь, изменивший статус
        actual_date_time: Дата и время изменения статуса
        reason: Основание изменения статуса
    """

    model_config = ConfigDict(defer_build=True)
    status: Optional[AnimalRegistrationStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    specified_person: Optional[UserInternalType] = field(
        default=None,
        metadata={
            "name": "specifiedPerson",
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
    reason: Optional[AnimalRegistrationStatusChangeReason] = field(
        default=None,
        metadata={
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


class FmpregistryEntryListInternalType(EntityList):
    """
    Тип, описывающий список записей гос.реестров ЛП, ФС, КД и КГМО (Гален)
    """

    class Meta:
        name = "FMPRegistryEntryList"

    model_config = ConfigDict(defer_build=True)
    fmp_registry_entry: list[FmpregistryEntryInternalType] = field(
        default_factory=list,
        metadata={
            "name": "fmpRegistryEntry",
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


class ReferencedAnimalIdentity(AnimalIdentity):
    """
    Связанные сведения об идентификации (маркировании) животного или группы
    животных.

    Attributes:
        relationship_type: Тип связи
    """

    model_config = ConfigDict(defer_build=True)
    relationship_type: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "relationshipType",
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


class VetPermitCargoItem(GenericEntity):
    """
    Позиция груза в ветеринарном разрешении.

    Attributes:
        code_within_permit: Шифр груза в разрешении.
        product: Продукция.
        sub_product: Вид продукции.
        cargo_amount: Объём груза.
        cargo_available_amount: Доступный объём груза по разрешению.
        cargo_unit: Единица измерения объёма груза.
        origin_country: Страна происхождения.
        origin_region: Регион страны происхождения.
        origin_district: Район страны происхождения.
        origin_locality: Населенный пункт происхождения.
        producer_list: Список аттестованных предприятий (для разрешений
            на экспорт).
        enterprise_list: Список предприятий.
        producer: Предприятие-производитель текстом.
        cargo_details: Дополнительная информация о грузе.
    """

    model_config = ConfigDict(defer_build=True)
    code_within_permit: str = field(
        metadata={
            "name": "codeWithinPermit",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
            "pattern": r"[А-Я]{1}[0-9]{2}",
        }
    )
    product: ProductInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    sub_product: SubProductInternalType = field(
        metadata={
            "name": "subProduct",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    cargo_amount: Decimal = field(
        metadata={
            "name": "cargoAmount",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
            "fraction_digits": 6,
        }
    )
    cargo_available_amount: Decimal = field(
        metadata={
            "name": "cargoAvailableAmount",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
            "fraction_digits": 6,
        }
    )
    cargo_unit: UnitInternalType = field(
        metadata={
            "name": "cargoUnit",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    origin_country: CountryInternalType = field(
        metadata={
            "name": "originCountry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    origin_region: Optional[RegionInternalType] = field(
        default=None,
        metadata={
            "name": "originRegion",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    origin_district: Optional[DistrictInternalType] = field(
        default=None,
        metadata={
            "name": "originDistrict",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    origin_locality: Optional[Locality] = field(
        default=None,
        metadata={
            "name": "originLocality",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    producer_list: Optional[CertifiedProducerListInternalType] = field(
        default=None,
        metadata={
            "name": "producerList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    enterprise_list: Optional[EnterpriseListInternalType] = field(
        default=None,
        metadata={
            "name": "enterpriseList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    producer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    cargo_details: Optional[VetPermitCargoItemDetails] = field(
        default=None,
        metadata={
            "name": "cargoDetails",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class VeterinaryEvent(GenericVersioningEntity):
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
        event_status: Статус записи о мероприятии.
        actual_date_time: Дата и время события
        actual_date: Дата мероприятия
        location: Место проведения мероприятия
        enterprise: Место проведения мероприятия в случае, если это
            зарегистрированное предприятие
        operator: Организация-оператор, осуществляющий мероприятие.
            Например, лаборатория (в случае лаб.исследований) или СББЖ.
        operator_business_entity: Организация-оператор, осуществляющий
            мероприятие. Например, лаборатория (в случае
            лаб.исследований) или СББЖ.
        operator_supervised_object: Поднадзорный объект
        authorized_person: Уполномоченное лицо
        classification:
        attribute:
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
    event_status: Optional[VeterinaryEventStatus] = field(
        default=None,
        metadata={
            "name": "eventStatus",
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
    actual_date: Optional[ComplexDatePeriod] = field(
        default=None,
        metadata={
            "name": "actualDate",
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
    operator_business_entity: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "name": "operatorBusinessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    operator_supervised_object: Optional[SupervisedObjectInternalType] = field(
        default=None,
        metadata={
            "name": "operatorSupervisedObject",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    authorized_person: Optional[UserInternalType] = field(
        default=None,
        metadata={
            "name": "authorizedPerson",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    classification: list[ClassificationAttribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    attribute: list[MeasuredAttribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
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
    notes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class VeterinaryEventStatusChange(BaseModel):
    """
    Сведения об изменении статуса сведений об идентификации.

    Attributes:
        status: Установленный статус документа.
        specified_person: Пользователь, изменивший статус
        actual_date_time: Дата и время изменения статуса
        reason: Основание изменения статуса
    """

    model_config = ConfigDict(defer_build=True)
    status: VeterinaryEventStatus = field(
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
    reason: Optional[VeterinaryEventStatusChangeReason] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class WbrcomplianceStatement(Document):
    """
    Заключение о соответствии партии ВБР требованиям страны-импортера.

    Attributes:
        decision: Решение (соответствует / не соответствует).
        conclusion: Заключение о несоответствии партии ВБР требованиям
            страны-импортера.
        import_country: Страна-импортер; страна, в которую следует груз.
        consignor: Грузоотправитель (хозяйствующий субъект).
        consignee: Грузополучатель (хозяйствующий субъект).
        official_veterinarian: Инспектор, оформивший заключение.
    """

    class Meta:
        name = "WBRComplianceStatement"

    model_config = ConfigDict(defer_build=True)
    decision: WbrcomplianceDecision = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    conclusion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    import_country: CountryInternalType = field(
        metadata={
            "name": "importCountry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    consignor: BusinessEntityInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    consignee: BusinessEntityInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    official_veterinarian: Optional[UserInternalType] = field(
        default=None,
        metadata={
            "name": "officialVeterinarian",
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


class AuthorizedPerson(UserInternalType):
    class Meta:
        name = "authorizedPerson"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class FmpRegistryEntry(FmpregistryEntryInternalType):
    class Meta:
        name = "fmpRegistryEntry"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


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


class AnimalKeepingEvent(VeterinaryEvent):
    """
    Сведения о содержании животного (группы животных)

    Attributes:
        keeping_type: Тип содержания животного (группы животных)
        keeping_purpose: Цель содержания животного (группы животных)
        keeping_location: Место содержания
        facility_description: Описание объекта (отделение, строение,
            корпус), в котором содержатся животные
    """

    model_config = ConfigDict(defer_build=True)
    keeping_type: Optional[AnimalKeepingTypeInternalType] = field(
        default=None,
        metadata={
            "name": "keepingType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    keeping_purpose: list[AnimalKeepingPurposeInternalType] = field(
        default_factory=list,
        metadata={
            "name": "keepingPurpose",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    keeping_location: Optional[AnimalKeepingLocation] = field(
        default=None,
        metadata={
            "name": "keepingLocation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    facility_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "facilityDescription",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )


class AnimalMarkingEvent(VeterinaryEvent):
    """
    Сведения о маркировании, перемаркировании или выбытии средства маркирования
    животного (группы животных)

    Attributes:
        occurrence_reason: Основание для проведения мероприятия
        associated_animal_identity: Сведения об идентификации животного
            (группы животных)
    """

    model_config = ConfigDict(defer_build=True)
    occurrence_reason: Optional[AnimalMarkingEventReason] = field(
        default=None,
        metadata={
            "name": "occurrenceReason",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    associated_animal_identity: list[AnimalIdentity] = field(
        default_factory=list,
        metadata={
            "name": "associatedAnimalIdentity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalMedicationEvent(VeterinaryEvent):
    """
    Сведения об обработке/иммунизации живого животного.

    Attributes:
        occurrence_reason: Основание мероприятия
        disease: Заболевание
        medicinal_drug: Препарат
        vaccine: Вакцина
        effective_before_date: Срок действия препарата/вакцины.
            Указывается дата и время окончания срока действия.
        active_substance: Действующее вещество препарата
        associated_animal_group: Сведения о зарегистрированных животных
            (группах животных)
    """

    model_config = ConfigDict(defer_build=True)
    occurrence_reason: Optional[AnimalLifecycleEventReason] = field(
        default=None,
        metadata={
            "name": "occurrenceReason",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    disease: list[AnimalDisease] = field(
        default_factory=list,
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
    vaccine: Optional[Vaccine] = field(
        default=None,
        metadata={
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
    active_substance: list[DrugActiveSubstance] = field(
        default_factory=list,
        metadata={
            "name": "activeSubstance",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    associated_animal_group: list[ObservableAnimalGroup] = field(
        default_factory=list,
        metadata={
            "name": "associatedAnimalGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


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


class VetPermitCargoItemList(BaseModel):
    """
    Список грузов.
    """

    model_config = ConfigDict(defer_build=True)
    cargo: list[VetPermitCargoItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class FmpRegistryEntryList(FmpregistryEntryListInternalType):
    class Meta:
        name = "fmpRegistryEntryList"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class UserList(UserListInternalType):
    class Meta:
        name = "userList"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalKeepingDetails(AnimalKeepingEvent):
    """
    Сведения о содержании животного (группы животных)
    """

    model_config = ConfigDict(defer_build=True)


class AnimalKeepingEventList(EntityList):
    """
    Список событий.

    Attributes:
        keeping_event: Событие
    """

    model_config = ConfigDict(defer_build=True)
    keeping_event: list[AnimalKeepingEvent] = field(
        default_factory=list,
        metadata={
            "name": "keepingEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalMedicationEventList(EntityList):
    """
    Список событий.

    Attributes:
        animal_medication_event: Событие
    """

    model_config = ConfigDict(defer_build=True)
    animal_medication_event: list[AnimalMedicationEvent] = field(
        default_factory=list,
        metadata={
            "name": "animalMedicationEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class LaboratoryResearchEventList(EntityList):
    """
    Список лабораторных исследований.
    """

    model_config = ConfigDict(defer_build=True)
    laboratory_research: list[LaboratoryResearchEvent] = field(
        default_factory=list,
        metadata={
            "name": "laboratoryResearch",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class LaboratoryResearchSample(BaseModel):
    """
    Сведения о пробе, отобранной для проведения лабораторных испытаний.

    Attributes:
        material: Материал.
        specified_material_name: Наименование материала.
        laboratory_research: Сведения о проведенном исследовании.
        conclusion: Заключение о лабораторных испытаниях (пробы).
    """

    model_config = ConfigDict(defer_build=True)
    material: Optional[LabSampleMaterial] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    specified_material_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "specifiedMaterialName",
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
    conclusion: Optional[str] = field(
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
        purpose: Цель направления груза.
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


class VeterinaryEventList(BaseModel):
    """
    Список ветеринарных мероприятий.

    Attributes:
        laboratory_research: Сведения о проведенных лабораторных
            исследованиях.
        quarantine: Сведения о карантинировании.
        immunization: Сведения о проведенной обработке/иммунизации
            животных.
        veterinary_event: Сведения о проведенных мероприятиях.
    """

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


class VeterinaryPermitInternalType(Document):
    """
    Разрешение РСХН на транспортировку через границу РФ подконтрольной продукции.

    Attributes:
        permit_year: Год, на который выдано разрешение.
        permit_decision: Решение (разрешение или запрет).
        central_department: ГУВ страны ТС, оформившее разрешение.
        vet_department: Ветеринарное управление субъекта страны ТС, в
            который следует груз.
        signed_by: Должностное лицо, ответственное за выдачу разрешения.
        general: Является ли разрешение генеральным (общим для всех).
        transfer_type: Тип операции (ввоз, вывоз, транзит).
        product_type: Тип продукции.
        transfer_purpose: Цель ввоза/вывоза.
        business_entity: Заявитель (хозяйствующий субъект).
        origin_country: Страна происхождения груза.
        import_country: Страна-импортер; страна, в которую следует груз.
        export_country: Страна-экспортер; страна, из которой следует
            груз.
        supplier: Предприятие-поставщик (при ввозе животных).
        consignee: Зарубежное предприятие-получатель (при экспорте)
        transfer_for: Груз следует ДЛЯ кого-то.
        transfer_via: Груз следует ЧЕРЕЗ кого-то.
        customs_clearance_region: Регион полного таможенного оформления.
        storage_point: Место хранения груза.
        shipment_point: Место отгрузки.
        bip_list_restricted: TRUE -- список допустимых пункты пропуска
            ограничен. Перечень приводится в элементе
            borderInspectionPointList. FALSE -- список допустимых
            пунктов пропуска не ограничен. Допускается транспорт груза
            через любой пункт пропуска ТС.
        border_inspection_point_list: Список допустимых пунктов
            пропуска.
        transport_type_list: Список допустимых типов транспорта.
        cargo_list: Список грузов в разрешении.
        condition_list: Список условий транспортировки груза.
        additional_condition_list: Список условий транспортировки груза.
        additional_info: Дополнительная информация.
        conclusion: Заключение о запрете в выдаче разрешения.
    """

    class Meta:
        name = "VeterinaryPermit"

    model_config = ConfigDict(defer_build=True)
    permit_year: Optional[str] = field(
        default=None,
        metadata={
            "name": "permitYear",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "pattern": r"[1-2][0-9][0-9][0-9]",
        },
    )
    permit_decision: Optional[PermitDecision] = field(
        default=None,
        metadata={
            "name": "permitDecision",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    central_department: Optional[Organization] = field(
        default=None,
        metadata={
            "name": "centralDepartment",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    vet_department: Optional[Organization] = field(
        default=None,
        metadata={
            "name": "vetDepartment",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    signed_by: Optional[UserInternalType] = field(
        default=None,
        metadata={
            "name": "signedBy",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    general: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transfer_type: Optional[TransferType] = field(
        default=None,
        metadata={
            "name": "transferType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    product_type: Optional[ProductTypeInternalType] = field(
        default=None,
        metadata={
            "name": "productType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transfer_purpose: Optional[PurposeInternalType] = field(
        default=None,
        metadata={
            "name": "transferPurpose",
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
    origin_country: Optional[CountryInternalType] = field(
        default=None,
        metadata={
            "name": "originCountry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    import_country: Optional[CountryInternalType] = field(
        default=None,
        metadata={
            "name": "importCountry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    export_country: Optional[CountryInternalType] = field(
        default=None,
        metadata={
            "name": "exportCountry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    supplier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    consignee: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transfer_for: Optional[str] = field(
        default=None,
        metadata={
            "name": "transferFor",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    transfer_via: Optional[str] = field(
        default=None,
        metadata={
            "name": "transferVia",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    customs_clearance_region: Optional[RegionInternalType] = field(
        default=None,
        metadata={
            "name": "customsClearanceRegion",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    storage_point: list[StoragePointInternalType] = field(
        default_factory=list,
        metadata={
            "name": "storagePoint",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    shipment_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "shipmentPoint",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    bip_list_restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "bipListRestricted",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    border_inspection_point_list: Optional[
        BorderVetControlPostListInternalType
    ] = field(
        default=None,
        metadata={
            "name": "borderInspectionPointList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    transport_type_list: Optional[TransportTypeList] = field(
        default=None,
        metadata={
            "name": "transportTypeList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    cargo_list: Optional[VetPermitCargoItemList] = field(
        default=None,
        metadata={
            "name": "cargoList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    condition_list: Optional[TransferConditionList] = field(
        default=None,
        metadata={
            "name": "conditionList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    additional_condition_list: Optional[TransferConditionList] = field(
        default=None,
        metadata={
            "name": "additionalConditionList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    additional_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "additionalInfo",
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


class AnimalRegistration(GenericVersioningEntity):
    """
    Сведения регистрации (учётная карточка) животного или группы животных.

    Attributes:
        identity_type: Тип идентификации/учёта: индивидуальная/групповая
        registration_number: Уникальный учётный номер животного
        registration_status: Статус учётной карточки животного (группы
            животных)
        initial_identification_type: Причина первичной идентификации:
            рождение, импорт, другое
        specified_animal: Сведения о животном (в случае индивидуальной
            идентификации)
        specified_animal_group: Сведения о группе животных (в случае
            групповой идентификации)
        specified_animal_identity: Сведения об идентификации животного
        specified_genetic_passport: Сведения о генетической
            идентификации
        import_details: Данные о ввозе на территорию РФ
        owner_party: Текущий владелец животного
        keeping_details: Сведения о содержании животного (группы
            животных)
        breeding_value_type: Племенная ценность
        specified_productivity: Сведения о продуктивности животного
            (группы животных)
        additional_attribute: Дополнительные атрибуты учётной карточки
        pedigree_info: Сведения о родословной животного
        brood_info: Сведения о потомстве животного (группы животных)
        unit_info: Сведения о животных, входящих в состав группы
        membership_info: Сведения о членстве в зарегистрированных
            группах животных
        referenced_document: Связанный документ
        notes: Дополнительная информация
        lifecycle_event_list: Сведения о событиях рождения, выбытия
            животного и т.п.
        medication_event_list: Сведения о ветеринарных мероприятиях в
            отношении животного
        keeping_event_list: Сведения о содержании животного
        movement_event_list: Сведения о перемещении животного и/или
            смене собственника
        qualifier:
    """

    model_config = ConfigDict(defer_build=True)
    identity_type: Optional[AnimalIdentityType] = field(
        default=None,
        metadata={
            "name": "identityType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    registration_number: Optional[AnimalId] = field(
        default=None,
        metadata={
            "name": "registrationNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    registration_status: Optional[AnimalRegistrationStatus] = field(
        default=None,
        metadata={
            "name": "registrationStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    initial_identification_type: Optional[AnimalIdentificationEventType] = (
        field(
            default=None,
            metadata={
                "name": "initialIdentificationType",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            },
        )
    )
    specified_animal: Optional[Animal] = field(
        default=None,
        metadata={
            "name": "specifiedAnimal",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    specified_animal_group: Optional[AnimalGroup] = field(
        default=None,
        metadata={
            "name": "specifiedAnimalGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    specified_animal_identity: list[AnimalIdentity] = field(
        default_factory=list,
        metadata={
            "name": "specifiedAnimalIdentity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    specified_genetic_passport: Optional[AnimalGeneticPassport] = field(
        default=None,
        metadata={
            "name": "specifiedGeneticPassport",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    import_details: Optional[AnimalImportDetails] = field(
        default=None,
        metadata={
            "name": "importDetails",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    owner_party: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "name": "ownerParty",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    keeping_details: Optional[AnimalKeepingDetails] = field(
        default=None,
        metadata={
            "name": "keepingDetails",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    breeding_value_type: Optional[AnimalBreedingValueType] = field(
        default=None,
        metadata={
            "name": "breedingValueType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    specified_productivity: list[AnimalProductivity] = field(
        default_factory=list,
        metadata={
            "name": "specifiedProductivity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    additional_attribute: list[UnmeasuredAttribute] = field(
        default_factory=list,
        metadata={
            "name": "additionalAttribute",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    pedigree_info: Optional[AnimalPedigreeInfo] = field(
        default=None,
        metadata={
            "name": "pedigreeInfo",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    brood_info: Optional[AnimalBroodInfo] = field(
        default=None,
        metadata={
            "name": "broodInfo",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    unit_info: Optional[AnimalUnitInfo] = field(
        default=None,
        metadata={
            "name": "unitInfo",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    membership_info: Optional[AnimalGroupMembershipInfo] = field(
        default=None,
        metadata={
            "name": "membershipInfo",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
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
    notes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    lifecycle_event_list: Optional[AnimalLifecycleEventList] = field(
        default=None,
        metadata={
            "name": "lifecycleEventList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    medication_event_list: Optional[AnimalMedicationEventList] = field(
        default=None,
        metadata={
            "name": "medicationEventList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    keeping_event_list: Optional[AnimalKeepingEventList] = field(
        default=None,
        metadata={
            "name": "keepingEventList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    movement_event_list: Optional[AnimalMovementEventList] = field(
        default=None,
        metadata={
            "name": "movementEventList",
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


class Sample(BaseModel):
    """
    Проба.

    Attributes:
        sampling_date_time: Дата и время отбора пробы.
        sample_cipher: Шифр пробы.
        sample_affixed_seal: Номер пломбы / сейф-пакета.
        sampling_regulatory_documents: Нормативные документы, согласно
            которым отобрана проба (ГОСТ, ТУ и т.п.).
        sampling_reason_list: Основание для проведения лабораторных
            исследований.
        certified_batch_producer: Аттестованный производитель
            (поднадзорный объект) партии продукции, от которой отобрана
            проба
        certified_batch: Сведения о партии продукции, от которой
            отобрана проба.
        sample_volume: Объем пробы.
        packing_type: Вид упаковки.
        sample_condition: Состояние пробы.
        sample_storage_conditions: Условия хранения пробы.
        sample_transportation_conditions: Условия перевозки пробы.
        control_sample_details: Сведения о контрольных образцах.
        laboratory_research_list: Сведения об исследованиях пробы.
    """

    model_config = ConfigDict(defer_build=True)
    sampling_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "samplingDateTime",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    sample_cipher: Optional[str] = field(
        default=None,
        metadata={
            "name": "sampleCipher",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )
    sample_affixed_seal: Optional[str] = field(
        default=None,
        metadata={
            "name": "sampleAffixedSeal",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    sampling_regulatory_documents: Optional[str] = field(
        default=None,
        metadata={
            "name": "samplingRegulatoryDocuments",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    sampling_reason_list: Optional[SamplingReasonList] = field(
        default=None,
        metadata={
            "name": "samplingReasonList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    certified_batch_producer: Optional[CertifiedProducerInternalType] = field(
        default=None,
        metadata={
            "name": "certifiedBatchProducer",
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
    sample_volume: Optional[Measure] = field(
        default=None,
        metadata={
            "name": "sampleVolume",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    packing_type: Optional[PackingType] = field(
        default=None,
        metadata={
            "name": "packingType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    sample_condition: Optional[str] = field(
        default=None,
        metadata={
            "name": "sampleCondition",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    sample_storage_conditions: Optional[str] = field(
        default=None,
        metadata={
            "name": "sampleStorageConditions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    sample_transportation_conditions: Optional[str] = field(
        default=None,
        metadata={
            "name": "sampleTransportationConditions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "max_length": 255,
        },
    )
    control_sample_details: Optional[ControlSampleDetails] = field(
        default=None,
        metadata={
            "name": "controlSampleDetails",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    laboratory_research_list: Optional[LaboratoryResearchEventList] = field(
        default=None,
        metadata={
            "name": "laboratoryResearchList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class StockEntryEventListInternalType(VeterinaryEventList):
    """
    Список мероприятий с партией продукции.
    """

    class Meta:
        name = "StockEntryEventList"

    model_config = ConfigDict(defer_build=True)


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


class VeterinaryPermitListInternalType(EntityList):
    """
    Тип, описывающий список ветеринарных разрешений.
    """

    class Meta:
        name = "VeterinaryPermitList"

    model_config = ConfigDict(defer_build=True)
    vet_permit: list[VeterinaryPermitInternalType] = field(
        default_factory=list,
        metadata={
            "name": "vetPermit",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class VeterinaryPermit(VeterinaryPermitInternalType):
    class Meta:
        name = "veterinaryPermit"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalGroupMembershipInfo(BaseModel):
    """
    Сведения о вхождении в зарегистрированные группы животных.

    Attributes:
        parent_group: Идентификатор карточки группового учёта животного
    """

    model_config = ConfigDict(defer_build=True)
    parent_group: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "parentGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalPedigreeInfo(BaseModel):
    """
    Сведения о родословной/родителях зарегистрированного животного.

    Attributes:
        parent: Идентификатор карточки учёта животного, являющегося
            родителем зарегистрированного животного
    """

    model_config = ConfigDict(defer_build=True)
    parent: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalRegistrationList(EntityList):
    """
    Тип, описывающий список регистрационных сведений о животном или группе
    животных.
    """

    model_config = ConfigDict(defer_build=True)
    animal_registration: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalUnitInfo(BaseModel):
    """
    Сведения о составе зарегистрированной группы животных.

    Attributes:
        individual_member: Идентификатор карточки индивидуального учёта
            животного, входящего в зарегистрированную группу
    """

    model_config = ConfigDict(defer_build=True)
    individual_member: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "individualMember",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


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


class ObservableAnimalGroup(BaseModel):
    """
    Животное или группа животных, в отношении которых проводится ветеринарное
    мероприятие.

    Attributes:
        specified_animal: Сведения о животном (в случае индивидуальной
            идентификации)
        specified_animal_group: Сведения о группе животных (в случае
            групповой идентификации)
        animal_registration_ref: Сведения о зарегистрированных животных
            (группах животных)
    """

    model_config = ConfigDict(defer_build=True)
    specified_animal: Optional[Animal] = field(
        default=None,
        metadata={
            "name": "specifiedAnimal",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    specified_animal_group: Optional[AnimalGroup] = field(
        default=None,
        metadata={
            "name": "specifiedAnimalGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    animal_registration_ref: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistrationRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class SamplingReportInternalType(Document):
    """
    Акт отбора проб.

    Attributes:
        sampling_report_status: Статус акта отбора проб.
        issuer_laboratory_research_party: Лаборатория, в которой будут
            проведены лаб. исследования.
        issuer_sampling_specialist: Специалист, отобравший пробу.
        contract_sender_party: Сторона-владелец продукции, с которой
            заключен данный акт.
        sampling_location: Место отбора проб.
        person_present_at_sampling: Лица, в присутствии которых
            производился отбор проб.
        laboratory_research_sample: Сведения о пробе, направляемой на
            лаб. исследования.
    """

    class Meta:
        name = "SamplingReport"

    model_config = ConfigDict(defer_build=True)
    sampling_report_status: Optional[SamplingReportStatus] = field(
        default=None,
        metadata={
            "name": "samplingReportStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    issuer_laboratory_research_party: Optional[VeterinaryLaboratory] = field(
        default=None,
        metadata={
            "name": "issuerLaboratoryResearchParty",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    issuer_sampling_specialist: Optional[UserInternalType] = field(
        default=None,
        metadata={
            "name": "issuerSamplingSpecialist",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    contract_sender_party: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "name": "contractSenderParty",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    sampling_location: Optional[EnterpriseInternalType] = field(
        default=None,
        metadata={
            "name": "samplingLocation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    person_present_at_sampling: list[UserInternalType] = field(
        default_factory=list,
        metadata={
            "name": "personPresentAtSampling",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    laboratory_research_sample: Optional[Sample] = field(
        default=None,
        metadata={
            "name": "laboratoryResearchSample",
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
        purpose: Цель направления партии продукции для входящей
            продукции, если задано
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
    purpose: Optional[PurposeInternalType] = field(
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


class StockEntryEventList(StockEntryEventListInternalType):
    class Meta:
        name = "stockEntryEventList"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class VetDocument(VetDocumentInternalType):
    class Meta:
        name = "vetDocument"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class VeterinaryPermitList(VeterinaryPermitListInternalType):
    class Meta:
        name = "veterinaryPermitList"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class AnimalLifecycleEvent(VeterinaryEvent):
    """
    Сведения о рождении, выбытии животного и т.п.

    Attributes:
        occurrence_reason: Основание мероприятия
        associated_animal_group: Сведения о зарегистрированных животных
            (группах животных)
    """

    model_config = ConfigDict(defer_build=True)
    occurrence_reason: Optional[AnimalLifecycleEventReason] = field(
        default=None,
        metadata={
            "name": "occurrenceReason",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    associated_animal_group: list[ObservableAnimalGroup] = field(
        default_factory=list,
        metadata={
            "name": "associatedAnimalGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalMovementEvent(VeterinaryEvent):
    """
    Сведения о перемещении животного.

    Attributes:
        consignor: Отправитель
        consignee: Получатель
        transport_info: Сведения о транспорте.
        shipment_route: Сведения о маршруте следования (пунктах
            перегрузки).
        purpose: Цель перемещения животного / группы животных
        associated_animal_group: Сведения о зарегистрированных животных
            (группах животных)
        associated_keeping_event: Сведения о содержании животного при
            перемещении
    """

    model_config = ConfigDict(defer_build=True)
    consignor: Optional[SupervisedObjectInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    consignee: Optional[SupervisedObjectInternalType] = field(
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
    shipment_route: Optional[ShipmentRouteInternalType] = field(
        default=None,
        metadata={
            "name": "shipmentRoute",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    purpose: Optional[AnimalKeepingPurposeInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    associated_animal_group: list[ObservableAnimalGroup] = field(
        default_factory=list,
        metadata={
            "name": "associatedAnimalGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    associated_keeping_event: list[AnimalKeepingEvent] = field(
        default_factory=list,
        metadata={
            "name": "associatedKeepingEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


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


class LaboratoryResearchReportInternalType(Document):
    """
    Сведения о протоколе испытаний (лабораторных исследований).

    Attributes:
        sample: Сведения о пробе.
        sampling_report: Сведения об акте отбора проб.
    """

    class Meta:
        name = "LaboratoryResearchReport"

    model_config = ConfigDict(defer_build=True)
    sample: list[LaboratoryResearchSample] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    sampling_report: Optional[SamplingReportInternalType] = field(
        default=None,
        metadata={
            "name": "samplingReport",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
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


class SamplingReport(SamplingReportInternalType):
    class Meta:
        name = "samplingReport"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


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


class AnimalBroodInfo(BaseModel):
    """
    Сведения о потомстве.

    Attributes:
        size: Численность потомства
        referenced_lifecycle_event: Связанные события, содержащие
            сведения о воспроизведении потомства
        descendant: Идентификатор карточки учёта животного, являющегося
            потомком зарегистрированного животного
    """

    model_config = ConfigDict(defer_build=True)
    size: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    referenced_lifecycle_event: list[AnimalLifecycleEvent] = field(
        default_factory=list,
        metadata={
            "name": "referencedLifecycleEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    descendant: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalImportDetails(BaseModel):
    """
    Сведения о ввозе животного (группы животных) в РФ.

    Attributes:
        import_date: Дата (в случае индивидуального учёта) или период
            дат (в случае группового учёта) ввоза животного (группы
            животных) на территорию РФ
        import_country: Страна, из которой было ввезено животное (группа
            животных)
        referenced_movement_event: Событие о перемещении животного
            (группы животных)
    """

    model_config = ConfigDict(defer_build=True)
    import_date: Optional[ComplexDatePeriod] = field(
        default=None,
        metadata={
            "name": "importDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    import_country: Optional[CountryInternalType] = field(
        default=None,
        metadata={
            "name": "importCountry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    referenced_movement_event: list[AnimalMovementEvent] = field(
        default_factory=list,
        metadata={
            "name": "referencedMovementEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalLifecycleEventList(EntityList):
    """
    Список событий.

    Attributes:
        animal_lifecycle_event: Событие
    """

    model_config = ConfigDict(defer_build=True)
    animal_lifecycle_event: list[AnimalLifecycleEvent] = field(
        default_factory=list,
        metadata={
            "name": "animalLifecycleEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class AnimalMovementEventList(EntityList):
    """
    Список событий.

    Attributes:
        movement_event: Событие
    """

    model_config = ConfigDict(defer_build=True)
    movement_event: list[AnimalMovementEvent] = field(
        default_factory=list,
        metadata={
            "name": "movementEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


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


class LaboratoryResearchReportListInternalType(EntityList):
    """
    Тип, описывающий список протоколов испытаний (лабораторных исследований).
    """

    class Meta:
        name = "LaboratoryResearchReportList"

    model_config = ConfigDict(defer_build=True)
    laboratory_research_report: list[LaboratoryResearchReportInternalType] = (
        field(
            default_factory=list,
            metadata={
                "name": "laboratoryResearchReport",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            },
        )
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
            выработанной партии - продукция. 5. Утилизация (10101) -
            если сырьё присутствует в операции, а выработанной партии
            нет.
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


class LaboratoryResearchReport(LaboratoryResearchReportInternalType):
    class Meta:
        name = "laboratoryResearchReport"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class StockEntryList(StockEntryListInternalType):
    class Meta:
        name = "stockEntryList"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)


class LaboratoryResearchReportList(LaboratoryResearchReportListInternalType):
    class Meta:
        name = "laboratoryResearchReportList"
        namespace = "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2"

    model_config = ConfigDict(defer_build=True)
