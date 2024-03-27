from pos.authorization import authorize_google, authorize_sms
from pos.order import Order
from pos.payment import (
    CreditPaymentProcessor,
    DebitPaymentProcessor,
    PaypalPaymentProcessor,
)


def read_choice(question: str, choices: list[str]) -> str:
    choice = ""
    while choice not in choices:
        choice = input(f"{question} ({', '.join(choices)})? ")
    return choice


def create_order():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)
    return order


def main():
    order = create_order()

    print(f"The total price is: ${(order.total_price / 100):.2f}.")

    # select the payment method
    payment_processor_choice = read_choice(
        "How would you like to pay?", ["paypal", "credit", "debit"]
    )

    # select the authentication method
    auth_choice = read_choice("Choose your authentication method", ["google", "sms"])

    if payment_processor_choice == "paypal":
        email_address = input("Enter your email address: ")
        processor = PaypalPaymentProcessor(email_address)
    elif payment_processor_choice == "credit":
        security_code = input("Enter the security code: ")
        processor = CreditPaymentProcessor(security_code)
    else:
        processor = DebitPaymentProcessor()

    if auth_choice == "google":
        auth = authorize_google
    else:
        auth = authorize_sms

    processor.pay(order, auth)


if __name__ == "__main__":
    main()
