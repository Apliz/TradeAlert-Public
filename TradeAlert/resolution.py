from enum import StrEnum

class Resolution(StrEnum):
    """
        Time resolution enumerator class for general use
    """
    _1TICK = "1t"
    _1SECOND = "1s"
    _1MINUTE = "1m"
    _5MINUTE = "5m"
    _15MINUTE = "15m"

