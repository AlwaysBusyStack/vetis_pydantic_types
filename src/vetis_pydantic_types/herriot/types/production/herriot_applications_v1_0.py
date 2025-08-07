from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict

from vetis_pydantic_types.base import ApplicationRequest, ApplicationResponse
from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.herriot.types.production.application_v2_1 import (
    ApplicationDataInternalType,
    ApplicationResultDataInternalType,
)
from vetis_pydantic_types.herriot.types.production.base_v2_1 import (
    ListOptions,
    UpdateDateInterval,
)
from vetis_pydantic_types.herriot.types.production.dictionary_v2_5 import (
    Animal,
    AnimalGroup,
    AnimalId,
    AnimalSpeciesInternalType,
    AnimalSpeciesListInternalType,
    Location,
    RegionInternalType,
    SupervisedObjectInternalType,
    SupervisedObjectListInternalType,
    UnifiedAnimalIdlist,
)
from vetis_pydantic_types.herriot.types.production.document_v2_5 import (
    AnimalIdentityList,
    AnimalIdentityStatusChange,
    AnimalIdentityType,
    AnimalLifecycleEvent,
    AnimalMarkingEvent,
    AnimalMedicationEvent,
    AnimalMedicationEventList,
    AnimalMovementEvent,
    AnimalRegistration,
    AnimalRegistrationList,
    AnimalRegistrationStatusChange,
    AnimalRegistrationStatusList,
    IssueDateInterval,
    ObservableAnimalGroup,
    UserInternalType,
    VeterinaryEventStatusChangeReason,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"


class ConfirmAnimalVeterinaryEventResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Подтверждение сведений о ветеринарном профилактическом мероприятии.

    Attributes:
        medication_event: Обновленная редакция сведений о
            зарегистрированном ветеринарном профилактическом мероприятии
        target_namespace_element:
    """

    class Meta:
        name = "ConfirmAnimalVeterinaryEventResponse"

    model_config = ConfigDict(defer_build=True)
    medication_event: list[AnimalMedicationEvent] = field(
        default_factory=list,
        metadata={
            "name": "medicationEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ExcludeFromAnimalGroupResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Исключение животных из группы.

    Attributes:
        animal_registration: Зарегистрированная учётная карточка группы
            животного
        target_namespace_element:
    """

    class Meta:
        name = "ExcludeFromAnimalGroupResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration: Optional[AnimalRegistration] = field(
        default=None,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalRegistrationByGuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Получение основных актуальных сведений о регистрации животного или
    группы животных по глобальному идентификатору.

    Attributes:
        animal_registration: Актуальная редакция (версия)
            регистрационной карточки животного или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalRegistrationByGuidResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration: Optional[AnimalRegistration] = field(
        default=None,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalRegistrationByUuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Получение редакции (версии) основных сведений о регистрации животного
    или группы животных по идентификатору конкретной версии.

    Attributes:
        animal_registration: Версия регистрационной карточки животного
            или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalRegistrationByUuidResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration: Optional[AnimalRegistration] = field(
        default=None,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalRegistrationChangesListResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Получение списка изменений по основным сведениям о регистрации животного
    или группы животных за указанный период времени.

    Attributes:
        animal_registration_list: Список созданных за указанный период
            времени версий регистрационных карточек животных или групп
            животных
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalRegistrationChangesListResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration_list: AnimalRegistrationList = field(
        metadata={
            "name": "animalRegistrationList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalRegistrationHistoryResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Получение всей истории изменения сведений о регистрации животного или
    группы животных по глобальному идентификатору.

    Attributes:
        animal_registration_list: Список версий регистрационной карточки
            животного или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalRegistrationHistoryResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration_list: AnimalRegistrationList = field(
        metadata={
            "name": "animalRegistrationList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalRegistrationListResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Получение списка основных актуальных сведений о регистрации животного
    или группы животных с заданными параметрами фильтрации.

    Attributes:
        animal_registration_list: Список регистрационных карточек
            животных или групп животных
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalRegistrationListResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration_list: AnimalRegistrationList = field(
        metadata={
            "name": "animalRegistrationList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalVeterinaryEventByGuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Получение актуальных сведений о зарегистрированном ветеринарном
    профилактическом мероприятии по глобальному идентификатору.

    Attributes:
        medication_event: Актуальная редакция зарегистрированных
            сведений о ветеринарном профилактическом мероприятии
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalVeterinaryEventByGuidResponse"

    model_config = ConfigDict(defer_build=True)
    medication_event: Optional[AnimalMedicationEvent] = field(
        default=None,
        metadata={
            "name": "medicationEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalVeterinaryEventByUuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Получение редакции (версии) сведений о зарегистрированном ветеринарном
    профилактическом мероприятии по идентификатору версии.

    Attributes:
        medication_event: Сведения о версии сведений о ветеринарном
            профилактическом мероприятии
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalVeterinaryEventByUuidResponse"

    model_config = ConfigDict(defer_build=True)
    medication_event: Optional[AnimalMedicationEvent] = field(
        default=None,
        metadata={
            "name": "medicationEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalVeterinaryEventChangesListResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Получение списка изменений сведений о зарегистрированных ветеринарных
    профилактических мероприятий за указанный период времени.

    Attributes:
        medication_event_list: Список созданных за указанный период
            времени версий сведений о ветеринарных профилактических
            мероприятиях животных или групп животных
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalVeterinaryEventChangesListResponse"

    model_config = ConfigDict(defer_build=True)
    medication_event_list: AnimalMedicationEventList = field(
        metadata={
            "name": "medicationEventList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalVeterinaryEventHistoryResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Получение всей истории изменений сведений о зарегистрированном
    ветеринарном профилактическом мероприятии по глобальному идентификатору.

    Attributes:
        medication_event_list: Список версий сведений о ветеринарном
            профилактическом мероприятии
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalVeterinaryEventHistoryResponse"

    model_config = ConfigDict(defer_build=True)
    medication_event_list: AnimalMedicationEventList = field(
        metadata={
            "name": "medicationEventList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetFullAnimalRegistrationByGuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Получение полных актуальных сведений (включая ветпрофмероприятия) о
    регистрации животного или группы животных по глобальному идентификатору.

    Attributes:
        animal_registration: Актуальная редакция (версия)
            регистрационной карточки животного или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "GetFullAnimalRegistrationByGuidResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration: Optional[AnimalRegistration] = field(
        default=None,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetFullAnimalRegistrationByUuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Получение редакции (версии) полных сведений (включая ветпрофмероприятия)
    о регистрации животного или группы животных по идентификатору конкретной
    версии.

    Attributes:
        animal_registration: Версия регистрационной карточки животного
            или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "GetFullAnimalRegistrationByUuidResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration: Optional[AnimalRegistration] = field(
        default=None,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class HerriotApplicationRequest(ApplicationDataInternalType):
    model_config = ConfigDict(defer_build=True)
    local_transaction_id: str = field(
        metadata={
            "name": "localTransactionId",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )
    initiator: UserInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "sessionToken",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )


class IncludeToAnimalGroupResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Пополнение группы животных.

    Attributes:
        animal_registration: Зарегистрированная учётная карточка группы
            животного
        target_namespace_element:
    """

    class Meta:
        name = "IncludeToAnimalGroupResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration: Optional[AnimalRegistration] = field(
        default=None,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ModifyAnimalRegistrationResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Внесение изменений в основные сведения о зарегистрированном животном или
    группе животных.

    Attributes:
        animal_registration: Обновленная учётная карточка животного или
            группы животных
        target_namespace_element:
    """

    class Meta:
        name = "ModifyAnimalRegistrationResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ModifyAnimalVeterinaryEventResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Редактирование сведений о ветеринарном профилактическом мероприятии.

    Attributes:
        medication_event: Обновленная редакция сведений о
            зарегистрированном ветеринарном профилактическом мероприятии
        target_namespace_element:
    """

    class Meta:
        name = "ModifyAnimalVeterinaryEventResponse"

    model_config = ConfigDict(defer_build=True)
    medication_event: list[AnimalMedicationEvent] = field(
        default_factory=list,
        metadata={
            "name": "medicationEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class RegisterAnimalIdentityResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Регистрация сведений об идентификации (маркирование) зарегистрированного
    животного или группы животных.

    Attributes:
        animal_registration_list: Список регистрационных карточек
            животных или групп животных с обновленными сведениями об
            идентификации (маркировании)
        target_namespace_element:
    """

    class Meta:
        name = "RegisterAnimalIdentityResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration_list: Optional[AnimalRegistrationList] = field(
        default=None,
        metadata={
            "name": "animalRegistrationList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class RegisterAnimalMovementEventResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Регистрация сведений о перемещении / смене собственника
    зарегистрированного животного или групп животных.

    Attributes:
        movement_animal_registration_list: Список учётных карточек
            перемещаемых животных или групп животных
        referenced_animal_registration_list: Список связанных карточек
            животных, которые в явном виде не участвовали в запросе, но
            были изменены в результате выполнения операции (например,
            перемещение индивидуального животного, входящего в группу,
            влечёт изменение данной группы).
        target_namespace_element:
    """

    class Meta:
        name = "RegisterAnimalMovementEventResponse"

    model_config = ConfigDict(defer_build=True)
    movement_animal_registration_list: Optional[AnimalRegistrationList] = (
        field(
            default=None,
            metadata={
                "name": "movementAnimalRegistrationList",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            },
        )
    )
    referenced_animal_registration_list: Optional[AnimalRegistrationList] = (
        field(
            default=None,
            metadata={
                "name": "referencedAnimalRegistrationList",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            },
        )
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class RegisterAnimalResponseInternalType(ApplicationResultDataInternalType):
    """
    Ответ: Регистрация животного или группы животных.

    Attributes:
        animal_registration: Зарегистрированная учётная карточка
            животного или группы животного
        target_namespace_element:
    """

    class Meta:
        name = "RegisterAnimalResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class RegisterAnimalVeterinaryEventResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Регистрация ветеринарного профилактического мероприятия.

    Attributes:
        medication_event: Зарегистрированные сведения о ветеринарном
            профилактическом мероприятии
        target_namespace_element:
    """

    class Meta:
        name = "RegisterAnimalVeterinaryEventResponse"

    model_config = ConfigDict(defer_build=True)
    medication_event: list[AnimalMedicationEvent] = field(
        default_factory=list,
        metadata={
            "name": "medicationEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class RemoveAnimalIdentityResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Прекращение регистрации сведений об идентификации (снятие средства
    маркирования) зарегистрированного животного или группы животных.

    Attributes:
        animal_registration_list: Список регистрационных карточек
            животных или групп животных с обновленными сведениями об
            идентификации (маркировании)
        target_namespace_element:
    """

    class Meta:
        name = "RemoveAnimalIdentityResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration_list: Optional[AnimalRegistrationList] = field(
        default=None,
        metadata={
            "name": "animalRegistrationList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ReplaceAnimalIdentityNotificationResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Заявка о необходимости перерегистрации сведений об идентификации (замене
    средства маркирования) зарегистрированного животного или группы животных.

    Attributes:
        animal_registration_list: Список регистрационных карточек
            животных или групп животных с обновленными сведениями об
            идентификации (маркировании)
        target_namespace_element:
    """

    class Meta:
        name = "ReplaceAnimalIdentityNotificationResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration_list: Optional[AnimalRegistrationList] = field(
        default=None,
        metadata={
            "name": "animalRegistrationList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ReplaceAnimalIdentityResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Перерегистрация сведений об идентификации (замена средства маркирования)
    зарегистрированного животного или группы животных.

    Attributes:
        animal_registration_list: Список регистрационных карточек
            животных или групп животных с обновленными сведениями об
            идентификации (маркировании)
        target_namespace_element:
    """

    class Meta:
        name = "ReplaceAnimalIdentityResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration_list: Optional[AnimalRegistrationList] = field(
        default=None,
        metadata={
            "name": "animalRegistrationList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class TerminateAnimalRegistrationResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Прекращение регистрации (выбытие) животного или группы животных.

    Attributes:
        terminated_animal_registration_list: Список учётных карточек
            выбывших животных или групп животных
        referenced_animal_registration_list: Список связанных карточек
            животных, которые в явном виде не участвовали в запросе, но
            были изменены в результате выполнения операции (например,
            обновление группы животных, в которой содержалось выбывшее
            индивидуальное животное из запроса).
        target_namespace_element:
    """

    class Meta:
        name = "TerminateAnimalRegistrationResponse"

    model_config = ConfigDict(defer_build=True)
    terminated_animal_registration_list: Optional[AnimalRegistrationList] = (
        field(
            default=None,
            metadata={
                "name": "terminatedAnimalRegistrationList",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            },
        )
    )
    referenced_animal_registration_list: Optional[AnimalRegistrationList] = (
        field(
            default=None,
            metadata={
                "name": "referencedAnimalRegistrationList",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            },
        )
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class VerifyAnimalIdresponseInternalType(ApplicationResultDataInternalType):
    """
    Ответ: Проверка статусов УНСМ (уникальных номеров средств маркирования)

    Attributes:
        animal_idlist: Результат проверки указанных в запросе номеров
            средств маркирования
        referenced_animal_registration_list: Список связанных учётных
            карточек животных
        target_namespace_element:
    """

    class Meta:
        name = "VerifyAnimalIDResponse"

    model_config = ConfigDict(defer_build=True)
    animal_idlist: UnifiedAnimalIdlist = field(
        metadata={
            "name": "animalIDList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    referenced_animal_registration_list: Optional[AnimalRegistrationList] = (
        field(
            default=None,
            metadata={
                "name": "referencedAnimalRegistrationList",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            },
        )
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class WithdrawAnimalIdentityResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Аннулирование сведений об идентификации (удаление средства маркирования)
    зарегистрированного животного или группы животных.

    Attributes:
        animal_registration_list: Список регистрационных карточек
            животных или групп животных с обновленными сведениями об
            идентификации (маркировании)
        target_namespace_element:
    """

    class Meta:
        name = "WithdrawAnimalIdentityResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration_list: Optional[AnimalRegistrationList] = field(
        default=None,
        metadata={
            "name": "animalRegistrationList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class WithdrawAnimalRegistrationResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Аннулирование сведений о регистрации животного или группы животных.

    Attributes:
        animal_registration: Обновленная учётная карточка животного или
            группы животных
        target_namespace_element:
    """

    class Meta:
        name = "WithdrawAnimalRegistrationResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class WithdrawAnimalVeterinaryEventResponseInternalType(
    ApplicationResultDataInternalType
):
    """
    Ответ: Аннулирование сведений о ветеринарном профилактическом мероприятии.

    Attributes:
        medication_event: Обновленная редакция сведений о
            зарегистрированном ветеринарном профилактическом мероприятии
            в статусе WITHDRAWN
        target_namespace_element:
    """

    class Meta:
        name = "WithdrawAnimalVeterinaryEventResponse"

    model_config = ConfigDict(defer_build=True)
    medication_event: list[AnimalMedicationEvent] = field(
        default_factory=list,
        metadata={
            "name": "medicationEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ConfirmAnimalVeterinaryEventRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Подтверждение сведений о ветеринарном профилактическом мероприятии.

    Attributes:
        medication_event: Глобальный идентификатор зарегистрированных
            сведений о ветеринарном профилактическом мероприятии
        target_namespace_element:
    """

    class Meta:
        name = "ConfirmAnimalVeterinaryEventRequest"

    model_config = ConfigDict(defer_build=True)
    medication_event: list[AnimalMedicationEvent] = field(
        default_factory=list,
        metadata={
            "name": "medicationEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ExcludeFromAnimalGroupRequestInternalType(HerriotApplicationRequest):
    """
    Запрос: Исключение животных из группы.

    Attributes:
        specified_animal_group: Сведения об исключении животных из
            группы
        excluded_animal_registration_list: Список учётных карточек
            животных индивидуальной идентификации, которые необходимо
            исключить из группы
        animal_registration_ref: Учётная карточка группы животных, для
            которой выполняется исключение
        target_namespace_element:
    """

    class Meta:
        name = "ExcludeFromAnimalGroupRequest"

    model_config = ConfigDict(defer_build=True)
    specified_animal_group: AnimalGroup = field(
        metadata={
            "name": "specifiedAnimalGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    excluded_animal_registration_list: Optional[AnimalRegistrationList] = (
        field(
            default=None,
            metadata={
                "name": "excludedAnimalRegistrationList",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            },
        )
    )
    animal_registration_ref: AnimalRegistration = field(
        metadata={
            "name": "animalRegistrationRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalRegistrationByGuidRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Получение основных актуальных сведений о регистрации животного или
    группы животных по глобальному идентификатору.

    Attributes:
        animal_registration_guid: Глобальный идентификатор
            регистрационной карточки животного или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalRegistrationByGuidRequest"

    model_config = ConfigDict(defer_build=True)
    animal_registration_guid: str = field(
        metadata={
            "name": "animalRegistrationGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalRegistrationByUuidRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Получение редакции (версии) основных сведений о регистрации животного
    или группы животных по идентификатору конкретной версии.

    Attributes:
        animal_registration_uuid: Уникальный идентификатор версии
            регистрационной карточки животного или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalRegistrationByUuidRequest"

    model_config = ConfigDict(defer_build=True)
    animal_registration_uuid: str = field(
        metadata={
            "name": "animalRegistrationUuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalRegistrationChangesListRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Получение списка изменений по основным сведениям о регистрации
    животного или группы животных за указанный период времени.

    Attributes:
        list_options: Параметры запрашиваемого списка
        update_date_interval: Интервал времени обновления
        region: Зона обслуживания: субъект РФ, на территории которого
            содержатся животные
        location: Зона обслуживания: место содержания животных
        operator: Поднадзорный объект, на котором осуществляется
            содержание животных
        animal_species: Биологический вид животного
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalRegistrationChangesListRequest"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    update_date_interval: Optional[UpdateDateInterval] = field(
        default=None,
        metadata={
            "name": "updateDateInterval",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    region: RegionInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    location: list[Location] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    operator: list[SupervisedObjectInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    animal_species: list[AnimalSpeciesInternalType] = field(
        default_factory=list,
        metadata={
            "name": "animalSpecies",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalRegistrationHistoryRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Получение всей истории изменения сведений о регистрации животного или
    группы животных по глобальному идентификатору.

    Attributes:
        animal_registration_guid: Глобальный идентификатор
            регистрационной карточки животного или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalRegistrationHistoryRequest"

    model_config = ConfigDict(defer_build=True)
    animal_registration_guid: str = field(
        metadata={
            "name": "animalRegistrationGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalRegistrationListRequestInternalType(HerriotApplicationRequest):
    """
    Запрос: Получение списка основных актуальных сведений о регистрации животного
    или группы животных с заданными параметрами фильтрации.

    Attributes:
        list_options: Параметры запрашиваемого списка
        issue_date_interval: Период дат оформления документов
        region: Зона обслуживания: субъект РФ, на территории которого
            содержатся животные
        supervised_object_list: Список поднадзорных объектов, на которых
            содержатся животные
        animal_identity_type: Тип идентификации/учёта:
            индивидуальная/групповая
        registration_number: Регистрационный номер учётной карточки
            животного / группы животных
        animal_idlist: Сведения о номерах средств маркирования
        registration_status_list: Статус учётной карточки животного
            (группы животных)
        animal_species_list: Биологический вид животного
        specified_animal: Сведения о животном (в случае индивидуальной
            идентификации)
        specified_animal_identity_list: Сведения об идентификации
            животного
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalRegistrationListRequest"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
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
    region: RegionInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    supervised_object_list: Optional[SupervisedObjectListInternalType] = field(
        default=None,
        metadata={
            "name": "supervisedObjectList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    animal_identity_type: Optional[AnimalIdentityType] = field(
        default=None,
        metadata={
            "name": "animalIdentityType",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    registration_number: Optional[AnimalId] = field(
        default=None,
        metadata={
            "name": "registrationNumber",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    animal_idlist: Optional[UnifiedAnimalIdlist] = field(
        default=None,
        metadata={
            "name": "animalIDList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    registration_status_list: Optional[AnimalRegistrationStatusList] = field(
        default=None,
        metadata={
            "name": "registrationStatusList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    animal_species_list: Optional[AnimalSpeciesListInternalType] = field(
        default=None,
        metadata={
            "name": "animalSpeciesList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    specified_animal: Optional[Animal] = field(
        default=None,
        metadata={
            "name": "specifiedAnimal",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    specified_animal_identity_list: Optional[AnimalIdentityList] = field(
        default=None,
        metadata={
            "name": "specifiedAnimalIdentityList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalVeterinaryEventByGuidRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Получение актуальных сведений о зарегистрированном ветеринарном
    профилактическом мероприятии по глобальному идентификатору.

    Attributes:
        medication_event_guid: Глобальный идентификатор
            зарегистрированных сведений о ветеринарном профилактическом
            мероприятии
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalVeterinaryEventByGuidRequest"

    model_config = ConfigDict(defer_build=True)
    medication_event_guid: str = field(
        metadata={
            "name": "medicationEventGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalVeterinaryEventByUuidRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Получение редакции (версии) сведений о зарегистрированном ветеринарном
    профилактическом мероприятии по идентификатору версии.

    Attributes:
        medication_event_uuid: Уникальный идентификатор версии сведений
            о ветеринарном профилактическом мероприятии
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalVeterinaryEventByUuidRequest"

    model_config = ConfigDict(defer_build=True)
    medication_event_uuid: str = field(
        metadata={
            "name": "medicationEventUuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalVeterinaryEventChangesListRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Получение списка изменений сведений о зарегистрированных ветеринарных
    профилактических мероприятий за указанный период времени.

    Attributes:
        list_options: Параметры запрашиваемого списка
        update_date_interval: Интервал времени обновления
        region: Зона обслуживания: субъект РФ, на территории которого
            содержатся животные
        location: Зона обслуживания: место содержания животных
        operator: Поднадзорный объект, на котором осуществляется
            содержание животных
        animal_registration_guid: Глобальный идентификатор учетной
            карточки животного или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalVeterinaryEventChangesListRequest"

    model_config = ConfigDict(defer_build=True)
    list_options: Optional[ListOptions] = field(
        default=None,
        metadata={
            "name": "listOptions",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    update_date_interval: Optional[UpdateDateInterval] = field(
        default=None,
        metadata={
            "name": "updateDateInterval",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/base",
        },
    )
    region: RegionInternalType = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    location: list[Location] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    operator: list[SupervisedObjectInternalType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    animal_registration_guid: list[str] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistrationGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetAnimalVeterinaryEventHistoryRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Получение всей истории изменений сведений о зарегистрированном
    ветеринарном профилактическом мероприятии по глобальному идентификатору.

    Attributes:
        medication_event_guid: Глобальный идентификатор
            зарегистрированных сведений о ветеринарном профилактическом
            мероприятии
        target_namespace_element:
    """

    class Meta:
        name = "GetAnimalVeterinaryEventHistoryRequest"

    model_config = ConfigDict(defer_build=True)
    medication_event_guid: str = field(
        metadata={
            "name": "medicationEventGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetFullAnimalRegistrationByGuidRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Получение полных актуальных сведений (включая ветпрофмероприятия) о
    регистрации животного или группы животных по глобальному идентификатору.

    Attributes:
        animal_registration_guid: Глобальный идентификатор
            регистрационной карточки животного или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "GetFullAnimalRegistrationByGuidRequest"

    model_config = ConfigDict(defer_build=True)
    animal_registration_guid: str = field(
        metadata={
            "name": "animalRegistrationGuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class GetFullAnimalRegistrationByUuidRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Получение редакции (версии) полных сведений (включая
    ветпрофмероприятия) о регистрации животного или группы животных по
    идентификатору конкретной версии.

    Attributes:
        animal_registration_uuid: Уникальный идентификатор версии
            регистрационной карточки животного или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "GetFullAnimalRegistrationByUuidRequest"

    model_config = ConfigDict(defer_build=True)
    animal_registration_uuid: str = field(
        metadata={
            "name": "animalRegistrationUuid",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class IncludeToAnimalGroupRequestInternalType(HerriotApplicationRequest):
    """
    Запрос: Пополнение группы животных.

    Attributes:
        specified_animal_group: Сведения о пополнении группы животных
        included_animal_registration_list: Список учётных карточек
            животных индивидуальной идентификации, которые необходимо
            включить в группу
        animal_registration_ref: Учётная карточка группы животных, для
            которой выполняется пополнение
        target_namespace_element:
    """

    class Meta:
        name = "IncludeToAnimalGroupRequest"

    model_config = ConfigDict(defer_build=True)
    specified_animal_group: AnimalGroup = field(
        metadata={
            "name": "specifiedAnimalGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    included_animal_registration_list: Optional[AnimalRegistrationList] = (
        field(
            default=None,
            metadata={
                "name": "includedAnimalRegistrationList",
                "type": "Element",
                "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            },
        )
    )
    animal_registration_ref: AnimalRegistration = field(
        metadata={
            "name": "animalRegistrationRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ModifyAnimalRegistrationRequestInternalType(HerriotApplicationRequest):
    """
    Запрос: Внесение изменений в основные сведения о зарегистрированном животном
    или группе животных.

    Attributes:
        animal_registration: Проект изменений существующей учётной
            карточки с указанным уникальным идентификатором версии
        target_namespace_element:
    """

    class Meta:
        name = "ModifyAnimalRegistrationRequest"

    model_config = ConfigDict(defer_build=True)
    animal_registration: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ModifyAnimalVeterinaryEventRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Редактирование сведений о ветеринарном профилактическом мероприятии.

    Attributes:
        medication_event: Проект обновленных сведений о
            зарегистрированном ветеринарном профилактическом мероприятии
            с указанным глобальным идентификатором
        target_namespace_element:
    """

    class Meta:
        name = "ModifyAnimalVeterinaryEventRequest"

    model_config = ConfigDict(defer_build=True)
    medication_event: list[AnimalMedicationEvent] = field(
        default_factory=list,
        metadata={
            "name": "medicationEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class RegisterAnimalIdentityRequestInternalType(HerriotApplicationRequest):
    """
    Запрос: Регистрация сведений об идентификации (маркирование)
    зарегистрированного животного или группы животных.

    Attributes:
        animal_marking_event: Проект сведений об идентификации,
            содержащий глобальный идентификатор зарегистрированного
            животного или группы животных
        target_namespace_element:
    """

    class Meta:
        name = "RegisterAnimalIdentityRequest"

    model_config = ConfigDict(defer_build=True)
    animal_marking_event: list[AnimalMarkingEvent] = field(
        default_factory=list,
        metadata={
            "name": "animalMarkingEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class RegisterAnimalMovementEventRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Регистрация сведений о перемещении / смене собственника
    зарегистрированного животного или групп животных.

    Attributes:
        referenced_movement_event: Сведения о перемещении
        movement_animal_registration_list: Cведения о перемещаемых
            зарегистрированных животных или групп животных
        target_namespace_element:
    """

    class Meta:
        name = "RegisterAnimalMovementEventRequest"

    model_config = ConfigDict(defer_build=True)
    referenced_movement_event: AnimalMovementEvent = field(
        metadata={
            "name": "referencedMovementEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    movement_animal_registration_list: AnimalRegistrationList = field(
        metadata={
            "name": "movementAnimalRegistrationList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class RegisterAnimalRequestInternalType(HerriotApplicationRequest):
    """
    Запрос: Регистрация животного или группы животных.

    Attributes:
        animal_registration: Проект учётной карточки животного или
            группы животных
        target_namespace_element:
    """

    class Meta:
        name = "RegisterAnimalRequest"

    model_config = ConfigDict(defer_build=True)
    animal_registration: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class RegisterAnimalVeterinaryEventRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Регистрация ветеринарного профилактического мероприятия.

    Attributes:
        referenced_medication_event: Проект сведений о ветеринарном
            профилактическом мероприятии
        specified_animal_group: Список зарегистрированных животных или
            групп животных, в отношении которых осуществлялось данное
            мероприятие
        target_namespace_element:
    """

    class Meta:
        name = "RegisterAnimalVeterinaryEventRequest"

    model_config = ConfigDict(defer_build=True)
    referenced_medication_event: list[AnimalMedicationEvent] = field(
        default_factory=list,
        metadata={
            "name": "referencedMedicationEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    specified_animal_group: list[ObservableAnimalGroup] = field(
        default_factory=list,
        metadata={
            "name": "specifiedAnimalGroup",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class RemoveAnimalIdentityRequestInternalType(HerriotApplicationRequest):
    """
    Запрос: Прекращение регистрации сведений об идентификации (снятие средства
    маркирования) зарегистрированного животного или группы животных.

    Attributes:
        referenced_marking_event: Сведения о выбытии зарегистрированного
            средства идентификации (маркирования)
        animal_registration_ref: Регистрационная карточка животных или
            групп животных
        target_namespace_element:
    """

    class Meta:
        name = "RemoveAnimalIdentityRequest"

    model_config = ConfigDict(defer_build=True)
    referenced_marking_event: AnimalMarkingEvent = field(
        metadata={
            "name": "referencedMarkingEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    animal_registration_ref: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistrationRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ReplaceAnimalIdentityNotificationRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Заявка о необходимости перерегистрации сведений об идентификации
    (замене средства маркирования) зарегистрированного животного или группы
    животных.

    Attributes:
        referenced_marking_event: Сведения о причинах замены средства
            идентификации (маркирования)
        animal_registration_ref: Регистрационная карточка животных или
            групп животных
        target_namespace_element:
    """

    class Meta:
        name = "ReplaceAnimalIdentityNotificationRequest"

    model_config = ConfigDict(defer_build=True)
    referenced_marking_event: AnimalMarkingEvent = field(
        metadata={
            "name": "referencedMarkingEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    animal_registration_ref: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistrationRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ReplaceAnimalIdentityRequestInternalType(HerriotApplicationRequest):
    """
    Запрос: Перерегистрация сведений об идентификации (замена средства
    маркирования) зарегистрированного животного или группы животных.

    Attributes:
        referenced_marking_event: Сведения о новом средстве
            идентификации (маркирования) животного
        animal_registration_ref: Регистрационная карточка животных или
            групп животных
        target_namespace_element:
    """

    class Meta:
        name = "ReplaceAnimalIdentityRequest"

    model_config = ConfigDict(defer_build=True)
    referenced_marking_event: AnimalMarkingEvent = field(
        metadata={
            "name": "referencedMarkingEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    animal_registration_ref: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistrationRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class TerminateAnimalRegistrationRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Прекращение регистрации (выбытие) животного или группы животных.

    Attributes:
        referenced_lifecycle_event: Сведения о выбытии животного или
            группы животных
        animal_registration_ref: Учётная карточка животного или группы
            животных, в отношении которой регистрируется выбытие
        target_namespace_element:
    """

    class Meta:
        name = "TerminateAnimalRegistrationRequest"

    model_config = ConfigDict(defer_build=True)
    referenced_lifecycle_event: AnimalLifecycleEvent = field(
        metadata={
            "name": "referencedLifecycleEvent",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    animal_registration_ref: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistrationRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class VerifyAnimalIdrequestInternalType(HerriotApplicationRequest):
    """
    Запрос: Проверка статусов УНСМ (уникальных номеров средств маркирования)

    Attributes:
        animal_idlist: Список номеров средств маркирования для проверки
        target_namespace_element:
    """

    class Meta:
        name = "VerifyAnimalIDRequest"

    model_config = ConfigDict(defer_build=True)
    animal_idlist: UnifiedAnimalIdlist = field(
        metadata={
            "name": "animalIDList",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class WithdrawAnimalIdentityRequestInternalType(HerriotApplicationRequest):
    """
    Запрос: Аннулирование сведений об идентификации (удаление средства
    маркирования) зарегистрированного животного или группы животных.

    Attributes:
        withdraw_details: Сведения об аннулировании
        animal_registration_ref: Регистрационная карточка животных или
            групп животных
        target_namespace_element:
    """

    class Meta:
        name = "WithdrawAnimalIdentityRequest"

    model_config = ConfigDict(defer_build=True)
    withdraw_details: AnimalIdentityStatusChange = field(
        metadata={
            "name": "withdrawDetails",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    animal_registration_ref: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistrationRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class WithdrawAnimalRegistrationRequestInternalType(HerriotApplicationRequest):
    """
    Запрос: Аннулирование сведений о регистрации животного или группы животных.

    Attributes:
        withdraw_details: Сведения об аннулировании учётной карточки
            животного
        animal_registration_ref: Учётная карточка животного или группы
            животных, в отношении которой регистрируется аннулирование
        target_namespace_element:
    """

    class Meta:
        name = "WithdrawAnimalRegistrationRequest"

    model_config = ConfigDict(defer_build=True)
    withdraw_details: AnimalRegistrationStatusChange = field(
        metadata={
            "name": "withdrawDetails",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    animal_registration_ref: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistrationRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class WithdrawAnimalVeterinaryEventRequestInternalType(
    HerriotApplicationRequest
):
    """
    Запрос: Аннулирование сведений о ветеринарном профилактическом мероприятии.

    Attributes:
        reason: Сведения об аннулировании
        medication_event_ref: Глобальный идентификатор аннулируемых
            сведений о ветеринарном профилактическом мероприятии
        target_namespace_element:
    """

    class Meta:
        name = "WithdrawAnimalVeterinaryEventRequest"

    model_config = ConfigDict(defer_build=True)
    reason: VeterinaryEventStatusChangeReason = field(
        metadata={
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )
    medication_event_ref: list[AnimalMedicationEvent] = field(
        default_factory=list,
        metadata={
            "name": "medicationEventRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )
    target_namespace_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )


class ConfirmAnimalVeterinaryEventResponse(
    ApplicationResponse, ConfirmAnimalVeterinaryEventResponseInternalType
):
    class Meta:
        name = "confirmAnimalVeterinaryEventResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class ExcludeFromAnimalGroupResponse(
    ApplicationResponse, ExcludeFromAnimalGroupResponseInternalType
):
    class Meta:
        name = "excludeFromAnimalGroupResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalRegistrationByGuidResponse(
    ApplicationResponse, GetAnimalRegistrationByGuidResponseInternalType
):
    class Meta:
        name = "getAnimalRegistrationByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalRegistrationByUuidResponse(
    ApplicationResponse, GetAnimalRegistrationByUuidResponseInternalType
):
    class Meta:
        name = "getAnimalRegistrationByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalRegistrationChangesListResponse(
    ApplicationResponse, GetAnimalRegistrationChangesListResponseInternalType
):
    class Meta:
        name = "getAnimalRegistrationChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalRegistrationHistoryResponse(
    ApplicationResponse, GetAnimalRegistrationHistoryResponseInternalType
):
    class Meta:
        name = "getAnimalRegistrationHistoryResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalRegistrationListResponse(
    ApplicationResponse, GetAnimalRegistrationListResponseInternalType
):
    class Meta:
        name = "getAnimalRegistrationListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalVeterinaryEventByGuidResponse(
    ApplicationResponse, GetAnimalVeterinaryEventByGuidResponseInternalType
):
    class Meta:
        name = "getAnimalVeterinaryEventByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalVeterinaryEventByUuidResponse(
    ApplicationResponse, GetAnimalVeterinaryEventByUuidResponseInternalType
):
    class Meta:
        name = "getAnimalVeterinaryEventByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalVeterinaryEventChangesListResponse(
    ApplicationResponse,
    GetAnimalVeterinaryEventChangesListResponseInternalType,
):
    class Meta:
        name = "getAnimalVeterinaryEventChangesListResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalVeterinaryEventHistoryResponse(
    ApplicationResponse, GetAnimalVeterinaryEventHistoryResponseInternalType
):
    class Meta:
        name = "getAnimalVeterinaryEventHistoryResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetFullAnimalRegistrationByGuidResponse(
    ApplicationResponse, GetFullAnimalRegistrationByGuidResponseInternalType
):
    class Meta:
        name = "getFullAnimalRegistrationByGuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetFullAnimalRegistrationByUuidResponse(
    ApplicationResponse, GetFullAnimalRegistrationByUuidResponseInternalType
):
    class Meta:
        name = "getFullAnimalRegistrationByUuidResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class IncludeToAnimalGroupResponse(
    ApplicationResponse, IncludeToAnimalGroupResponseInternalType
):
    class Meta:
        name = "includeToAnimalGroupResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class ModifyAnimalRegistrationResponse(
    ApplicationResponse, ModifyAnimalRegistrationResponseInternalType
):
    class Meta:
        name = "modifyAnimalRegistrationResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class ModifyAnimalVeterinaryEventResponse(
    ApplicationResponse, ModifyAnimalVeterinaryEventResponseInternalType
):
    class Meta:
        name = "modifyAnimalVeterinaryEventResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class RegisterAnimalIdentityResponse(
    ApplicationResponse, RegisterAnimalIdentityResponseInternalType
):
    class Meta:
        name = "registerAnimalIdentityResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class RegisterAnimalMovementEventResponse(
    ApplicationResponse, RegisterAnimalMovementEventResponseInternalType
):
    class Meta:
        name = "registerAnimalMovementEventResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class RegisterAnimalResponse(
    ApplicationResponse, RegisterAnimalResponseInternalType
):
    class Meta:
        name = "registerAnimalResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class RegisterAnimalVeterinaryEventResponse(
    ApplicationResponse, RegisterAnimalVeterinaryEventResponseInternalType
):
    class Meta:
        name = "registerAnimalVeterinaryEventResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class RemoveAnimalIdentityResponse(
    ApplicationResponse, RemoveAnimalIdentityResponseInternalType
):
    class Meta:
        name = "removeAnimalIdentityResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class ReplaceAnimalIdentityNotificationResponse(
    ApplicationResponse, ReplaceAnimalIdentityNotificationResponseInternalType
):
    class Meta:
        name = "replaceAnimalIdentityNotificationResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class ReplaceAnimalIdentityResponse(
    ApplicationResponse, ReplaceAnimalIdentityResponseInternalType
):
    class Meta:
        name = "replaceAnimalIdentityResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class TerminateAnimalRegistrationResponse(
    ApplicationResponse, TerminateAnimalRegistrationResponseInternalType
):
    class Meta:
        name = "terminateAnimalRegistrationResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class VerifyAnimalIdresponse(VerifyAnimalIdresponseInternalType):
    class Meta:
        name = "verifyAnimalIDResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class WithdrawAnimalIdentityResponse(
    ApplicationResponse, WithdrawAnimalIdentityResponseInternalType
):
    class Meta:
        name = "withdrawAnimalIdentityResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class WithdrawAnimalRegistrationResponse(
    ApplicationResponse, WithdrawAnimalRegistrationResponseInternalType
):
    class Meta:
        name = "withdrawAnimalRegistrationResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class WithdrawAnimalVeterinaryEventResponse(
    ApplicationResponse, WithdrawAnimalVeterinaryEventResponseInternalType
):
    class Meta:
        name = "withdrawAnimalVeterinaryEventResponse"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class ConfirmAnimalVeterinaryEventRequest(
    ApplicationRequest, ConfirmAnimalVeterinaryEventRequestInternalType
):
    class Meta:
        name = "confirmAnimalVeterinaryEventRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class ExcludeFromAnimalGroupRequest(
    ApplicationRequest, ExcludeFromAnimalGroupRequestInternalType
):
    class Meta:
        name = "excludeFromAnimalGroupRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalRegistrationByGuidRequest(
    ApplicationRequest, GetAnimalRegistrationByGuidRequestInternalType
):
    class Meta:
        name = "getAnimalRegistrationByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalRegistrationByUuidRequest(
    ApplicationRequest, GetAnimalRegistrationByUuidRequestInternalType
):
    class Meta:
        name = "getAnimalRegistrationByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalRegistrationChangesListRequest(
    ApplicationRequest, GetAnimalRegistrationChangesListRequestInternalType
):
    class Meta:
        name = "getAnimalRegistrationChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalRegistrationHistoryRequest(
    ApplicationRequest, GetAnimalRegistrationHistoryRequestInternalType
):
    class Meta:
        name = "getAnimalRegistrationHistoryRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalRegistrationListRequest(
    ApplicationRequest, GetAnimalRegistrationListRequestInternalType
):
    class Meta:
        name = "getAnimalRegistrationListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalVeterinaryEventByGuidRequest(
    ApplicationRequest, GetAnimalVeterinaryEventByGuidRequestInternalType
):
    class Meta:
        name = "getAnimalVeterinaryEventByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalVeterinaryEventByUuidRequest(
    ApplicationRequest, GetAnimalVeterinaryEventByUuidRequestInternalType
):
    class Meta:
        name = "getAnimalVeterinaryEventByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalVeterinaryEventChangesListRequest(
    ApplicationRequest, GetAnimalVeterinaryEventChangesListRequestInternalType
):
    class Meta:
        name = "getAnimalVeterinaryEventChangesListRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetAnimalVeterinaryEventHistoryRequest(
    ApplicationRequest, GetAnimalVeterinaryEventHistoryRequestInternalType
):
    class Meta:
        name = "getAnimalVeterinaryEventHistoryRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetFullAnimalRegistrationByGuidRequest(
    ApplicationRequest, GetFullAnimalRegistrationByGuidRequestInternalType
):
    class Meta:
        name = "getFullAnimalRegistrationByGuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class GetFullAnimalRegistrationByUuidRequest(
    ApplicationRequest, GetFullAnimalRegistrationByUuidRequestInternalType
):
    class Meta:
        name = "getFullAnimalRegistrationByUuidRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class IncludeToAnimalGroupRequest(
    ApplicationRequest, IncludeToAnimalGroupRequestInternalType
):
    class Meta:
        name = "includeToAnimalGroupRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class ModifyAnimalRegistrationRequest(
    ApplicationRequest, ModifyAnimalRegistrationRequestInternalType
):
    class Meta:
        name = "modifyAnimalRegistrationRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class ModifyAnimalVeterinaryEventRequest(
    ApplicationRequest, ModifyAnimalVeterinaryEventRequestInternalType
):
    class Meta:
        name = "modifyAnimalVeterinaryEventRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class RegisterAnimalIdentityRequest(
    ApplicationRequest, RegisterAnimalIdentityRequestInternalType
):
    class Meta:
        name = "registerAnimalIdentityRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class RegisterAnimalMovementEventRequest(
    ApplicationRequest, RegisterAnimalMovementEventRequestInternalType
):
    class Meta:
        name = "registerAnimalMovementEventRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class RegisterAnimalRequest(
    ApplicationRequest, RegisterAnimalRequestInternalType
):
    class Meta:
        name = "registerAnimalRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class RegisterAnimalVeterinaryEventRequest(
    ApplicationRequest, RegisterAnimalVeterinaryEventRequestInternalType
):
    class Meta:
        name = "registerAnimalVeterinaryEventRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class RemoveAnimalIdentityRequest(
    ApplicationRequest, RemoveAnimalIdentityRequestInternalType
):
    class Meta:
        name = "removeAnimalIdentityRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class ReplaceAnimalIdentityNotificationRequest(
    ApplicationRequest, ReplaceAnimalIdentityNotificationRequestInternalType
):
    class Meta:
        name = "replaceAnimalIdentityNotificationRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class ReplaceAnimalIdentityRequest(
    ApplicationRequest, ReplaceAnimalIdentityRequestInternalType
):
    class Meta:
        name = "replaceAnimalIdentityRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class TerminateAnimalRegistrationRequest(
    ApplicationRequest, TerminateAnimalRegistrationRequestInternalType
):
    class Meta:
        name = "terminateAnimalRegistrationRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class VerifyAnimalIdrequest(VerifyAnimalIdrequestInternalType):
    class Meta:
        name = "verifyAnimalIDRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class WithdrawAnimalIdentityRequest(
    ApplicationRequest, WithdrawAnimalIdentityRequestInternalType
):
    class Meta:
        name = "withdrawAnimalIdentityRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class WithdrawAnimalRegistrationRequest(
    ApplicationRequest, WithdrawAnimalRegistrationRequestInternalType
):
    class Meta:
        name = "withdrawAnimalRegistrationRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)


class WithdrawAnimalVeterinaryEventRequest(
    ApplicationRequest, WithdrawAnimalVeterinaryEventRequestInternalType
):
    class Meta:
        name = "withdrawAnimalVeterinaryEventRequest"
        namespace = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"

    model_config = ConfigDict(defer_build=True)
