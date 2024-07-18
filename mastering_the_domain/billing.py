from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum, auto


class Status(StrEnum):
    COMPLETED = auto()
    PENDING = auto()
    FAILED = auto()


# Entity: Represents an account that can make payments
@dataclass
class Account:
    id: str
    username: str
    email: str
    inserted_at: datetime
    updated_at: datetime


# Entity: Represents a payment made by an account
@dataclass
class Payment:
    id: str
    account_id: str
    amount: float
    payment_date: datetime
    status: Status
    inserted_at: datetime
    updated_at: datetime


# Aggregate Root: Manages payments and behaviors related to an account
@dataclass
class Billing:
    account: Account
    payments: list[Payment]

    def total_amount_paid(self):
        return sum(
            payment.amount for payment in self.payments if payment.status == "completed"
        )

    def number_of_payments(self):
        return len(
            [payment for payment in self.payments if payment.status == "completed"]
        )

    def last_payment_date(self):
        completed_payments = [
            payment.payment_date
            for payment in self.payments
            if payment.status == "completed"
        ]
        return max(completed_payments) if completed_payments else None

    def __repr__(self):
        return (
            f"BillingAggregate(id={self.account.id}, "
            f"total_amount_paid={self.total_amount_paid()}, "
            f"number_of_payments={self.number_of_payments()}, "
            f"last_payment_date={self.last_payment_date()})"
        )


def main() -> None:
    account = Account(
        id="123",
        username="johndoe",
        email="johndoe@example.com",
        inserted_at=datetime.now(),
        updated_at=datetime.now(),
    )

    # Example payment details
    payments = [
        Payment(
            id="1",
            account_id="123",
            amount=100.0,
            payment_date=datetime(2023, 1, 1),
            inserted_at=datetime.now(),
            updated_at=datetime.now(),
            status=Status.COMPLETED,
        ),
        Payment(
            id="3",
            account_id="123",
            amount=75.0,
            inserted_at=datetime.now(),
            updated_at=datetime.now(),
            payment_date=datetime(2023, 3, 1),
            status=Status.PENDING,
        ),
    ]

    # Create billing aggregate
    billing = Billing(account, payments)

    # Output aggregate details
    print(billing)


# Example usage:
if __name__ == "__main__":
    main()
