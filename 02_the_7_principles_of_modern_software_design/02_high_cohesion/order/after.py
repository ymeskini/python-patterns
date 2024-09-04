from dataclasses import dataclass
from enum import StrEnum, auto


class PaymentStatus(StrEnum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


@dataclass
class ItemOrder:
    name: str
    quantity: int
    price: int


class Order:
    def __init__(self):
        self.items: list[ItemOrder] = []
        self.status: PaymentStatus = PaymentStatus.OPEN

    def add_item(self, name: str, quantity: int, price: int) -> None:
        item = ItemOrder(name, quantity, price)
        self.items.append(item)


class PaymentProcessor:
    def pay_debit(self, order: Order, security_code: str) -> None:
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = PaymentStatus.PAID

    def pay_credit(self, order: Order, security_code: str) -> None:
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = PaymentStatus.PAID


def main() -> None:
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 15)
    order.add_item("USB cable", 2, 5)

    processor = PaymentProcessor()
    processor.pay_debit(order, "0372846")


if __name__ == "__main__":
    main()
