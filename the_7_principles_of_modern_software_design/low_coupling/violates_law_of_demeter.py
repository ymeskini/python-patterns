from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    email: str


@dataclass
class Account:
    customer: Customer
    balance: int = 0

class AccountManager:
    def email_customer(self, account: Account):
        customer_email = account.customer.email
        print(f"Emailing {customer_email} about the transaction...")


def main() -> None:
    customer = Customer(name="John Doe", email="johndoe@example.com")
    account = Account(customer=customer)

    account_manager = AccountManager()
    account_manager.email_customer(account)


if __name__ == "__main__":
    main()
