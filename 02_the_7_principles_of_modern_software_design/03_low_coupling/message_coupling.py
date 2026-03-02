from dataclasses import dataclass, field
from enum import StrEnum, auto


class TransactionType(StrEnum):
    DEPOSIT = auto()
    WITHDRAWAL = auto()
    TRANSFER = auto()
    COMPLETED = auto()


type Message = dict[str, int | str | TransactionType]


@dataclass
class AccountService:
    queue: "MessageQueue"

    def perform_transaction(self, account_id: int, amount: int):
        message: Message = {
            "account_id": account_id,
            "amount": amount,
            "type": TransactionType.COMPLETED,
        }
        self.queue.publish(message)


class NotificationService:
    def receive(self, message: Message):
        if message["type"] == TransactionType.COMPLETED:
            print(
                f"Notification: Transaction completed for account {message['account_id']}."
            )


@dataclass
class MessageQueue:
    subscribers: list[NotificationService] = field(
        default_factory=list[NotificationService]
    )

    def publish(self, message: Message) -> None:
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
