from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict

from vetis_pydantic_types.base import ApplicationRequest, ApplicationResponse
from vetis_pydantic_types.base.fields import field
from vetis_pydantic_types.herriot.types.pilot.application_v2_1 import (
    ApplicationDataInternalType,
    ApplicationResultDataInternalType,
)
from vetis_pydantic_types.herriot.types.pilot.base_v2_1 import (
    ListOptions,
    UpdateDateInterval,
)
from vetis_pydantic_types.herriot.types.pilot.dictionary_v2_5 import (
    AnimalSpeciesInternalType,
    Location,
    RegionInternalType,
    SupervisedObjectInternalType,
)
from vetis_pydantic_types.herriot.types.pilot.document_v2_5 import (
    AnimalIdentity,
    AnimalIdentityStatusChange,
    AnimalLifecycleEvent,
    AnimalMarkingEvent,
    AnimalMedicationEvent,
    AnimalMedicationEventList,
    AnimalMovementEvent,
    AnimalRegistration,
    AnimalRegistrationList,
    AnimalRegistrationStatusChange,
    IssueDateInterval,
    ObservableAnimalGroup,
    UserInternalType,
    VeterinaryEventStatusChangeReason,
)

__NAMESPACE__ = "http://api.vetrf.ru/schema/cdm/herriot/applications/v1"


class ConfirmAnimalVeterinaryEventResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 4.3.

    "Подтверждение ветеринарного профилактического мероприятия"

    Attributes:
        medication_event: обновленная редакция сведений о
            зарегистрированном ветеринарном профилактическом мероприятии
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


class GetAnimalRegistrationByGuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 1.6.

    "Получение основных актуальных сведений о регистрации животного или
    группы животных по глобальному идентификатору"

    Attributes:
        animal_registration: актуальная редакция регистрационной
            карточки животного или группы животных без сведений о
            ветеринарных профилактических мероприятиях
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


class GetAnimalRegistrationByUuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 1.11.

    "Получение редакции основных сведений о регистрации животного или
    группы животных по идентификатору конкретной версии (редакции)"

    Attributes:
        animal_registration: сведения о запрашиваемой версии
            регистрационной карточки животного или группы животных без
            сведений о ветеринарных профилактических мероприятиях
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


class GetAnimalRegistrationChangesListResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 1.9.

    "Получение списка изменений по основным сведениям о регистрации
    животных или групп животных _на поднадзорном объекте_ за указанный
    период"

    Attributes:
        animal_registration_list: список созданных за указанный период
            времени версий регистрационных карточек животных или групп
            животных, которые содержатся в указанной зоне обслуживания
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


class GetAnimalRegistrationHistoryResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 1.8.

    "Получение всей истории изменений сведений о регистрации животного
    или группы животных по глобальному идентификатору"

    Attributes:
        animal_registration_list: список версий регистрационной карточки
            животного или группы животных
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


class GetAnimalRegistrationListResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 1.10.

    "Получение списка сведений о регистрации животных или групп животных
    _на поднадзорном объекте_ за указанный период"

    Attributes:
        animal_registration_list: список созданных за указанный период
            времени версий регистрационных карточек животных или групп
            животных, которые содержатся в указанной зоне обслуживания
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


class GetAnimalVeterinaryEventByGuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 4.4.

    "Получение актуальных сведений о зарегистрированном ветеринарном
    профилактическом мероприятии по глобальному идентификатору"

    Attributes:
        medication_event: актуальная редакция зарегистрированных
            сведений о ветеринарном профилактическом мероприятии
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


class GetAnimalVeterinaryEventByUuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 4.7.

    "Получение сведений о редакции ветеринарного профилактического
    мероприятия по идентификатору версии"

    Attributes:
        medication_event: сведения о запрашиваемой версии сведений о
            ветеринарном профилактическом мероприятии
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


class GetAnimalVeterinaryEventChangesListResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 4.5.

    "Получение списка изменений сведений о зарегистрированных
    ветеринарных профилактических мероприятиях _на поднадзорном объекте_
    за указанный период"

    Attributes:
        medication_event_list: список созданных за указанный период
            времени версий сведений о ветеринарных профилактических
            мероприятиях животных или групп животных, которые содержатся
            в указанной зоне обслуживания
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


class GetAnimalVeterinaryEventHistoryResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 4.6.

    "Получение всей истории изменений ветеринарного профилактического
    мероприятия по глобальному идентификатору"

    Attributes:
        medication_event_list: список версий сведений о ветеринарном
            профилактическом мероприятии
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


class GetFullAnimalRegistrationByGuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 1.7.

    "Получение полных актуальных сведений (включая ветпрофмероприятия) о
    регистрации животного или группы животных по глобальному
    идентификатору"

    Attributes:
        animal_registration: актуальная редакция регистрационной
            карточки животного или группы животных, включая сведения о
            ветеринарных профилактических мероприятиях
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


class GetFullAnimalRegistrationByUuidResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 1.12.

    "Получение редакции полных сведений (включая ветпрофмероприятия) о
    регистрации животного по идентификатору конкретной версии"

    Attributes:
        animal_registration: сведения о запрашиваемой версии
            регистрационной карточки животного или группы животных,
            включая сведения о ветеринарных профилактических
            мероприятиях
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


class ModifyAnimalRegistrationResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 1.2.

    "Внесение изменений в основные сведения о зарегистрированном
    животном или группе животных"

    Attributes:
        animal_registration: обновленная карточка животного или группы
            животных в статусе ACTIVE
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


class ModifyAnimalVeterinaryEventResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 4.2.

    "Редактирование сведений о ветеринарном профилактическом
    мероприятии"

    Attributes:
        medication_event: обновленная редакция сведений о
            зарегистрированном ветеринарном профилактическом мероприятии
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


class RegisterAnimalIdentityResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 2.1.

    "Регистрация сведений об идентификации зарегистрированного животного
    или группы животных (маркирование)"

    Attributes:
        animal_identity: зарегистрированные сведения об идентификации
            животного
    """

    class Meta:
        name = "RegisterAnimalIdentityResponse"

    model_config = ConfigDict(defer_build=True)
    animal_identity: Optional[AnimalIdentity] = field(
        default=None,
        metadata={
            "name": "animalIdentity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )


class RegisterAnimalMovementEventResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 1.3.

    "Регистрация сведения о перемещение/смене собственника
    зарегистрированного животного или групп животных"

    Attributes:
        animal_registration: обновленная карточка животного или группы
            животных в статусе RELOCATING или ACTIVE
    """

    class Meta:
        name = "RegisterAnimalMovementEventResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )


class RegisterAnimalResponseInternalType(ApplicationResultDataInternalType):
    """Результат заявки по операции 1.1.

    "Регистрация животного или группы животных"

    Attributes:
        animal_registration: зарегистрированная карточка животного или
            группы животного в статусе PREPARING или ACTIVE
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


class RegisterAnimalVeterinaryEventResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 4.1.

    "Регистрация ветеринарного профилактического мероприятия"

    Attributes:
        medication_event: зарегистрированные сведения о ветеринарном
            профилактическом мероприятии
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


class RemoveAnimalIdentityResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 2.2.

    "Прекращение регистрации сведений об идентификации
    зарегистрированного животного или группы животных (выбытие
    зарегистрированного средства маркирования)"

    Attributes:
        animal_identity: обновленные сведения об идентификации животного
            или группы животных в статусе TERMINATED
    """

    class Meta:
        name = "RemoveAnimalIdentityResponse"

    model_config = ConfigDict(defer_build=True)
    animal_identity: list[AnimalIdentity] = field(
        default_factory=list,
        metadata={
            "name": "animalIdentity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )


class ReplaceAnimalIdentityResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 2.3.

    "Перерегистрация сведений об идентификации зарегистрированного
    животного или группы животных (замена средства маркирования)"

    Attributes:
        removed_animal_identity: обновленные сведения об идентификации
            животного или группы животных в статусе TERMINATED
        registered_animal_identity: зарегистрированные сведения о новой
            идентификации животного или группы животных
    """

    class Meta:
        name = "ReplaceAnimalIdentityResponse"

    model_config = ConfigDict(defer_build=True)
    removed_animal_identity: Optional[AnimalIdentity] = field(
        default=None,
        metadata={
            "name": "removedAnimalIdentity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )
    registered_animal_identity: Optional[AnimalIdentity] = field(
        default=None,
        metadata={
            "name": "registeredAnimalIdentity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )


class TerminateAnimalRegistrationResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 1.4.

    "Прекращение регистрации животного или группы животных / выбытие
    животного (прекращение регистрации по той или иной причине)"

    Attributes:
        animal_registration: обновленная карточка животного или группы
            животных в статусе TERMINATED
    """

    class Meta:
        name = "TerminateAnimalRegistrationResponse"

    model_config = ConfigDict(defer_build=True)
    animal_registration: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistration",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )


class WithdrawAnimalIdentityResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 2.4.

    "Аннулирование сведений о регистрации сведений об идентификации
    животного или группы животных"

    Attributes:
        animal_identity: обновленные сведения об идентификации животного
            или группы животных в статусе WITHDRAWN
    """

    class Meta:
        name = "WithdrawAnimalIdentityResponse"

    model_config = ConfigDict(defer_build=True)
    animal_identity: list[AnimalIdentity] = field(
        default_factory=list,
        metadata={
            "name": "animalIdentity",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
        },
    )


class WithdrawAnimalRegistrationResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 1.5.

    "Аннулирование сведений о регистрации животного или группы животных"

    Attributes:
        animal_registration: обновленная карточка животного или группы
            животных в статусе WITHDRAWN
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


class WithdrawAnimalVeterinaryEventResponseInternalType(
    ApplicationResultDataInternalType
):
    """Результат заявки по операции 4.3.

    "Аннулирование сведений о ветеринарном профилактическом мероприятии"

    Attributes:
        medication_event: обновленная редакция сведений о
            зарегистрированном ветеринарном профилактическом мероприятии
            в статусе WITHDRAWN
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


class ConfirmAnimalVeterinaryEventRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 4.3.

    "Подтверждение ветеринарного профилактического мероприятия"

    Attributes:
        medication_event: глобальный идентификатор зарегистрированных
            сведений о ветеринарном профилактическом мероприятии
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


class GetAnimalRegistrationByGuidRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 1.6.

    "Получение основных актуальных сведений о регистрации животного или
    группы животных по глобальному идентификатору"

    Attributes:
        animal_registration_guid: глобальный идентификатор
            регистрационной карточки животного или группы животных
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


class GetAnimalRegistrationByUuidRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 1.10.

    "Получение редакции основных сведений о регистрации животного или
    группы животных по идентификатору конкретной версии (редакции)"

    Attributes:
        animal_registration_uuid: уникальный идентификатор версии
            регистрационной карточки животного или группы животных
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


class GetAnimalRegistrationChangesListRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 1.9.

    "Получение списка изменений по основным сведениям о регистрации
    животных или групп животных _на поднадзорном объекте_ за указанный
    период"

    Attributes:
        list_options: Параметры запрашиваемого списка
        update_date_interval: Интервал времени обновления
        region: Зона обслуживания: субъект РФ, на территории которого
            содержатся животные
        location: Зона обслуживания: место содержания животных
        operator: Поднадзорный объект, на котором осуществляется
            содержание животных
        animal_species: Биологический вид животного
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


class GetAnimalRegistrationHistoryRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 1.8.

    "Получение всей истории изменений сведений о регистрации животного
    или группы животных по глобальному идентификатору"

    Attributes:
        animal_registration_guid: глобальный идентификатор
            регистрационной карточки животного или группы животных
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


class GetAnimalRegistrationListRequestInternalType(HerriotApplicationRequest):
    """Заявка по операции 1.10.

    "Получение списка сведений о регистрации животных или групп животных
    _на поднадзорном объекте_ за указанный период"

    Attributes:
        list_options: Параметры запрашиваемого списка
        issue_date_interval: Период дат оформления документов
        region: Зона обслуживания: субъект РФ, на территории которого
            содержатся животные
        location: Зона обслуживания: место содержания животных
        operator: Поднадзорный объект, на котором осуществляется
            содержание животных
        animal_species: Биологический вид животного
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


class GetAnimalVeterinaryEventByGuidRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 4.4.

    "Получение актуальных сведений о зарегистрированном ветеринарном
    профилактическом мероприятии по глобальному идентификатору"

    Attributes:
        medication_event_guid: глобальный идентификатор
            зарегистрированных сведений о ветеринарном профилактическом
            мероприятии
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


class GetAnimalVeterinaryEventByUuidRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 4.7.

    "Получение сведений о редакции ветеринарного профилактического
    мероприятия по идентификатору версии"

    Attributes:
        medication_event_uuid: уникальный идентификатор версии сведений
            о ветеринарном профилактическом мероприятии
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


class GetAnimalVeterinaryEventChangesListRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 4.5.

    "Получение списка изменений сведений о зарегистрированных
    ветеринарных профилактических мероприятиях _на поднадзорном объекте_
    за указанный период"

    Attributes:
        list_options: Параметры запрашиваемого списка.
        update_date_interval: Интервал времени обновления. В список
            попадают все версии записи, дата создания которых попадает в
            указанный интервал.
        region: Зона обслуживания: субъект РФ, на территории которого
            содержатся животные
        location: зона обслуживания: место содержания животных
        operator: поднадзорный объект, на котором осуществляется
            содержание животных
        animal_registration_guid: глобальный идентификатор
            зарегистрированной карточки животного или группы животных
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


class GetAnimalVeterinaryEventHistoryRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 4.6.

    "Получение всей истории изменений ветеринарного профилактического
    мероприятия по глобальному идентификатору"

    Attributes:
        medication_event_guid: глобальный идентификатор
            зарегистрированных сведений о ветеринарном профилактическом
            мероприятии
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


class GetFullAnimalRegistrationByGuidRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 1.7.

    "Получение полных актуальных сведений (включая ветпрофмероприятия) о
    регистрации животного или группы животных по глобальному
    идентификатору"

    Attributes:
        animal_registration_guid: глобальный идентификатор
            регистрационной карточки животного или группы животных
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


class GetFullAnimalRegistrationByUuidRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 1.12.

    "Получение редакции полных сведений (включая ветпрофмероприятия) о
    регистрации животного по идентификатору конкретной версии"

    Attributes:
        animal_registration_uuid: уникальный идентификатор версии
            регистрационной карточки животного или группы животных
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


class ModifyAnimalRegistrationRequestInternalType(HerriotApplicationRequest):
    """Заявка по операции 1.2.

    "Внесение изменений в основные сведения о зарегистрированном
    животном или группе животных". В заявлении указываются _изменяемые_
    сведения о животном. Не допускается изменение сведений об
    идентификации, выбытии, ветпрофмероприятиях, текущем месте
    содержания.

    Attributes:
        animal_registration: Проект изменений существующей
            регистрационной карточки с указанным уникальным
            идентификатором версии.
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


class ModifyAnimalVeterinaryEventRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 4.2.

    "Редактирование сведений о ветеринарном профилактическом
    мероприятии"

    Attributes:
        medication_event: проект обновленных сведений о
            зарегистрированном ветеринарном профилактическом мероприятии
            с указанным глобальным идентификатором
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


class RegisterAnimalIdentityRequestInternalType(HerriotApplicationRequest):
    """Заявка по операции 2.1.

    "Регистрация сведений об идентификации зарегистрированного животного
    или группы животных (маркирование)"

    Attributes:
        animal_marking_event: проект сведений об идентификации,
            содержащий глобальный идентификатор зарегистрированного
            животного или группы животных
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


class RegisterAnimalMovementEventRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 1.3.

    "Регистрация сведения о перемещение/смене собственника
    зарегистрированного животного или групп животных"

    Attributes:
        referenced_movement_event: сведения о перемещении
        animal_registration_ref: Cведения о перемещаемых
            зарегистрированных животных или группах животных
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
    animal_registration_ref: list[AnimalRegistration] = field(
        default_factory=list,
        metadata={
            "name": "animalRegistrationRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )


class RegisterAnimalRequestInternalType(HerriotApplicationRequest):
    """Заявка по операции 1.1. "Регистрация животного или группы животных".

    Сценарии:
    - регистрация животного;
    - регистрация группы животных;
    - регистрация животного, ввезенного в РФ;
    - регистрация группы животных, ввезенных в РФ.

    Attributes:
        animal_registration: Проект регистрационной карточки животного
            или группы животных, включая сведения об идентификации
            животного, ввозе на территорию РФ, текущем содержании,
            потомстве
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


class RegisterAnimalVeterinaryEventRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 4.1.

    "Регистрация ветеринарного профилактического мероприятия"

    Attributes:
        referenced_medication_event: Проект сведений о ветеринарном
            профилактическом мероприятии
        specified_animal_group: список зарегистрированных животных или
            групп животных, в отношении которых осуществлялось данное
            мероприятие
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


class RemoveAnimalIdentityRequestInternalType(HerriotApplicationRequest):
    """Заявка по операции 2.2.

    "Прекращение регистрации сведений об идентификации
    зарегистрированного животного или группы животных (выбытие
    зарегистрированного средства маркирования)"

    Attributes:
        referenced_marking_event: сведения о выбытии зарегистрированного
            средства маркирования
        animal_identity_ref: глобальный идентификатор зарегистрированных
            сведений об идентификации животного, в отношении которых
            регистрируется выбытие
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
    animal_identity_ref: list[AnimalIdentity] = field(
        default_factory=list,
        metadata={
            "name": "animalIdentityRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )


class ReplaceAnimalIdentityRequestInternalType(HerriotApplicationRequest):
    """Заявка по операции 2.3.

    "Перерегистрация сведений об идентификации зарегистрированного
    животного или группы животных (замена средства маркирования)"

    Attributes:
        referenced_marking_event: сведения о замене средства
            маркирования
        animal_identity_ref: глобальный идентификатор сведений о
            зарегистрированных сведениях об идентификации животного
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
    animal_identity_ref: AnimalIdentity = field(
        metadata={
            "name": "animalIdentityRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "required": True,
        }
    )


class TerminateAnimalRegistrationRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 1.4.

    "Прекращение регистрации животного или группы животных / выбытие
    животного (прекращение регистрации по той или иной причине)"

    Attributes:
        referenced_lifecycle_event: сведения о выбытии животного
        animal_registration_ref: сведения о зарегистрированных животных
            или группах животных, в отношении которых регистрируется
            выбытие
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


class WithdrawAnimalIdentityRequestInternalType(HerriotApplicationRequest):
    """Заявка по операции 2.4.

    "Аннулирование сведений о регистрации сведений об идентификации
    животного или группы животных"

    Attributes:
        withdraw_details: сведения об аннулировании сведений
        animal_identity_ref: глобальный идентификатор аннулируемых
            сведений об идентификации животного или группы животных
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
    animal_identity_ref: list[AnimalIdentity] = field(
        default_factory=list,
        metadata={
            "name": "animalIdentityRef",
            "type": "Element",
            "namespace": "http://api.vetrf.ru/schema/cdm/herriot/applications/v1",
            "min_occurs": 1,
        },
    )


class WithdrawAnimalRegistrationRequestInternalType(HerriotApplicationRequest):
    """Заявка по операции 1.5.

    "Аннулирование сведений о регистрации животного или группы животных"

    Attributes:
        withdraw_details: сведения об аннулировании регистрационной
            карточки животного
        animal_registration_ref: сведения о зарегистрированных животных
            или группах животных
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


class WithdrawAnimalVeterinaryEventRequestInternalType(
    HerriotApplicationRequest
):
    """Заявка по операции 4.3.

    "Аннулирование сведений о ветеринарном профилактическом мероприятии"

    Attributes:
        reason: сведения об аннулировании
        medication_event_ref: глобальный идентификатор аннулируемых
            сведений о ветеринарном профилактическом мероприятии
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


class ConfirmAnimalVeterinaryEventResponse(
    ApplicationResponse, ConfirmAnimalVeterinaryEventResponseInternalType
):
    class Meta:
        name = "confirmAnimalVeterinaryEventResponse"
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
