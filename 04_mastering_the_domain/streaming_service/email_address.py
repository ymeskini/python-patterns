from dataclasses import dataclass
from typing import Any

# This is a Value Object
# It does not have an identity
# It is immutable
# It is interchangeable


@dataclass
class EmailAddress:
    address: str

    def __post_init__(self):
        if not self.is_valid():
            raise ValueError("Invalid email address")

    def is_valid(self):
        # Add your email address validation logic here
        # For simplicity, let's assume any non-empty string is valid
        return bool(self.address)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EmailAddress):
            return False
        return self.address == other.address
