from dataclasses import dataclass


@dataclass
class Account:
    owner: str
    _balance: int = 0

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}: Deposited {amount}")
        else:
            print(f"{self.owner}: Deposit attempt with invalid amount")

    def withdraw(self, amount: int) -> None:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{self.owner}: Withdrew {amount}")
        else:
            print(f"{self.owner}: Withdrawal attempt with invalid amount")

    def get_balance(self) -> int:
        return self._balance


accounts: list[Account] = []


# Module 1: Account Management System
def create_account(owner: str, initial_balance: int) -> None:
    account = Account(owner, initial_balance)
    accounts.append(account)
    print(f"Account created for {owner}")


def get_total_balance() -> int:
    total = 0
    for account in accounts:
        total += account.get_balance()
    return total


def main() -> None:
    create_account("John Doe", 1000)
    create_account("Mary Williams", 2000)

    print(f"Total balance: {get_total_balance()}")


if __name__ == "__main__":
    main()
