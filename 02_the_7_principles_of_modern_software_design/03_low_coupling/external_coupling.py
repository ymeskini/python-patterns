from enum import StrEnum, auto
import stripe


class Currency(StrEnum):
    USD = auto()
    EUR = auto()
    GBP = auto()


class PaymentProcessor:
    def __init__(self):
        # Stripe's setup can be encapsulated within this class
        self.stripe = stripe

    def charge_card(
        self, amount: int, currency: str, card_token: str, description: str = "Charge"
    ) -> tuple[bool, stripe.Charge | None]:
        """Charge a credit card using Stripe."""
        try:
            # Create a charge in Stripe
            charge = self.stripe.Charge.create(
                amount=amount,
                currency=currency,
                source=card_token,
                description=description,
            )
            return True, charge
        except stripe.StripeError as e:
            print(f"Stripe Error: {e}")
            return False, None


def main() -> None:
    processor = PaymentProcessor()
    success, charge = processor.charge_card(1000, "usd", "tok_visa", "Example charge")
    if success:
        print(f"Charge successful: {charge}")
    else:
        print("Charge failed.")


if __name__ == "__main__":
    main()
