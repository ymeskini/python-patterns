from enum import StrEnum, auto


class PaymentStatus(StrEnum):
    OPEN = auto()
    PAID = auto()
