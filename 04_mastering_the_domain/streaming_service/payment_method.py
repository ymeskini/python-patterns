from dataclasses import dataclass
from enum import StrEnum, auto


# This is an value object
# It does not have an identity
# It is immutable
# It is interchangeable
# It is side-effect free


class PaymentProssesor(StrEnum):
    STRIPE = auto()
    MASTER_CARD = auto()
    VISA = auto()


class CardType(StrEnum):
    CREDIT = auto()
    DEBIT = auto()


@dataclass
class PaymentMethod:
    payment_processor: PaymentProssesor
    type_of_card: CardType
