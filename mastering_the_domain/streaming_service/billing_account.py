from dataclasses import dataclass
from account import Account
from payment_details import PaymentDetails

# This is an Aggregate
# Because it has an identity (id)
# It is mutable
# It has a lifecycle because of the inserted_at and updated_at fields
# It has a root Entity (Account) and a Entity (payment_details),
# The Account is the root of the Aggregate
# The boundary of the Aggregate is the Account


@dataclass
class BillingAccount:
    id: str
    payment_details: PaymentDetails
    account: Account
