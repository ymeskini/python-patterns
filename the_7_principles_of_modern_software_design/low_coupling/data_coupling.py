from enum import Enum
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class TransactionService:
    def process_deposit(self, account_id: int, amount: int) -> None:
        self.log_transaction(account_id, amount, TransactionType.DEPOSIT)

    def process_withdrawal(self, account_id: int, amount: int) -> None:
        self.log_transaction(account_id, amount, TransactionType.WITHDRAWAL)

    def log_transaction(
        self, account_id: int, amount: int, transaction_type: TransactionType
    ):
        logging.info(
            f"Transaction - Account ID: {account_id}, Amount: {amount}, Type: {transaction_type}"
        )


def main() -> None:
    transaction_service = TransactionService()
    transaction_service.process_deposit(1, 1000)
    transaction_service.process_withdrawal(1, 500)


if __name__ == "__main__":
    main()
