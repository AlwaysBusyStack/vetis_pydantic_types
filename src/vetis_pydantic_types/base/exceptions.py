class VetisError(Exception):
    """Базовое исключение для ошибок VetIS."""


class VetisFaultError(VetisError):
    """Ошибка SOAP Fault."""


class VetisBusinessError(VetisError):
    """Бизнес-ошибка приложения."""


class VetisUnauthorizedError(VetisError):
    """Ошибка авторизации системы в шлюзе ВетИС.API."""


class VetisTooManyRequestsError(VetisError):
    """Ошибка достижения лимита кол-ва запросов в секунду."""
