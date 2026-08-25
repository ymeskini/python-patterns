from dataclasses import dataclass, field
from datetime import datetime

import numpy as np


@dataclass
class Account:
    owner: str
    transactions: list[tuple[datetime, str, int]] = field(
        default_factory=list[tuple[datetime, str, int]]
    )
    _balance: int = 0

    def add_transaction(self, transaction_type: str, amount: int) -> None:
        # Appending a transaction record
        self.transactions.append((datetime.now(), transaction_type, amount))

    def calculate_balance(self):
        # Using NumPy to sum the amounts in the transactions list
        amounts = np.array([transaction[2] for transaction in self.transactions])
        return np.sum(amounts)

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.add_transaction("Deposit", amount)
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount: int) -> None:
        if 0 < amount <= self.calculate_balance():
            self.add_transaction("Withdrawal", -amount)
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.calculate_balance()


def main() -> None:
    account = Account(owner="Alex Doe")
    account.deposit(200)
    account.withdraw(150)
    print(f"Current Balance: {account.get_balance()}")


if __name__ == "__main__":
    main()
