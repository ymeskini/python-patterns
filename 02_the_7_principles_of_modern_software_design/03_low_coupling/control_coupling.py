from dataclasses import dataclass
from enum import StrEnum, auto


class Operation(StrEnum):
    DEPOSIT = auto()
    WITHDRAW = auto()
    INTEREST = auto()


@dataclass
class Account:
    owner: str
    balance: int | float = 0

    def update_balance(self, amount: int, operation: Operation) -> None:
        if operation == Operation.DEPOSIT:
            self.balance += amount
            print(
                f"{self.owner}'s account: Deposited {amount}, New balance: {self.balance}"
            )
        elif operation == Operation.WITHDRAW:
            if amount > self.balance:
                print("Withdrawal amount exceeds the current balance.")
            else:
                self.balance -= amount
                print(
                    f"{self.owner}'s account: Withdrew {amount}, New balance: {self.balance}"
                )
        elif operation == Operation.INTEREST:
            interest = self.balance * 0.05
            self.balance += interest
            print(
                f"{self.owner}'s account: Interest added {interest}, New balance: {self.balance}"
            )
        else:
            print("Invalid operation.")


def main() -> None:
    account = Account("John Doe", 1000)
    account.update_balance(100, Operation.DEPOSIT)
    account.update_balance(200, Operation.WITHDRAW)
    account.update_balance(0, Operation.INTEREST)


if __name__ == "__main__":
    main()
