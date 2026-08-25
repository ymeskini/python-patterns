from enum import StrEnum, auto


class PaymentStatus(StrEnum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()
