class VetisError(Exception):
    """Базовое исключение для ошибок VetIS."""


class VetisFaultError(VetisError):
    """Ошибка SOAP Fault."""


class VetisBusinessError(VetisError):
    """Бизнес-ошибка приложения."""
