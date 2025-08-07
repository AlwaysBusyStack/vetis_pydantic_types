from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict

from vetis_pydantic_types.base import ApplicationRequest, ApplicationResponse
from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.mercury.types.base_v2_0 import (
    Guid,
    ListOptions,
    UpdateDateInterval,
    Uuid,
)
from vetis_pydantic_types.mercury.types.dictionary_v2_1 import (
    ActivityLocationList,
    BusinessEntity,
    BusinessEntityList,
    BusinessMember,
    Country,
    CountryGuid,
    CountryList,
    Disease,
    DiseaseList,
    District,
    DistrictGuid,
    DistrictList,
    Enterprise,
    EnterpriseGroup,
    EnterpriseList,
    GlobalId,
    LocalityGuid,
    LocalityList,
    Producer,
    Product,
    ProductGuid,
    ProductItem,
    ProductItemList,
    ProductList,
    ProductType,
    Purpose,
    PurposeList,
    R13NConditionList,
    R13NRegionStatusList,
    R13NShippingRuleList,
    R13NZone,
    Region,
    RegionGuid,
    RegionList,
    ResearchMethod,
    ResearchMethodList,
    StreetList,
    SubProduct,
    SubProductList,
    Unit,
    UnitList,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"


class FindLocalityListByNameRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка населенных пунктов по шаблону и родителю(региону).

    Attributes:
        list_options: Параметры запрашиваемого списка.
        region_guid: Глобальный идентификатор региона, для которой
            запрашивается список населенных пунктов.
        pattern: Шаблон для поиска в именах населенных пунктов.
    """

    class Meta:
        name = "findLocalityListByNameRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    region_guid: RegionGuid = field(
        metadata={
            "name": "regionGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    pattern: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class FindLocalityListByNameResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка населенных пунктов по региону.

    Attributes:
        locality_list: Список населенных пунктов указанного региона.
    """

    class Meta:
        name = "findLocalityListByNameResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    locality_list: LocalityList = field(
        metadata={
            "name": "localityList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class FindStreetListByNameRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка улиц по шаблону и родителю(населенному пункту).

    Attributes:
        list_options: Параметры запрашиваемого списка.
        locality_guid: Глобальный идентификатор населенного пункта, для
            которой запрашивается список улиц.
        pattern: Шаблон для поиска в именах улиц.
    """

    class Meta:
        name = "findStreetListByNameRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    locality_guid: LocalityGuid = field(
        metadata={
            "name": "localityGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    pattern: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class FindStreetListByNameResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка улиц по населенному пункту.

    Attributes:
        street_list: Список улиц указанного населенного пункта.
    """

    class Meta:
        name = "findStreetListByNameResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    street_list: StreetList = field(
        metadata={
            "name": "streetList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetActivityLocationListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка предприятий, связанных с указанным ХСом.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        business_entity: Хозяйствующий субъект, осуществляющий
            деятельность. Должны быть заполнено одно из полей: `uuid`,
            `guid`, `inn`.
    """

    class Meta:
        name = "getActivityLocationListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    business_entity: BusinessEntity = field(
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetActivityLocationListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка предприятий.

    Attributes:
        activity_location_list: Список предприятий.
    """

    class Meta:
        name = "getActivityLocationListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    activity_location_list: ActivityLocationList = field(
        metadata={
            "name": "activityLocationList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetActualR13NRegionStatusListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение статусов региона (регионализация).

    Attributes:
        list_options: Параметры запрашиваемого списка.
        disease: Заболевание, по которому запрашиваются статусы
            регионов.
        r13n_zone: (Опционально) Регион, по которому запрашиваются
            статусы.
    """

    class Meta:
        name = "getActualR13nRegionStatusListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    disease: Disease = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    r13n_zone: Optional[R13NZone] = field(
        default=None,
        metadata={
            "name": "r13nZone",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetActualR13NRegionStatusListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения статусов региона (регионализация).

    Attributes:
        r13n_region_status_list: Список статусов региона
            (регионализация).
    """

    class Meta:
        name = "getActualR13nRegionStatusListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    r13n_region_status_list: R13NRegionStatusList = field(
        metadata={
            "name": "r13nRegionStatusList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetActualR13NShippingRuleListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение пары ХС-площадка по глобальному идентификатору GLN.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        disease: Заболевание, по которому запрашиваются статусы
            регионов.
        product_type: (Опционально) Ветеринарная категория груза (тип
            продукции), для которой запрашиваются правила перемещения.
        product: (Опционально) Ветеринарная категория груза (продукция),
            для которой запрашиваются правила перемещения.
        sub_product: (Опционально) Ветеринарная категория груза (вид
            продукции), для которой запрашиваются правила перемещения.
    """

    class Meta:
        name = "getActualR13nShippingRuleListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    disease: Disease = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
    product_type: Optional[ProductType] = field(
        default=None,
        metadata={
            "name": "productType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    product: Optional[Product] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    sub_product: Optional[SubProduct] = field(
        default=None,
        metadata={
            "name": "subProduct",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetActualR13NShippingRuleListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи ХС по глобальному идентификатору.

    Attributes:
        r13n_shipping_rule_list: Список правил перемещения груза
            (регионализация).
    """

    class Meta:
        name = "getActualR13nShippingRuleListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    r13n_shipping_rule_list: R13NShippingRuleList = field(
        metadata={
            "name": "r13nShippingRuleList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetAllCountryListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения списка активных записей стран.

    Attributes:
        list_options: Параметры запрашиваемого списка.
    """

    class Meta:
        name = "getAllCountryListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )


class GetAllCountryListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения актуального списка стран.

    Attributes:
        country_list: Список актуальных записей стран.
    """

    class Meta:
        name = "getAllCountryListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    country_list: CountryList = field(
        metadata={
            "name": "countryList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetBusinessEntityByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение записи ХС по глобальному идентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getBusinessEntityByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetBusinessEntityByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи ХС по глобальному идентификатору.

    Attributes:
        business_entity: Запись ХС.
    """

    class Meta:
        name = "getBusinessEntityByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    business_entity: BusinessEntity = field(
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetBusinessEntityByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение записи ХС по идентфикатору.

    Attributes:
        uuid: Идентификатор, по которому производится поиск записи.
    """

    class Meta:
        name = "getBusinessEntityByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetBusinessEntityByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи ХС по идентификатору.

    Attributes:
        business_entity: Запись ХС.
    """

    class Meta:
        name = "getBusinessEntityByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    business_entity: BusinessEntity = field(
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetBusinessEntityChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка изменившихся записей ХС.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getBusinessEntityChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetBusinessEntityChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка изменений записей ХС.

    Attributes:
        business_entity_list: Список записей ХС.
    """

    class Meta:
        name = "getBusinessEntityChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    business_entity_list: BusinessEntityList = field(
        metadata={
            "name": "businessEntityList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetBusinessEntityListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка ХС.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        business_entity: Параметр фильтрации ХС.
    """

    class Meta:
        name = "getBusinessEntityListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    business_entity: Optional[BusinessEntity] = field(
        default=None,
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetBusinessEntityListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка ХС.

    Attributes:
        business_entity_list: Список ХС.
    """

    class Meta:
        name = "getBusinessEntityListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    business_entity_list: BusinessEntityList = field(
        metadata={
            "name": "businessEntityList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetBusinessMemberByGlnrequest(BaseModel):
    """
    Запрос на получение пары ХС-площадка по глобальному идентификатору GLN.

    Attributes:
        global_id: Глобальный идентификатор (GLN), по которому
            проводится поиск записи.
    """

    class Meta:
        name = "getBusinessMemberByGLNRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    global_id: GlobalId = field(
        metadata={
            "name": "globalID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetBusinessMemberByGlnresponse(BaseModel):
    """
    Ответ на запрос получения записи ХС по глобальному идентификатору.

    Attributes:
        business_member: Запись ХС.
    """

    class Meta:
        name = "getBusinessMemberByGLNResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    business_member: BusinessMember = field(
        metadata={
            "name": "businessMember",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetCountryByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения объекта страны по глобальному идентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getCountryByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetCountryByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос на получения объекта страны по глобальному идентификатору.

    Attributes:
        country: Найденный по guid-у объект страны.
    """

    class Meta:
        name = "getCountryByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    country: Country = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetCountryByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения объекта страны по идентификатору.

    Attributes:
        uuid: идентификатор, по которому проводится поиск записи.
    """

    class Meta:
        name = "getCountryByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetCountryByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос на получения объекта страны по идентификатору.

    Attributes:
        country: Найденный по uuid-у объект страны.
    """

    class Meta:
        name = "getCountryByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    country: Country = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetCountryChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение изменений в списке стран, начиная с указанной даты.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getCountryChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetCountryChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения изменений в списке стран.

    Attributes:
        country_list: Список стран, в не зависимости от статуса.
    """

    class Meta:
        name = "getCountryChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    country_list: CountryList = field(
        metadata={
            "name": "countryList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetDiseaseByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение заболевания по глобальному идентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getDiseaseByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetDiseaseByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения заболевания по глобальному идентификатору.

    Attributes:
        disease: Найденная по глобальному идентификатору запись
            заболевания.
    """

    class Meta:
        name = "getDiseaseByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    disease: Disease = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetDiseaseByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение записи заболевания по ее идентификатору.

    Attributes:
        uuid: Идентификатор, по которому производится поиск записи.
    """

    class Meta:
        name = "getDiseaseByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetDiseaseByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи заболевания по идентификатору.

    Attributes:
        disease: Найденная по идентификатору запись заболевания.
    """

    class Meta:
        name = "getDiseaseByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    disease: Disease = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetDiseaseChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка изменившихся записей заболеваний.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getDiseaseChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetDiseaseChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка изменившихся записей заболеваний.

    Attributes:
        disease_list: Список записей заболеваний.
    """

    class Meta:
        name = "getDiseaseChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    disease_list: DiseaseList = field(
        metadata={
            "name": "diseaseList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetDiseaseListRequest(BaseModel, ApplicationRequest):
    """
    Запрос списка заболеваний.

    Attributes:
        list_options: Параметры запрашиваемого списка.
    """

    class Meta:
        name = "getDiseaseListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )


class GetDiseaseListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос списка заболеваний.

    Attributes:
        disease_list: Список заболеваний.
    """

    class Meta:
        name = "getDiseaseListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    disease_list: DiseaseList = field(
        metadata={
            "name": "diseaseList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetDistrictByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения объекта района по глобальному идентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getDistrictByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetDistrictByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос на получения объекта района по глобальному идентификатору.

    Attributes:
        district: Найденный по guid-у объект района.
    """

    class Meta:
        name = "getDistrictByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    district: District = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetDistrictByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения объекта района по глобальному идентификатору.

    Attributes:
        uuid: Идентификатор, по которому проводится поиск записи.
    """

    class Meta:
        name = "getDistrictByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetDistrictByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос на получения объекта района по глобальному идентификатору.

    Attributes:
        district: Найденный по guid-у объект района.
    """

    class Meta:
        name = "getDistrictByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    district: District = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetDistrictChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение изменений в списке районов, начиная с указанной даты.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getDistrictChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetDistrictChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения изменений в списке районов.

    Attributes:
        district_list: Список районов, в не зависимости от статуса
            объекта.
    """

    class Meta:
        name = "getDistrictChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    district_list: DistrictList = field(
        metadata={
            "name": "districtList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetDistrictListByRegionRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка районов указанного региона.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        region_guid: Глобальный идентификатор региона, для которой
            запрашивается список регионов.
    """

    class Meta:
        name = "getDistrictListByRegionRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    region_guid: RegionGuid = field(
        metadata={
            "name": "regionGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetDistrictListByRegionResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка районов региона.

    Attributes:
        district_list: Список районов указанного региона в заданном
            формате.
    """

    class Meta:
        name = "getDistrictListByRegionResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    district_list: DistrictList = field(
        metadata={
            "name": "districtList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetEnterpriseByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение записи предприятия по глобальномуидентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getEnterpriseByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetEnterpriseByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи предприятия по глобальному идентификатору.

    Attributes:
        enterprise: Запись ХС.
    """

    class Meta:
        name = "getEnterpriseByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    enterprise: Enterprise = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetEnterpriseByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение записи предприятия по идентфикатору.

    Attributes:
        uuid: Идентификатор, по которому производится поиск записи.
    """

    class Meta:
        name = "getEnterpriseByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetEnterpriseByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи предприятия по идентификатору.

    Attributes:
        enterprise: Запись ХС.
    """

    class Meta:
        name = "getEnterpriseByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    enterprise: Enterprise = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetForeignEnterpriseChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка изменившихся записей предприятий.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getForeignEnterpriseChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetForeignEnterpriseChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка изменений записей предприятий.

    Attributes:
        enterprise_list: Список записей предприятий.
    """

    class Meta:
        name = "getForeignEnterpriseChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    enterprise_list: EnterpriseList = field(
        metadata={
            "name": "enterpriseList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetForeignEnterpriseListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка зарубежныйх предприятий.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        enterprise_group: Параметр запроса предприятий.
        enterprise: Параметр запроса предприятий.
    """

    class Meta:
        name = "getForeignEnterpriseListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    enterprise_group: Optional[EnterpriseGroup] = field(
        default=None,
        metadata={
            "name": "enterpriseGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    enterprise: Optional[Enterprise] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetForeignEnterpriseListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка зарубежных предприятий.

    Attributes:
        enterprise_list: Список предприятий.
    """

    class Meta:
        name = "getForeignEnterpriseListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    enterprise_list: EnterpriseList = field(
        metadata={
            "name": "enterpriseList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetLocalityChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение изменений в списке населенных пунктов, начиная с указанной
    даты.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getLocalityChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetLocalityChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения изменений в списке населенных пунктов.

    Attributes:
        locality_list: Список населенных пунктов, вне зависимости от
            статуса объекта.
    """

    class Meta:
        name = "getLocalityChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    locality_list: LocalityList = field(
        metadata={
            "name": "localityList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetLocalityListByDistrictRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка населенных пунктов по району.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        district_guid: Глобальный идентификатор районы, для которой
            запрашивается список населенных пунктов.
    """

    class Meta:
        name = "getLocalityListByDistrictRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    district_guid: DistrictGuid = field(
        metadata={
            "name": "districtGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetLocalityListByDistrictResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка населенных пунктов по району.

    Attributes:
        locality_list: Список населенных пунктов указанного района.
    """

    class Meta:
        name = "getLocalityListByDistrictResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    locality_list: LocalityList = field(
        metadata={
            "name": "localityList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetLocalityListByLocalityRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка зависимых населенных пунктов по населенному пункту.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        locality_guid: Глобальный идентификатор населенного пункта, для
            которой запрашивается список зависимых населенных пунктов.
    """

    class Meta:
        name = "getLocalityListByLocalityRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    locality_guid: LocalityGuid = field(
        metadata={
            "name": "localityGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetLocalityListByLocalityResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка зависимых населенных пунктов по населенному
    пункту.

    Attributes:
        locality_list: Список завимиых населенных пунктов указанного
            населенного пункта.
    """

    class Meta:
        name = "getLocalityListByLocalityResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    locality_list: LocalityList = field(
        metadata={
            "name": "localityList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetLocalityListByRegionRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка населенных пунктов по региону.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        region_guid: Глобальный идентификатор региона, для которой
            запрашивается список населенных пунктов.
    """

    class Meta:
        name = "getLocalityListByRegionRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    region_guid: RegionGuid = field(
        metadata={
            "name": "regionGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetLocalityListByRegionResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка населенных пунктов по региону.

    Attributes:
        locality_list: Список населенных пунктов указанного региона.
    """

    class Meta:
        name = "getLocalityListByRegionResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    locality_list: LocalityList = field(
        metadata={
            "name": "localityList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetProductByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения продукции по глобальному идентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getProductByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetProductByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения продукции по глобальному идентификатору.

    Attributes:
        product: Найденная по глобальному идентификатору запись
            продукции.
    """

    class Meta:
        name = "getProductByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    product: Product = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetProductByTypeListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения списка активных записей продукции.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        product_type: Идентификатор типа продукта, по которому будет
            осуществлен поиск.
    """

    class Meta:
        name = "getProductByTypeListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    product_type: ProductType = field(
        metadata={
            "name": "productType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetProductByTypeListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка активных записей продукции.

    Attributes:
        product_list: Список записей продукции.
    """

    class Meta:
        name = "getProductByTypeListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    product_list: ProductList = field(
        metadata={
            "name": "productList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetProductByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение записи продукции по идентификатору.

    Attributes:
        uuid: Идентификатор записи, по которому проводится поиск.
    """

    class Meta:
        name = "getProductByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetProductByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи продукции по идентификатору.

    Attributes:
        product: Найденая по идентификатору запись продукции.
    """

    class Meta:
        name = "getProductByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    product: Product = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetProductChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка изменившихся записей продукции.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getProductChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetProductChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка изменений записей продукции.

    Attributes:
        product_list: Список записей типов продукции.
    """

    class Meta:
        name = "getProductChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    product_list: ProductList = field(
        metadata={
            "name": "productList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetProductItemByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения наименований продукции по глобальному идентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getProductItemByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetProductItemByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения наименований продукции по глобальному идентификатору.

    Attributes:
        product_item: Найденная по глобальному идентификатору запись
            наименований продукции.
    """

    class Meta:
        name = "getProductItemByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    product_item: Optional[ProductItem] = field(
        default=None,
        metadata={
            "name": "productItem",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetProductItemByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение записи наименований продукции по идентификатору.

    Attributes:
        uuid: Идентификатор записи, по которому проводится поиск.
    """

    class Meta:
        name = "getProductItemByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetProductItemByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи наименований продукции по идентификатору.

    Attributes:
        product_item: Найденая по идентификатору запись наименований
            продукции.
    """

    class Meta:
        name = "getProductItemByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    product_item: Optional[ProductItem] = field(
        default=None,
        metadata={
            "name": "productItem",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetProductItemChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка изменившихся записей наименований продукции.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
        business_entity: Идентификатор хозяйствующего субъекта,
            справочник которого запрашивается.
        enterprise: [DEPRECATED] Идентификатор предприятия-производителя
            продукции. Вместо этого используйте producer/enterprise.
        producer: Производитель продукции. Поиск может осуществляться по
            ХС-производителю и/или площадке, на которой выпускается
            продукция: поля producer/businessEntity/guid и
            producer/enterprise/guid соответственно.
    """

    class Meta:
        name = "getProductItemChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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
    business_entity: Optional[BusinessEntity] = field(
        default=None,
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    enterprise: Optional[Enterprise] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    producer: Optional[Producer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetProductItemChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка изменений записей наименований продукции.

    Attributes:
        product_item_list: Список записей типов наименований продукции.
    """

    class Meta:
        name = "getProductItemChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    product_item_list: Optional[ProductItemList] = field(
        default=None,
        metadata={
            "name": "productItemList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetProductItemListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения списка активных записей наименований продукции.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        product_type: Идентификатор вида продукции, по которому будет
            осуществлен поиск.
        product: Идентификатор вида продукции, по которому будет
            осуществлен поиск.
        sub_product: Идентификатор вида продукции, по которому будет
            осуществлен поиск.
        business_entity: Идентификатор хозяйствующего субъекта,
            справочник которого запрашивается. В результирующий список
            попадут все публичные записи справочника хозяйствующего
            субъекта.
        enterprise: [DEPRECATED] Идентификатор предприятия-производителя
            продукции. Вместо этого используйте поле
            producer/enterprise.
        producer: Производитель продукции. Поиск может осуществляться по
            ХС-производителю и/или площадке, на которой выпускается
            продукция: поля producer/businessEntity/guid и
            producer/enterprise/guid соответственно.
        global_id: Global Trade Identification Number (GTIN) -
            уникальный идентификационный номер продукции производителя.
    """

    class Meta:
        name = "getProductItemListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    product_type: Optional[ProductType] = field(
        default=None,
        metadata={
            "name": "productType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    product: Optional[Product] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    sub_product: Optional[SubProduct] = field(
        default=None,
        metadata={
            "name": "subProduct",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    business_entity: Optional[BusinessEntity] = field(
        default=None,
        metadata={
            "name": "businessEntity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    enterprise: Optional[Enterprise] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    producer: Optional[Producer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )
    global_id: Optional[GlobalId] = field(
        default=None,
        metadata={
            "name": "globalID",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetProductItemListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка активных записей наименований продукции.

    Attributes:
        product_item_list: Список записей наименований продукции.
    """

    class Meta:
        name = "getProductItemListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    product_item_list: Optional[ProductItemList] = field(
        default=None,
        metadata={
            "name": "productItemList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetPurposeByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение назначения груза по глобальному идентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getPurposeByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetPurposeByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи назначения груза по глобальному
    идентификатору.

    Attributes:
        purpose: Запись назначения груза.
    """

    class Meta:
        name = "getPurposeByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    purpose: Purpose = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetPurposeByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение записи назначения груза по идентфикатору.

    Attributes:
        uuid: Идентификатор, по которому производится поиск записи.
    """

    class Meta:
        name = "getPurposeByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetPurposeByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи назначения груза по идентификатору.

    Attributes:
        purpose: Запись назначения груза.
    """

    class Meta:
        name = "getPurposeByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    purpose: Purpose = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetPurposeChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка изменившихся записей целей ввоза/вывоза.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getPurposeChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetPurposeChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка изменений записей назначений.

    Attributes:
        purpose_list: Список записей назначения груза.
    """

    class Meta:
        name = "getPurposeChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    purpose_list: PurposeList = field(
        metadata={
            "name": "purposeList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetPurposeListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка назначений.

    Attributes:
        list_options: Параметры запрашиваемого списка.
    """

    class Meta:
        name = "getPurposeListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )


class GetPurposeListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка целей.

    Attributes:
        purpose_list: Список целей.
    """

    class Meta:
        name = "getPurposeListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    purpose_list: PurposeList = field(
        metadata={
            "name": "purposeList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetR13NConditionListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка условий перемещения груза (регионализация).

    Attributes:
        list_options: Параметры запрашиваемого списка.
        disease: (Опционально) Заболевание, к которому относятся
            запрашиваемые условия перемещения груза.
    """

    class Meta:
        name = "getR13nConditionListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    disease: Optional[Disease] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetR13NConditionListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка условий перемещения груза (регионализация).

    Attributes:
        r13n_condition_list: Список условий перемещения груза.
    """

    class Meta:
        name = "getR13nConditionListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    r13n_condition_list: R13NConditionList = field(
        metadata={
            "name": "r13nConditionList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetRegionByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения объекта региона по глобальному идентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getRegionByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetRegionByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос на получения объекта региона по глобальному идентификатору.

    Attributes:
        region: Найденный по guid-у объект региона.
    """

    class Meta:
        name = "getRegionByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    region: Region = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetRegionByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения объекта региона по идентификатору.

    Attributes:
        uuid: Идентификатор, по которому проводится поиск записи.
    """

    class Meta:
        name = "getRegionByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetRegionByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос на получения объекта региона по идентификатору.

    Attributes:
        region: Найденный по uuid-у объект региона.
    """

    class Meta:
        name = "getRegionByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    region: Region = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetRegionChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение изменений в списке регионов, начиная с указанной даты.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getRegionChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetRegionChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения изменений в списке регионов.

    Attributes:
        region_list: Список регионов, в не зависимости от статуса.
    """

    class Meta:
        name = "getRegionChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    region_list: RegionList = field(
        metadata={
            "name": "regionList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetRegionListByCountryRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка регионов по стране.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        country_guid: Глобальный идентификатор страны, для которой
            запрашивается список регионов.
    """

    class Meta:
        name = "getRegionListByCountryRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    country_guid: CountryGuid = field(
        metadata={
            "name": "countryGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetRegionListByCountryResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка регионов по стране.

    Attributes:
        region_list: Список регионов указанной страны в заданном
            формате.
    """

    class Meta:
        name = "getRegionListByCountryResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    region_list: RegionList = field(
        metadata={
            "name": "regionList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetResearchMethodByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение метода исследований по глобальному идентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getResearchMethodByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetResearchMethodByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения метода исследований по глобальному идентификатору.

    Attributes:
        research_method: Найденная по глобальному идентификатору запись
            метода исследований.
    """

    class Meta:
        name = "getResearchMethodByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    research_method: ResearchMethod = field(
        metadata={
            "name": "researchMethod",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetResearchMethodByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение записи метода исследований по ее идентификатору.

    Attributes:
        uuid: Идентификатор, по которому производится поиск записи.
    """

    class Meta:
        name = "getResearchMethodByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetResearchMethodByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи метода исследований по идентификатору.

    Attributes:
        research_method: Найденная по идентификатору запись метода
            исследований.
    """

    class Meta:
        name = "getResearchMethodByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    research_method: ResearchMethod = field(
        metadata={
            "name": "researchMethod",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetResearchMethodChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка изменившихся записей методов исследований.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getResearchMethodChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetResearchMethodChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка изменившихся записей методов исследований.

    Attributes:
        research_method_list: Список записей методов исследований.
    """

    class Meta:
        name = "getResearchMethodChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    research_method_list: ResearchMethodList = field(
        metadata={
            "name": "researchMethodList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetResearchMethodListRequest(BaseModel, ApplicationRequest):
    """
    Запрос списка методов исследований.

    Attributes:
        list_options: Параметры запрашиваемого списка.
    """

    class Meta:
        name = "getResearchMethodListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )


class GetResearchMethodListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос списка методов исследований.

    Attributes:
        research_method_list: Список методов исследований.
    """

    class Meta:
        name = "getResearchMethodListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    research_method_list: ResearchMethodList = field(
        metadata={
            "name": "researchMethodList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetRussianEnterpriseChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка изменившихся записей предприятий.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getRussianEnterpriseChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetRussianEnterpriseChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка изменений записей предприятий.

    Attributes:
        enterprise_list: Список записей предприятий.
    """

    class Meta:
        name = "getRussianEnterpriseChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    enterprise_list: EnterpriseList = field(
        metadata={
            "name": "enterpriseList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetRussianEnterpriseListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка российских предприятий.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        enterprise: Параметр запроса предприятий.
    """

    class Meta:
        name = "getRussianEnterpriseListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    enterprise: Optional[Enterprise] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
        },
    )


class GetRussianEnterpriseListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка российских предприятий.

    Attributes:
        enterprise_list: Список предприятий.
    """

    class Meta:
        name = "getRussianEnterpriseListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    enterprise_list: EnterpriseList = field(
        metadata={
            "name": "enterpriseList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetStreetChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение изменений в списке улиц, начиная с указанной даты.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getStreetChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetStreetChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения изменений в списке улиц.

    Attributes:
        street_list: Список улиц, в не зависимости от статуса объекта.
    """

    class Meta:
        name = "getStreetChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    street_list: StreetList = field(
        metadata={
            "name": "streetList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetStreetListByLocalityRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка улиц по населенному пункту.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        locality_guid: Глобальный идентификатор населенного пункта, для
            которой запрашивается список улиц.
    """

    class Meta:
        name = "getStreetListByLocalityRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    locality_guid: LocalityGuid = field(
        metadata={
            "name": "localityGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetStreetListByLocalityResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка улиц по населенному пункту.

    Attributes:
        street_list: Список улиц указанного населенного пункта.
    """

    class Meta:
        name = "getStreetListByLocalityResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    street_list: StreetList = field(
        metadata={
            "name": "streetList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetSubProductByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения вида продукции по глобальному идентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getSubProductByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetSubProductByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения вида продукции по глобальному идентификатору.

    Attributes:
        sub_product: Найденный по глобальному идентификатору запись вида
            продукции.
    """

    class Meta:
        name = "getSubProductByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    sub_product: SubProduct = field(
        metadata={
            "name": "subProduct",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetSubProductByProductListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получения списка активных записей видов продукции.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        product_guid: Идентификатор продукта, по которому будет
            осуществлен поиск.
    """

    class Meta:
        name = "getSubProductByProductListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    product_guid: ProductGuid = field(
        metadata={
            "name": "productGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetSubProductByProductListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка активных записей видов продукции.

    Attributes:
        sub_product_list: Список записей видов продукции.
    """

    class Meta:
        name = "getSubProductByProductListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    sub_product_list: SubProductList = field(
        metadata={
            "name": "subProductList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetSubProductByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение записи вида продукции по идентификатору.

    Attributes:
        uuid: Идентификатор записи, по которому проводится поиск.
    """

    class Meta:
        name = "getSubProductByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetSubProductByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи видов продукции по идентификатору.

    Attributes:
        sub_product: Найденая по идентификатору запись вида продукции.
    """

    class Meta:
        name = "getSubProductByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    sub_product: SubProduct = field(
        metadata={
            "name": "subProduct",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetSubProductChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка изменившихся записей видов продукции.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getSubProductChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetSubProductChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка изменений записей видов продукции.

    Attributes:
        sub_product_list: Список записей видов продукции.
    """

    class Meta:
        name = "getSubProductChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    sub_product_list: SubProductList = field(
        metadata={
            "name": "subProductList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetUnitByGuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение единицы измерения по глобальному идентификатору.

    Attributes:
        guid: Глобальный идентификатор, по которому проводится поиск
            записи.
    """

    class Meta:
        name = "getUnitByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    guid: Guid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetUnitByGuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения единицы измерения по глобальному идентификатору.

    Attributes:
        unit: Найденная по глобальному идентификатору запись единицы
            измерения.
    """

    class Meta:
        name = "getUnitByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    unit: Unit = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetUnitByUuidRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение записи единицы измерения по ее идентификатору.

    Attributes:
        uuid: Идентификатор, по которому производится поиск записи.
    """

    class Meta:
        name = "getUnitByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    uuid: Uuid = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
            "required": True,
        }
    )


class GetUnitByUuidResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения записи единицы измерения по идентификатору.

    Attributes:
        unit: Найденная по идентификатору запись единицы измерения.
    """

    class Meta:
        name = "getUnitByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    unit: Unit = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetUnitChangesListRequest(BaseModel, ApplicationRequest):
    """
    Запрос на получение списка изменившихся записей единиц измерений.

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все записи, дата обновлений которых попадает в
            указанный интервал.
    """

    class Meta:
        name = "getUnitChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

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


class GetUnitChangesListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос получения списка изменившихся записей единиц измерений.

    Attributes:
        unit_list: Список записей единиц измерений.
    """

    class Meta:
        name = "getUnitChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    unit_list: UnitList = field(
        metadata={
            "name": "unitList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )


class GetUnitListRequest(BaseModel, ApplicationRequest):
    """
    Запрос списка единиц измерения.

    Attributes:
        list_options: Параметры запрашиваемого списка.
    """

    class Meta:
        name = "getUnitListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )


class GetUnitListResponse(BaseModel, ApplicationResponse):
    """
    Ответ на запрос сипка единиц измерения.

    Attributes:
        unit_list: Список едениц измерений.
    """

    class Meta:
        name = "getUnitListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/registry/ws-definitions/v2"

    model_config = ConfigDict(defer_build=True)
    unit_list: UnitList = field(
        metadata={
            "name": "unitList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/dictionary/v2",
            "required": True,
        }
    )
