from dataclasses import dataclass
from typing import Any

# This is a Value Object
# It does not have an identity
# It is immutable
# It is interchangeable


@dataclass
class Address:
    street: str
    city: str
    zipcode: str
    country: str

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Address):
            return False
        return (
            self.street == other.street
            and self.city == other.city
            and self.zipcode == other.zipcode
            and self.country == other.country
        )

    def __hash__(self) -> int:
        return hash((self.street, self.city, self.zipcode, self.country))
