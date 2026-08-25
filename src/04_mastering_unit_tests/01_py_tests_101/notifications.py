from typing import Protocol


class EmailClient(Protocol):
    def send(self, to: str, subject: str, body: str) -> None: ...


def send_order_confirmation(email: str, total: float, client: EmailClient) -> None:
    client.send(
        to=email,
        subject="Order confirmation",
        body=f"Thanks for your order! Total: ${total:.2f}",
    )
