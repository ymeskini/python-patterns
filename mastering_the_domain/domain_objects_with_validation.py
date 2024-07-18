from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Address:
    street: str
    city: str
    zip_code: str

    def __post__init__(self) -> None:
        if not self.valid_zip_code():
            raise ValueError("Invalid zip code")

    def valid_zip_code(self) -> bool:
        return len(self.zip_code) == 5


def main() -> None:
    address = Address(
        street="123 Main St",
        city="Springfield",
        zip_code="12345",
    )

    print(address)


if __name__ == "__main__":
    main()
