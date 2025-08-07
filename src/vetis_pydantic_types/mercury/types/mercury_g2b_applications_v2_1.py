from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict
from xsdata.models.datatype import XmlDateTime

from vetis_pydantic_types.base import ApplicationRequest, ApplicationResponse
from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.mercury.types.application_v2_0 import (
    ApplicationDataInternalType,
    ApplicationResultDataInternalType,
)
from vetis_pydantic_types.mercury.types.base_v2_0 import (
    Guid,
    ListOptions,
    UpdateDateInterval,
    Uuid,
)
from vetis_pydantic_types.mercury.types.dictionary_v2_1 import (
    BusinessEntityInternalType,
    CargoType,
    EnterpriseGuid,
    EnterpriseInternalType,
    ProductItemListInternalType,
)
from vetis_pydantic_types.mercury.types.document_v2_1 import (
    AuthorityList,
    BeactivityLocationsModificationOperation,
    BemodificationOperation,
    Consignor,
    Delivery,
    DeliveryFactList,
    DeliveryParticipant,
    DiscrepancyReport,
    EntmodificationOperation,
    IssueDateInterval,
    MergeStockEntriesOperation,
    ProductionOperation,
    PslmodificationOperation,
    R13NRouteSection,
    ReferencedDocument,
    ShipmentRoute,
    StockDiscrepancy,
    StockEntry,
    StockEntryInternalType,
    StockEntryList,
    StockEntryListInternalType,
    StockEntrySearchPattern,
    User,
    UserInternalType,
    UserList,
    VetDocument,
    VetDocumentInternalType,
    VetDocumentList,
    VetDocumentStatus,
    VetDocumentType,
    VetDocumentUuid,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"


class AddBusinessEntityUserResponseInternalType(
    ApplicationResultDataInternalType
):
    """Ответ на регистрацию/привязку пользователя(ей) хозяйствующего субъекта.

    Ответ содержит список пользователей, для которых в результате
    запроса была выполнена регистрация/привязка.

    Attributes:
        user: Сведения о зарегистрированном/привязанном пользователе.
    """

    class Meta:
        name = "AddBusinessEntityUserResponse"

    model_config = ConfigDict(defer_build=True)
    user: list[User] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class CheckShipmentRegionalizationResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат проверки правил регионализации.

    Attributes:
        r13n_route_section: Описание правил перемещения продукции.
            Количество элементов `r13nRouteSection` в ответе
            соответствует количеству отрезков маршрута. Атрибут
            `r13nRouteSection/sqnId` равен номеру отрезка, нумерация
            начинается с единицы. Количество элементов
            `r13nRouteSection/appliedR13nRule` соответствует количеству
            категорий груза (элемент `cargoType`) в запросе.
    """

    class Meta:
        name = "CheckShipmentRegionalizationResponse"

    model_config = ConfigDict(defer_build=True)
    r13n_route_section: list[R13NRouteSection] = field(
        default_factory=list,
        metadata={
            "name": "r13nRouteSection",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class GetApplicableUserAuthorityListResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ на получение списка доступных ролей.

    Attributes:
        authority_list: Список доступных ролей пользователя ХС.
    """

    class Meta:
        name = "GetApplicableUserAuthorityListResponse"

    model_config = ConfigDict(defer_build=True)
    authority_list: Optional[AuthorityList] = field(
        default=None,
        metadata={
            "name": "authorityList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class GetBusinessEntityUserListResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ на получение списка пользователей ХС.

    Attributes:
        user_list: Список пользователей, прикрепленных к ХС.
    """

    class Meta:
        name = "GetBusinessEntityUserListResponse"

    model_config = ConfigDict(defer_build=True)
    user_list: Optional[UserList] = field(
        default=None,
        metadata={
            "name": "userList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class GetBusinessEntityUserResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ на получение полных сведений о пользователе.

    Attributes:
        user: Запрашиваемые сведения о пользователе.
    """

    class Meta:
        name = "GetBusinessEntityUserResponse"

    model_config = ConfigDict(defer_build=True)
    user: Optional[User] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class GetStockEntryByGuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на получение записи по идентификатору.

    Attributes:
        stock_entry: Запись журнала продукции.
    """

    class Meta:
        name = "GetStockEntryByGuidResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry: StockEntry = field(
        metadata={
            "name": "stockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class GetStockEntryByUuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на получение версии записи по идентификатору.

    Attributes:
        stock_entry: Запись журнала продукции.
    """

    class Meta:
        name = "GetStockEntryByUuidResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry: StockEntry = field(
        metadata={
            "name": "stockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class GetStockEntryChangesListResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на получение списка версий.

    Attributes:
        stock_entry_list: Список версий.
    """

    class Meta:
        name = "GetStockEntryChangesListResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry_list: StockEntryList = field(
        metadata={
            "name": "stockEntryList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class GetStockEntryListResponseInternalType(ApplicationResultDataInternalType):
    """
    Результат заявки на получение списка актуальных записей журнала.

    Attributes:
        stock_entry_list: Список записей.
    """

    class Meta:
        name = "GetStockEntryListResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry_list: StockEntryList = field(
        metadata={
            "name": "stockEntryList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class GetStockEntryVersionListResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на получение списка версий записи журнала.

    Attributes:
        stock_entry_list: Список версий записеи.
    """

    class Meta:
        name = "GetStockEntryVersionListResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry_list: StockEntryList = field(
        metadata={
            "name": "stockEntryList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class GetVetDocumentByUuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки на получение записи вет.

    сертификата по идентификатору.

    Attributes:
        vet_document: Ветеринарный сертификат.
    """

    class Meta:
        name = "GetVetDocumentByUuidResponse"

    model_config = ConfigDict(defer_build=True)
    vet_document: VetDocument = field(
        metadata={
            "name": "vetDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class GetVetDocumentChangesListResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на получение списка измененных ветсертификатов.

    Attributes:
        vet_document_list: Список записей.
    """

    class Meta:
        name = "GetVetDocumentChangesListResponse"

    model_config = ConfigDict(defer_build=True)
    vet_document_list: VetDocumentList = field(
        metadata={
            "name": "vetDocumentList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class GetVetDocumentListResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на получение списка ветсертификатов.

    Attributes:
        vet_document_list: Список записей.
    """

    class Meta:
        name = "GetVetDocumentListResponse"

    model_config = ConfigDict(defer_build=True)
    vet_document_list: VetDocumentList = field(
        metadata={
            "name": "vetDocumentList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class MercuryApplicationRequest(ApplicationDataInternalType):
    model_config = ConfigDict(defer_build=True)
    local_transaction_id: str = field(
        metadata={
            "name": "localTransactionId",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
            "max_length": 100,
        }
    )
    initiator: UserInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "sessionToken",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class MergeStockEntriesResponseInternalType(ApplicationResultDataInternalType):
    """
    Результат заявки на объединение записей журнала продукции.

    Attributes:
        stock_entry_list: Сведения о созданных и/или измененных версиях
            записей журнала продукции.
    """

    class Meta:
        name = "MergeStockEntriesResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry_list: StockEntryListInternalType = field(
        metadata={
            "name": "stockEntryList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )


class ModifyActivityLocationsResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на изменение списка мест осуществления деятельности
    хозяйствующим субъектом.

    Attributes:
        business_entity: Запись хозяйствующего субъекта с указанием
            текущего списка площадок.
    """

    class Meta:
        name = "ModifyActivityLocationsResponse"

    model_config = ConfigDict(defer_build=True)
    business_entity: Optional[BusinessEntityInternalType] = field(
        default=None,
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class ModifyBusinessEntityResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на внесение изменений в реестр ХС.

    Attributes:
        business_entity: Измененные версии записей реестра ХС.
    """

    class Meta:
        name = "ModifyBusinessEntityResponse"

    model_config = ConfigDict(defer_build=True)
    business_entity: list[BusinessEntityInternalType] = field(
        default_factory=list,
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class ModifyEnterpriseResponseInternalType(ApplicationResultDataInternalType):
    """
    Результат заявки на внесение изменений в реестр предприятий.

    Attributes:
        enterprise: Измененные версии записей реестра предприятий.
    """

    class Meta:
        name = "ModifyEnterpriseResponse"

    model_config = ConfigDict(defer_build=True)
    enterprise: list[EnterpriseInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class ModifyProducerStockListResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на изменение реестра наименований продукции предприятия-
    производителя.

    Attributes:
        product_item_list: Сведения о созданных и/или измененных версиях
            наименований продукции.
    """

    class Meta:
        name = "ModifyProducerStockListResponse"

    model_config = ConfigDict(defer_build=True)
    product_item_list: ProductItemListInternalType = field(
        metadata={
            "name": "productItemList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )


class PrepareOutgoingConsignmentResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на оформление транспортной партии.

    Attributes:
        stock_entry: Сведения о измененных записи(ях) журнала продукции.
        vet_document: Сведения об оформленном или погашенном
            ветеринарном сертификате.
    """

    class Meta:
        name = "PrepareOutgoingConsignmentResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry: list[StockEntryInternalType] = field(
        default_factory=list,
        metadata={
            "name": "stockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )
    vet_document: list[VetDocumentInternalType] = field(
        default_factory=list,
        metadata={
            "name": "vetDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class ProcessIncomingConsignmentResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на оформление входящей партии.

    Attributes:
        stock_entry: Сведения о созданных записи(ях) журнала продукции.
        vet_document: Сведения о ветеринарных сертификатах: погашенном и
            возвратном.
    """

    class Meta:
        name = "ProcessIncomingConsignmentResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry: list[StockEntryInternalType] = field(
        default_factory=list,
        metadata={
            "name": "stockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )
    vet_document: list[VetDocumentInternalType] = field(
        default_factory=list,
        metadata={
            "name": "vetDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class ProcessIncomingDeliveryResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на оформление входящей партии.

    Attributes:
        stock_entry: Сведения о созданных записи(ях) журнала продукции.
            Передаётся сокращенный набор сведений о записи журнала: uuid
            guid active last status createDate updateDate entryNumber
            batch/productType batch/product batch/subProduct
            batch/productItem batch/volume batch/unit
            batch/dateOfProduction batch/expiryDate batch/batchID
            batch/perishable batch/lowGradeCargo @qualifier Атрибут
            @qualifier заполняется значением, указанным в атрибуте
            запроса accompanyingForms/vetCertificate/@qualifier для
            соответствующего входящего ВСД. По умолчанию, значение
            @qualifier совпадает с идентификатором сертификата
            accompanyingForms/vetCertificate/uuid
        vet_document: Сведения о ветеринарных сертификатах: погашенном и
            возвратном. Для возвратных ВСД передаётся полный набор
            сведений, для погашенных ВСД -- сокращенный: uuid vetDForm
            vetDType vetDStatus finalized lastUpdateDate statusChange
            @qualifier Для возвратных ВСД атрибут @qualifier заполняется
            значением, указанным в атрибуте запроса
            accompanyingForms/vetCertificate/@qualifier для
            соответствующего входящего ВСД. По умолчанию, значение
            @qualifier совпадает с идентификатором сертификата
            accompanyingForms/vetCertificate/uuid
    """

    class Meta:
        name = "ProcessIncomingDeliveryResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry: list[StockEntryInternalType] = field(
        default_factory=list,
        metadata={
            "name": "stockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )
    vet_document: list[VetDocumentInternalType] = field(
        default_factory=list,
        metadata={
            "name": "vetDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class RegisterProductionOperationResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на оформление производственной партии.

    Attributes:
        stock_entry_list: Сведения о созданных и/или измененных записях
            журнала продукции.
        vet_document: Сведения об оформленном или погашенном
            ветеринарном сертификате.
    """

    class Meta:
        name = "RegisterProductionOperationResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry_list: Optional[StockEntryListInternalType] = field(
        default=None,
        metadata={
            "name": "stockEntryList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )
    vet_document: list[VetDocumentInternalType] = field(
        default_factory=list,
        metadata={
            "name": "vetDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class ResolveDiscrepancyResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на регистрацию несоответствий в записях складского журнала,
    выявленных в результате инвентаризации.

    Attributes:
        stock_entry_list: Сведения о созданных и/или измененных версиях
            записей журнала продукции.
    """

    class Meta:
        name = "ResolveDiscrepancyResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry_list: StockEntryListInternalType = field(
        metadata={
            "name": "stockEntryList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )


class UnbindBusinessEntityUserResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ на удаление пользователя.

    Attributes:
        user: Пользователь, который был откреплен от ХС-заявителя.
    """

    class Meta:
        name = "UnbindBusinessEntityUserResponse"

    model_config = ConfigDict(defer_build=True)
    user: list[User] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class UpdateTransportMovementDetailsResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на получение списка версий записи журнала.

    Attributes:
        vet_document: Список транспортных ветеринарных сертификатов с
            измененными сведениями о транспортных средствах.
    """

    class Meta:
        name = "UpdateTransportMovementDetailsResponse"

    model_config = ConfigDict(defer_build=True)
    vet_document: list[VetDocument] = field(
        default_factory=list,
        metadata={
            "name": "vetDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class UpdateUserAuthoritiesResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ на изменение прав доступа пользователя.

    Attributes:
        user: Пользователь, для которого были изменены права доступа.
    """

    class Meta:
        name = "UpdateUserAuthoritiesResponse"

    model_config = ConfigDict(defer_build=True)
    user: list[User] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class UpdateUserWorkingAreasResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ на изменение зон ответственности пользователя.

    Attributes:
        user: Пользователь, для которого были изменены зоны
            ответственности
    """

    class Meta:
        name = "UpdateUserWorkingAreasResponse"

    model_config = ConfigDict(defer_build=True)
    user: list[User] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class UpdateVeterinaryEventsResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на получение списка версий записи журнала.

    Attributes:
        stock_entry: Список записей складского журнала продукции с
            измененными сведениями о ветеринарным мероприятиях.
    """

    class Meta:
        name = "UpdateVeterinaryEventsResponse"

    model_config = ConfigDict(defer_build=True)
    stock_entry: list[StockEntry] = field(
        default_factory=list,
        metadata={
            "name": "stockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class WithdrawVetDocumentResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Результат заявки на аннулирование ветеринарного сертификата.

    Attributes:
        vet_document: Сведения об аннулированном ветеринарном
            сертификате.
        stock_entry: Сведения об измененных версиях записей журнала
            продукции.
    """

    class Meta:
        name = "WithdrawVetDocumentResponse"

    model_config = ConfigDict(defer_build=True)
    vet_document: Optional[VetDocumentInternalType] = field(
        default=None,
        metadata={
            "name": "vetDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )
    stock_entry: list[StockEntryInternalType] = field(
        default_factory=list,
        metadata={
            "name": "stockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class AddBusinessEntityUserRequestInternalType(MercuryApplicationRequest):
    """Запрос на регистрацию/привязку пользователя(ей) хозяйствующего субъекта.

    Если пользователь с указанным uuid, login, passport или snils уже
    зарегистрирован и ФИО совпадает, он будет прикреплен к ХС-заявителю
    (если зарегистрированный пользователь не привязан к ХС-заявителю).
    Профиль пользователя при этом обновлен не будет. Если ФИО не
    совпадает или пользователь уже привязан к ХС-заявителю --
    пользователь зарегистрирован/привязан не будет. Иначе регистрируется
    новый пользователь при условии заполнения обязательных сведений. За
    один запрос можно зарегистрировать/привязать не более N
    пользователей. Для вновь регистрируемых пользователей и существующих
    пользователей, для которых выполняется привязка к ХС-заявителю,
    будут установлены права и зоны ответственности, указанные в запросе.

    Attributes:
        user: Сведения о регистрируемом пользователе.
    """

    class Meta:
        name = "AddBusinessEntityUserRequest"

    model_config = ConfigDict(defer_build=True)
    user: list[User] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "min_occurs": 1,
        },
    )


class CheckShipmentRegionalizationRequestInternalType(
    MercuryApplicationRequest
):
    """
    Заявка на проверку правил регионализации для определенной категории груза и
    маршрута следования.

    Attributes:
        cargo_type: Категория груза, для которой запрашиваются правила
            перемещения по маршруту.
        shipment_route: Маршрут следования груза. В отличие от маршрута
            следования, который указывается в транспортном сертификате и
            в запросе на оформление исходящей партии, `shipmentRoute`
            здесь должен включать точку отправления и точку назначения.
            Для каждой точки маршрута обязательно должен быть заполнен
            адрес: элементы `shipmentRoute/routePoint/location/address`
            и `shipmentRoute/routePoint/enterprise/address`. Только в
            этом случае проверка правил перемещения (регионализация)
            даст корректный результат.
    """

    class Meta:
        name = "CheckShipmentRegionalizationRequest"

    model_config = ConfigDict(defer_build=True)
    cargo_type: list[CargoType] = field(
        default_factory=list,
        metadata={
            "name": "cargoType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "min_occurs": 1,
        },
    )
    shipment_route: ShipmentRoute = field(
        metadata={
            "name": "shipmentRoute",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class GetApplicableUserAuthorityListRequestInternalType(
    MercuryApplicationRequest
):
    """Запрос на получение списка доступных ролей пользователя.

    В ответ на запрос будет сформирован список ролей в ИС Меркурий для
    пользователя хозяйствующего субъекта.

    Attributes:
        list_options: Параметры запрашиваемого списка.
    """

    class Meta:
        name = "GetApplicableUserAuthorityListRequest"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )


class GetBusinessEntityUserListRequestInternalType(MercuryApplicationRequest):
    """
    Запрос на получение списка пользователей ХС-заявителя.

    Attributes:
        list_options: Параметры запрашиваемого списка.
    """

    class Meta:
        name = "GetBusinessEntityUserListRequest"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )


class GetBusinessEntityUserRequestInternalType(MercuryApplicationRequest):
    """Запрос на получение полных сведений о пользователе ХС-заявителя.

    Пользователь должен быть привязан к ХС-заявителю, иначе -- ошибка.

    Attributes:
        user: Пользователь, для которого запрашиваются сведения. Должен
            быть указан uuid или login.
    """

    class Meta:
        name = "GetBusinessEntityUserRequest"

    model_config = ConfigDict(defer_build=True)
    user: User = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class GetStockEntryByGuidRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на получение записи журнала по глобальному идентификатору.

    Attributes:
        guid: Идентификатор записи, по которому производится поиск.
        enterprise_guid: Идентификатор предприятия, по которому
            производится поиск записи.
    """

    class Meta:
        name = "GetStockEntryByGuidRequest"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )
    enterprise_guid: EnterpriseGuid = field(
        metadata={
            "name": "enterpriseGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetStockEntryByUuidRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на получение версии записи по идентификатору.

    Attributes:
        uuid: Идентификатор версии, по которому производится поиск.
        enterprise_guid: Идентификатор предприятия, по которому
            производится поиск записи.
    """

    class Meta:
        name = "GetStockEntryByUuidRequest"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )
    enterprise_guid: EnterpriseGuid = field(
        metadata={
            "name": "enterpriseGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetStockEntryChangesListRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на получение списка версий записей журнала, созданных или измененных за
    указанный интервал дат.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
        enterprise_guid: Идентификатор предприятия, по которому
            производится поиск записей.
    """

    class Meta:
        name = "GetStockEntryChangesListRequest"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    update_date_interval: UpdateDateInterval = field(
        metadata={
            "name": "updateDateInterval",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )
    enterprise_guid: EnterpriseGuid = field(
        metadata={
            "name": "enterpriseGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetStockEntryListRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на получение списка актуальных записей журнала.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        enterprise_guid: Идентификатор предприятия, по которому
            производится поиск записей.
        search_pattern: Шаблон поиска записей складского журнала.
    """

    class Meta:
        name = "GetStockEntryListRequest"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    enterprise_guid: EnterpriseGuid = field(
        metadata={
            "name": "enterpriseGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    search_pattern: Optional[StockEntrySearchPattern] = field(
        default=None,
        metadata={
            "name": "searchPattern",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class GetStockEntryVersionListRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на получение всех версий по идентификатору записи журнала.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        guid: Идентификатор записи, по которому производится поиск.
        enterprise_guid: Идентификатор предприятия, по которому
            производится поиск записи.
    """

    class Meta:
        name = "GetStockEntryVersionListRequest"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )
    enterprise_guid: EnterpriseGuid = field(
        metadata={
            "name": "enterpriseGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetVetDocumentByUuidRequestInternalType(MercuryApplicationRequest):
    """Заявка на получение записи вет.

    сертификата по идентификатору.

    Attributes:
        uuid: Идентификатор версии, по которому производится поиск.
        enterprise_guid: Идентификатор предприятия, по которому
            производится поиск записи.
    """

    class Meta:
        name = "GetVetDocumentByUuidRequest"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )
    enterprise_guid: EnterpriseGuid = field(
        metadata={
            "name": "enterpriseGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetVetDocumentChangesListRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на получение списка версий, созданных или измененных за указанный
    интервал дат.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
        enterprise_guid: Идентификатор предприятия, по которому
            производится поиск записей.
        vet_document_type: Тип ветсертификата.
        vet_document_status: Статус ветсертификата.
    """

    class Meta:
        name = "GetVetDocumentChangesListRequest"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    update_date_interval: UpdateDateInterval = field(
        metadata={
            "name": "updateDateInterval",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )
    enterprise_guid: EnterpriseGuid = field(
        metadata={
            "name": "enterpriseGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    vet_document_type: Optional[VetDocumentType] = field(
        default=None,
        metadata={
            "name": "vetDocumentType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    vet_document_status: Optional[VetDocumentStatus] = field(
        default=None,
        metadata={
            "name": "vetDocumentStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )


class GetVetDocumentListRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на получение списка записей ветсертификатов.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        vet_document_type: Тип ветсертификата.
        vet_document_status: Статус ветсертификата.
        issue_date_interval: Период дат оформления документа.
            Соответствует полю issueDate документа в результирующем
            списке. Максимальная длина интервала -- 31 день.
        consignor: Отправитель для транспортного ВСД. Фильтрация
            осуществляется по глобальному идентификатору ХС
            (consignor/businessEntity/guid) и площадки
            (consignor/enterprise/guid). Если производится поиск по
            производственным документам (установлен фильтр
            vetDocumentType = PRODUCTIVE), поле consignor игнорируется.
        referenced_document: Связанный документ. Поддерживается поиск по
            связанным документам с отношением (relationshipType) равным
            1 и 6, поддерживаемые типы документов: 1-5 (транспортный
            документ). Для документа обязательными к заполнению являются
            поля тип (type), номер (issueNumber) и дата (issueDate). При
            поиске по связанному документу обязательно заполнение
            фильтра vetDocumentType.
        enterprise_guid: Идентификатор предприятия, по которому
            производится поиск записей. В результирующий список попадут
            (в общем случае, если не установлено других критериев
            отбора): 1) Транспортные ВСД, для которых ХС-отправитель
            соответствует заявителю (issuer), предприятие-отправитель --
            указанному идентификатору (enterpriseGuid). 2) Транспортные
            ВСД, для которых ХС-получатель соответствует заявителю
            (issuer), предприятие-получатель -- указанному
            идентификатору (enterpriseGuid). 3) Производственные ВСД,
            для которых ХС-производитель соответствует заявителю
            (issuer), предприятие-производитель -- указанному
            идентификатору (enterpriseGuid).
    """

    class Meta:
        name = "GetVetDocumentListRequest"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    vet_document_type: Optional[VetDocumentType] = field(
        default=None,
        metadata={
            "name": "vetDocumentType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    vet_document_status: Optional[VetDocumentStatus] = field(
        default=None,
        metadata={
            "name": "vetDocumentStatus",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    issue_date_interval: Optional[IssueDateInterval] = field(
        default=None,
        metadata={
            "name": "issueDateInterval",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    consignor: Optional[Consignor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    referenced_document: Optional[ReferencedDocument] = field(
        default=None,
        metadata={
            "name": "referencedDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
        },
    )
    enterprise_guid: EnterpriseGuid = field(
        metadata={
            "name": "enterpriseGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class MergeStockEntriesRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на объединение записей журнала продукции.

    Attributes:
        enterprise: Предприятие.
        merge_operation: Складская операция (объединение записей журнала
            продукции).
    """

    class Meta:
        name = "MergeStockEntriesRequest"

    model_config = ConfigDict(defer_build=True)
    enterprise: EnterpriseInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    merge_operation: MergeStockEntriesOperation = field(
        metadata={
            "name": "mergeOperation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )


class ModifyActivityLocationsRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на изменение списка мест осуществления деятельности хозяйствующего
    субъекта.

    Attributes:
        modification_operation: Операция внесения изменений списка
            площадок.
    """

    class Meta:
        name = "ModifyActivityLocationsRequest"

    model_config = ConfigDict(defer_build=True)
    modification_operation: BeactivityLocationsModificationOperation = field(
        metadata={
            "name": "modificationOperation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )


class ModifyBusinessEntityRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на внесение изменений в реестр ХС.

    Attributes:
        modification_operation: Операция внесения изменений в реестр ХС.
    """

    class Meta:
        name = "ModifyBusinessEntityRequest"

    model_config = ConfigDict(defer_build=True)
    modification_operation: BemodificationOperation = field(
        metadata={
            "name": "modificationOperation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )


class ModifyEnterpriseRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на внесение изменений в реестр предприятий.

    Attributes:
        modification_operation: Операция внесения изменений в реестр
            предприятий.
    """

    class Meta:
        name = "ModifyEnterpriseRequest"

    model_config = ConfigDict(defer_build=True)
    modification_operation: EntmodificationOperation = field(
        metadata={
            "name": "modificationOperation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )


class ModifyProducerStockListRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на изменение реестра наименований продукции предприятия-производителя.

    Attributes:
        modification_operation: Операция внесения изменений в реестр
            наименований продукции производителя.
    """

    class Meta:
        name = "ModifyProducerStockListRequest"

    model_config = ConfigDict(defer_build=True)
    modification_operation: PslmodificationOperation = field(
        metadata={
            "name": "modificationOperation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )


class PrepareOutgoingConsignmentRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на оформление транспортной партии.

    Attributes:
        delivery: Сведения об отгрузке.
    """

    class Meta:
        name = "PrepareOutgoingConsignmentRequest"

    model_config = ConfigDict(defer_build=True)
    delivery: list[Delivery] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "min_occurs": 1,
        },
    )


class ProcessIncomingConsignmentRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на оформление входящей партии.

    Attributes:
        delivery: Сведения о поставке.
        delivery_facts: Результаты приёмки.
        discrepancy_report: Акт о несоответствии.
        returned_delivery: Сведения о возврате продукции.
    """

    class Meta:
        name = "ProcessIncomingConsignmentRequest"

    model_config = ConfigDict(defer_build=True)
    delivery: Delivery = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    delivery_facts: DeliveryFactList = field(
        metadata={
            "name": "deliveryFacts",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    discrepancy_report: list[DiscrepancyReport] = field(
        default_factory=list,
        metadata={
            "name": "discrepancyReport",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )
    returned_delivery: Optional[Delivery] = field(
        default=None,
        metadata={
            "name": "returnedDelivery",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class ProcessIncomingDeliveryRequestInternalType(MercuryApplicationRequest):
    """Заявка на оформление входящей поставки.

    Предназначена для пакетного гашения электронных ВСД в случае полной
    приёмки или полного возврата, не предусматривающих создание акта
    расхождений. Максимальное допустимое количество входящих ВСД
    (партий) в запросе -- 50 (уточнить значение).

    Attributes:
        delivery: Сведения о поставке. Поставка соответствует множеству
            партий, следующих в одном транспортном средстве в адрес
            одного получателя. Для объекта delivery не заполняется
            элемент consignment -- считаем, что сведения о партии
            совпадают с данными входящего ВСД. Остальные элементы
            объекта delivery заполняются в соответствии с атрибутами
            поставки: consignor - отправитель consignee - получатель
            broker - посредник/перевозчик transportInfo - сведения о
            транспорте transportStorageType - режим хранения при
            перевозке shipmentRoute - маршрут следования В разделе
            accompanyingForms заполняются элементы waybill и
            vetCertificate, элемент vetCertificate указывается для
            каждого ВСД из поставки. Идентификатор входящего
            электронного ВСД передаётся в поле vetCertificate/uuid. Все
            перечисленные в блоке accompanyingForms/vetCertificate ВСД
            должны соответствовать сведениям о поставке, указанным в
            блоке delivery: consignor - отправитель consignee -
            получатель broker - посредник/перевозчик transportInfo -
            сведения о транспорте transportStorageType - режим хранения
            при перевозке В случае несоответствия как минимум для одного
            ВСД заявка отклоняется полностью с соответствующей ошибкой.
        delivery_facts: Результаты приёмки. Допускаются следующие
            значения дочерних элементов: vetCertificatePresence =
            ELECTRONIC decision = ACCEPT_ALL, RETURN_ALL
            docInspection/result = CORRESPONDS vetInspection/result =
            CORRESPONDS Если значения для этих полей в запросе
            отличаются от допустимых, заявка отклоняется.
        returned_delivery: Сведения о возврате продукции. В случае
            возврата (RETURN_ALL) правила заполнения блока
            returnedDelivery те же, что и для операции
            ProcessIncomingConsignmentRequest. Блок consignment не
            заполняется -- считаем, что сведения о партии совпадают с
            данными входящего ВСД.
    """

    class Meta:
        name = "ProcessIncomingDeliveryRequest"

    model_config = ConfigDict(defer_build=True)
    delivery: Delivery = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    delivery_facts: DeliveryFactList = field(
        metadata={
            "name": "deliveryFacts",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    returned_delivery: Optional[Delivery] = field(
        default=None,
        metadata={
            "name": "returnedDelivery",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class RegisterProductionOperationRequestInternalType(
    MercuryApplicationRequest
):
    """Заявка на оформление производственной партии.

    Заявка поддерживает оформление "незавершенного" производства.

    Attributes:
        enterprise: Предприятие, на котором совершается производственная
            операция.
        production_operation: Производственная транзакция.
        vet_document: Сведения, необходимые для оформления ветеринарного
            сертификата.
    """

    class Meta:
        name = "RegisterProductionOperationRequest"

    model_config = ConfigDict(defer_build=True)
    enterprise: EnterpriseInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    production_operation: ProductionOperation = field(
        metadata={
            "name": "productionOperation",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    vet_document: list[VetDocumentInternalType] = field(
        default_factory=list,
        metadata={
            "name": "vetDocument",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class ResolveDiscrepancyRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на регистрацию несоответствий в записях складского журнала, выявленных в
    результате инвентаризации.

    Attributes:
        enterprise: Предприятие.
        inventory_date: Дата инвентаризации/обнаружения несоответствия.
        responsible: Ответственный за инвентаризацию.
        stock_discrepancy: Несоответствие в записях складского журнала.
        discrepancy_report: Акт о несоответствии.
    """

    class Meta:
        name = "ResolveDiscrepancyRequest"

    model_config = ConfigDict(defer_build=True)
    enterprise: EnterpriseInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    inventory_date: XmlDateTime = field(
        metadata={
            "name": "inventoryDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    responsible: UserInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    stock_discrepancy: list[StockDiscrepancy] = field(
        default_factory=list,
        metadata={
            "name": "stockDiscrepancy",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "min_occurs": 1,
        },
    )
    discrepancy_report: list[DiscrepancyReport] = field(
        default_factory=list,
        metadata={
            "name": "discrepancyReport",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "min_occurs": 1,
        },
    )


class UnbindBusinessEntityUserRequestInternalType(MercuryApplicationRequest):
    """
    Запрос на удаление пользователя (открепление пользователя от ХС-заявителя)

    Attributes:
        user: Пользователь, которого необходимо удалить. Должен быть
            указан `uuid` или `login`.
    """

    class Meta:
        name = "UnbindBusinessEntityUserRequest"

    model_config = ConfigDict(defer_build=True)
    user: list[User] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "min_occurs": 1,
        },
    )


class UpdateTransportMovementDetailsRequestInternalType(
    MercuryApplicationRequest
):
    """Заявка на изменение сведений о транспортных средствах, осуществляющих
    доставку сертифицированной партии.

    Поддерживается уполномоченное выполнение.

    Attributes:
        delivery_participant: Грузополучатель или грузоотправитель,
            осуществляющий изменение параметров маршрута.
        vet_document_uuid: Идентификатор транспортного вет.сертификата.
            Может быть указано более одного сертификата на партии,
            оформленные строго в одной поставк в адрес одного
            получателя.
        shipment_route: Маршрут следования. Указывается список точек
            перегрузки и сведения о транспорте. Для точки перегрузки
            должен быть указан её идентификатор (uuid). В запросе на
            изменение могут участвовать только точки маршрута, для
            которых установлен флаг transshipment (точка перегрузки).
    """

    class Meta:
        name = "UpdateTransportMovementDetailsRequest"

    model_config = ConfigDict(defer_build=True)
    delivery_participant: DeliveryParticipant = field(
        metadata={
            "name": "deliveryParticipant",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )
    vet_document_uuid: list[VetDocumentUuid] = field(
        default_factory=list,
        metadata={
            "name": "vetDocumentUuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "min_occurs": 1,
        },
    )
    shipment_route: ShipmentRoute = field(
        metadata={
            "name": "shipmentRoute",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "required": True,
        }
    )


class UpdateUserAuthoritiesRequestInternalType(MercuryApplicationRequest):
    """Запрос на изменение прав доступа пользователя.

    Роли пользователя и статус его активности изменяются только
    применительно к ХС-заявителю.

    Attributes:
        user: Пользователь, для которого изменяются права доступа.
            Должен быть указан `uuid` или `login`. Изменяются поля:
            `enabled` -- активность учетной записи пользователя
            `authorityList` -- роли пользователя
    """

    class Meta:
        name = "UpdateUserAuthoritiesRequest"

    model_config = ConfigDict(defer_build=True)
    user: list[User] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "min_occurs": 1,
        },
    )


class UpdateUserWorkingAreasRequestInternalType(MercuryApplicationRequest):
    """
    Запрос на изменение зон ответственности пользователя.

    Attributes:
        user: Пользователь, для которого изменяются права доступа.
            Должен быть указан `uuid` или `login`. Изменяются поля:
            `workingAreaList` -- зоны ответственности пользователя
    """

    class Meta:
        name = "UpdateUserWorkingAreasRequest"

    model_config = ConfigDict(defer_build=True)
    user: list[User] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "min_occurs": 1,
        },
    )


class UpdateVeterinaryEventsRequestInternalType(MercuryApplicationRequest):
    """Заявка на внесение сведений о ветеринарных мероприятиях с партией продукции
    таких, как лабораторные исследования, карантинирование, иммунизации и обработки
    для живых животных.

    Поддерживается обновление сведений о лабораторных исследованиях, для
    которых ранее не был указан результат исследования.

    Attributes:
        enterprise: Предприятие.
        stock_entry: Запись складского журнала, для которой
            вносятся/обновляются сведения о мероприятиях. Может быть
            указано более одной записи складского журнала. Для каждой
            записи должен быть указан идентификатор (GUID) и список
            мероприятий stockEntry/vetEventList. При обновлении
            результатов лабораторных исследований у соответствующего
            stockEntry/vetEventList/laboratoryResearch должен быть
            указан идентификатор ID.
    """

    class Meta:
        name = "UpdateVeterinaryEventsRequest"

    model_config = ConfigDict(defer_build=True)
    enterprise: EnterpriseInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    stock_entry: list[StockEntry] = field(
        default_factory=list,
        metadata={
            "name": "stockEntry",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/vet-document/v2",
            "min_occurs": 1,
        },
    )


class WithdrawVetDocumentRequestInternalType(MercuryApplicationRequest):
    """
    Заявка на аннулирование ветеринарного сертификата.

    Attributes:
        vet_document_id: Идентификатор аннулируемого сертификата.
        withdraw_reason: Причина аннулирования.
        withdraw_date: Дата аннулирования.
        specified_person: Ветеринарный врач, ответственный за
            аннулирование сертификата.
    """

    class Meta:
        name = "WithdrawVetDocumentRequest"

    model_config = ConfigDict(defer_build=True)
    vet_document_id: str = field(
        metadata={
            "name": "vetDocumentId",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )
    withdraw_reason: str = field(
        metadata={
            "name": "withdrawReason",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    withdraw_date: XmlDateTime = field(
        metadata={
            "name": "withdrawDate",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
            "required": True,
        }
    )
    specified_person: Optional[UserInternalType] = field(
        default=None,
        metadata={
            "name": "specifiedPerson",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2",
        },
    )


class AddBusinessEntityUserResponse(
    ApplicationResponse, AddBusinessEntityUserResponseInternalType
):
    class Meta:
        name = "addBusinessEntityUserResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class CheckShipmentRegionalizationResponse(
    ApplicationResponse, CheckShipmentRegionalizationResponseInternalType
):
    class Meta:
        name = "checkShipmentRegionalizationResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetApplicableUserAuthorityListResponse(
    ApplicationResponse, GetApplicableUserAuthorityListResponseInternalType
):
    class Meta:
        name = "getApplicableUserAuthorityListResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetBusinessEntityUserListResponse(
    ApplicationResponse, GetBusinessEntityUserListResponseInternalType
):
    class Meta:
        name = "getBusinessEntityUserListResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetBusinessEntityUserResponse(
    ApplicationResponse, GetBusinessEntityUserResponseInternalType
):
    class Meta:
        name = "getBusinessEntityUserResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetStockEntryByGuidResponse(
    ApplicationResponse, GetStockEntryByGuidResponseInternalType
):
    class Meta:
        name = "getStockEntryByGuidResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetStockEntryByUuidResponse(
    ApplicationResponse, GetStockEntryByUuidResponseInternalType
):
    class Meta:
        name = "getStockEntryByUuidResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetStockEntryChangesListResponse(
    ApplicationResponse, GetStockEntryChangesListResponseInternalType
):
    class Meta:
        name = "getStockEntryChangesListResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetStockEntryListResponse(
    ApplicationResponse, GetStockEntryListResponseInternalType
):
    class Meta:
        name = "getStockEntryListResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetStockEntryVersionListResponse(
    ApplicationResponse, GetStockEntryVersionListResponseInternalType
):
    class Meta:
        name = "getStockEntryVersionListResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetVetDocumentByUuidResponse(
    ApplicationResponse, GetVetDocumentByUuidResponseInternalType
):
    class Meta:
        name = "getVetDocumentByUuidResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetVetDocumentChangesListResponse(
    ApplicationResponse, GetVetDocumentChangesListResponseInternalType
):
    class Meta:
        name = "getVetDocumentChangesListResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetVetDocumentListResponse(
    ApplicationResponse, GetVetDocumentListResponseInternalType
):
    class Meta:
        name = "getVetDocumentListResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class MergeStockEntriesResponse(
    ApplicationResponse, MergeStockEntriesResponseInternalType
):
    class Meta:
        name = "mergeStockEntriesResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ModifyActivityLocationsResponse(
    ApplicationResponse, ModifyActivityLocationsResponseInternalType
):
    class Meta:
        name = "modifyActivityLocationsResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ModifyBusinessEntityResponse(
    ApplicationResponse, ModifyBusinessEntityResponseInternalType
):
    class Meta:
        name = "modifyBusinessEntityResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ModifyEnterpriseResponse(
    ApplicationResponse, ModifyEnterpriseResponseInternalType
):
    class Meta:
        name = "modifyEnterpriseResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ModifyProducerStockListResponse(
    ApplicationResponse, ModifyProducerStockListResponseInternalType
):
    class Meta:
        name = "modifyProducerStockListResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class PrepareOutgoingConsignmentResponse(
    ApplicationResponse, PrepareOutgoingConsignmentResponseInternalType
):
    class Meta:
        name = "prepareOutgoingConsignmentResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ProcessIncomingConsignmentResponse(
    ApplicationResponse, ProcessIncomingConsignmentResponseInternalType
):
    class Meta:
        name = "processIncomingConsignmentResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ProcessIncomingDeliveryResponse(
    ApplicationResponse, ProcessIncomingDeliveryResponseInternalType
):
    class Meta:
        name = "processIncomingDeliveryResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class RegisterProductionOperationResponse(
    ApplicationResponse, RegisterProductionOperationResponseInternalType
):
    class Meta:
        name = "registerProductionOperationResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ResolveDiscrepancyResponse(
    ApplicationResponse, ResolveDiscrepancyResponseInternalType
):
    class Meta:
        name = "resolveDiscrepancyResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class UnbindBusinessEntityUserResponse(
    ApplicationResponse, UnbindBusinessEntityUserResponseInternalType
):
    class Meta:
        name = "unbindBusinessEntityUserResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class UpdateTransportMovementDetailsResponse(
    ApplicationResponse, UpdateTransportMovementDetailsResponseInternalType
):
    class Meta:
        name = "updateTransportMovementDetailsResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class UpdateUserAuthoritiesResponse(
    ApplicationResponse, UpdateUserAuthoritiesResponseInternalType
):
    class Meta:
        name = "updateUserAuthoritiesResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class UpdateUserWorkingAreasResponse(
    ApplicationResponse, UpdateUserWorkingAreasResponseInternalType
):
    class Meta:
        name = "updateUserWorkingAreasResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class UpdateVeterinaryEventsResponse(
    ApplicationResponse, UpdateVeterinaryEventsResponseInternalType
):
    class Meta:
        name = "updateVeterinaryEventsResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class WithdrawVetDocumentResponse(
    ApplicationResponse, WithdrawVetDocumentResponseInternalType
):
    class Meta:
        name = "withdrawVetDocumentResponse"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class AddBusinessEntityUserRequest(
    ApplicationRequest, AddBusinessEntityUserRequestInternalType
):
    class Meta:
        name = "addBusinessEntityUserRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class CheckShipmentRegionalizationRequest(
    ApplicationRequest, CheckShipmentRegionalizationRequestInternalType
):
    class Meta:
        name = "checkShipmentRegionalizationRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetApplicableUserAuthorityListRequest(
    ApplicationRequest, GetApplicableUserAuthorityListRequestInternalType
):
    class Meta:
        name = "getApplicableUserAuthorityListRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetBusinessEntityUserListRequest(
    ApplicationRequest, GetBusinessEntityUserListRequestInternalType
):
    class Meta:
        name = "getBusinessEntityUserListRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetBusinessEntityUserRequest(
    ApplicationRequest, GetBusinessEntityUserRequestInternalType
):
    class Meta:
        name = "getBusinessEntityUserRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetStockEntryByGuidRequest(
    ApplicationRequest, GetStockEntryByGuidRequestInternalType
):
    class Meta:
        name = "getStockEntryByGuidRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetStockEntryByUuidRequest(
    ApplicationRequest, GetStockEntryByUuidRequestInternalType
):
    class Meta:
        name = "getStockEntryByUuidRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetStockEntryChangesListRequest(
    ApplicationRequest, GetStockEntryChangesListRequestInternalType
):
    class Meta:
        name = "getStockEntryChangesListRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetStockEntryListRequest(
    ApplicationRequest, GetStockEntryListRequestInternalType
):
    class Meta:
        name = "getStockEntryListRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetStockEntryVersionListRequest(
    ApplicationRequest, GetStockEntryVersionListRequestInternalType
):
    class Meta:
        name = "getStockEntryVersionListRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetVetDocumentByUuidRequest(
    ApplicationRequest, GetVetDocumentByUuidRequestInternalType
):
    class Meta:
        name = "getVetDocumentByUuidRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetVetDocumentChangesListRequest(
    ApplicationRequest, GetVetDocumentChangesListRequestInternalType
):
    class Meta:
        name = "getVetDocumentChangesListRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class GetVetDocumentListRequest(
    ApplicationRequest, GetVetDocumentListRequestInternalType
):
    class Meta:
        name = "getVetDocumentListRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class MergeStockEntriesRequest(
    ApplicationRequest, MergeStockEntriesRequestInternalType
):
    class Meta:
        name = "mergeStockEntriesRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ModifyActivityLocationsRequest(
    ApplicationRequest, ModifyActivityLocationsRequestInternalType
):
    class Meta:
        name = "modifyActivityLocationsRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ModifyBusinessEntityRequest(
    ApplicationRequest, ModifyBusinessEntityRequestInternalType
):
    class Meta:
        name = "modifyBusinessEntityRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ModifyEnterpriseRequest(
    ApplicationRequest, ModifyEnterpriseRequestInternalType
):
    class Meta:
        name = "modifyEnterpriseRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ModifyProducerStockListRequest(
    ApplicationRequest, ModifyProducerStockListRequestInternalType
):
    class Meta:
        name = "modifyProducerStockListRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class PrepareOutgoingConsignmentRequest(
    ApplicationRequest, PrepareOutgoingConsignmentRequestInternalType
):
    class Meta:
        name = "prepareOutgoingConsignmentRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ProcessIncomingConsignmentRequest(
    ApplicationRequest, ProcessIncomingConsignmentRequestInternalType
):
    class Meta:
        name = "processIncomingConsignmentRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ProcessIncomingDeliveryRequest(
    ApplicationRequest, ProcessIncomingDeliveryRequestInternalType
):
    class Meta:
        name = "processIncomingDeliveryRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class RegisterProductionOperationRequest(
    ApplicationRequest, RegisterProductionOperationRequestInternalType
):
    class Meta:
        name = "registerProductionOperationRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class ResolveDiscrepancyRequest(
    ApplicationRequest, ResolveDiscrepancyRequestInternalType
):
    class Meta:
        name = "resolveDiscrepancyRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class UnbindBusinessEntityUserRequest(
    ApplicationRequest, UnbindBusinessEntityUserRequestInternalType
):
    class Meta:
        name = "unbindBusinessEntityUserRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class UpdateTransportMovementDetailsRequest(
    ApplicationRequest, UpdateTransportMovementDetailsRequestInternalType
):
    class Meta:
        name = "updateTransportMovementDetailsRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class UpdateUserAuthoritiesRequest(
    ApplicationRequest, UpdateUserAuthoritiesRequestInternalType
):
    class Meta:
        name = "updateUserAuthoritiesRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class UpdateUserWorkingAreasRequest(
    ApplicationRequest, UpdateUserWorkingAreasRequestInternalType
):
    class Meta:
        name = "updateUserWorkingAreasRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class UpdateVeterinaryEventsRequest(
    ApplicationRequest, UpdateVeterinaryEventsRequestInternalType
):
    class Meta:
        name = "updateVeterinaryEventsRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)


class WithdrawVetDocumentRequest(
    ApplicationRequest, WithdrawVetDocumentRequestInternalType
):
    class Meta:
        name = "withdrawVetDocumentRequest"
        namespace = (
            "http://api.vetrf.ru/schema/cdm/mercury/g2b/applications/v2"
        )

    model_config = ConfigDict(defer_build=True)
