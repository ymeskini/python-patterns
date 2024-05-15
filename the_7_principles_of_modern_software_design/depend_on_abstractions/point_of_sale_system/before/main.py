from point_of_sale.order import Order
from point_of_sale.payment import Authorizer, PaymentProcessor


def main() -> None:
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)

    print(f"The total price is: ${(order.total_price / 100):.2f}.")
    processor = PaymentProcessor(Authorizer.SMS)
    processor.pay_credit(order, "123456")


if __name__ == "__main__":
    main()
