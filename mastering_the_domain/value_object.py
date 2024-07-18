from dataclasses import dataclass
from typing import TypedDict


@dataclass(frozen=True, slots=True)
class Address:
    street: str
    city: str
    zip_code: str


class AddressDict(TypedDict):
    street: str
    city: str
    zip_code: str


def main() -> None:
    address = Address(
        street="123 Main St",
        city="Springfield",
        zip_code="12345",
    )

    address_dict: AddressDict = {
        "street": "123 Main St",
        "city": "Springfield",
        "zip_code": "12345",
    }

    print(f"Class: {address}")
    print(f"Dict: {address_dict}")


if __name__ == "__main__":
    main()
