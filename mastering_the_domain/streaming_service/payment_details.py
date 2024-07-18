from dataclasses import dataclass
from datetime import datetime
from payment_method import PaymentMethod

# This is an Entity
# Because it has an identity (id)
# It is mutable
# It has a lifecycle because of the inserted_at and updated_at fields
# It has a value object (PaymentMethod)


@dataclass
class PaymentDetails:
    id: str
    payment_method: PaymentMethod
    currency: str
    inserted_at: datetime
    updated_at: datetime
