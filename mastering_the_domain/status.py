from enum import StrEnum, auto


class PaymentStatus(StrEnum):
    COMPLETED = auto()
    PENDING = auto()
    FAILED = auto()


class AccountStatus(StrEnum):
    ACTIVE = auto()
    DISABLED = auto()
    PAUSED = auto()
