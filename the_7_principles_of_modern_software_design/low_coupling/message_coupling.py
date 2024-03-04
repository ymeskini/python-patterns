from dataclasses import dataclass, field
from enum import Enum

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"
    COMPLETED = "completed"


@dataclass
class AccountService:
    queue: "MessageQueue"

    def perform_transaction(self, account_id: int, amount: int):
        message = {
            "account_id": account_id,
            "amount": amount,
            "type": TransactionType.COMPLETED,
        }
        self.queue.publish(message)


class NotificationService:
    def receive(self, message: dict[str, int | str | TransactionType]):
        if message["type"] == TransactionType.COMPLETED:
            print(
                f"Notification: Transaction completed for account {message['account_id']}."
            )


@dataclass
class MessageQueue:
    subscribers: list[NotificationService] = field(default_factory=list)

    def publish(self, message: dict[str, int | str | TransactionType]) -> None:
        for subscriber in self.subscribers:
            subscriber.receive(message)

    def subscribe(self, subscriber: NotificationService):
        self.subscribers.append(subscriber)


def main() -> None:
    queue = MessageQueue()
    account_service = AccountService(queue)
    notification_service = NotificationService()

    queue.subscribe(notification_service)

    account_service.perform_transaction(12345, 1000)


if __name__ == "__main__":
    main()