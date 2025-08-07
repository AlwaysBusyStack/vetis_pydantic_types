from enum import Enum


class VetisCircuitEnum(str, Enum):
    """Перечисление для контуров ВетИС.API"""

    TEST = 'pilot'
    PRODUCTIVE = 'production'
