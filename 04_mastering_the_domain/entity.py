from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum, auto
from typing import TypedDict
from uuid import UUID, uuid4


class AccountStatus(StrEnum):
    ACTIVE = auto()
    INACTIVE = auto()
    PENDING = auto()
    SUSPENDED = auto()


### Object-Oriented
@dataclass
class Account:
    id: UUID
    username: str
    email: str
    status: AccountStatus
    inserted_at: datetime
    updated_at: datetime


### Functional


class AccountDict(TypedDict):
    id: UUID
    username: str
    email: str
    status: str
    inserted_at: str
    updated_at: str


def main() -> None:
    account = Account(
        id=uuid4(),
        username="johndoe",
        email="johndoe@example.com",
        status=AccountStatus.ACTIVE,
        inserted_at=datetime.now(),
        updated_at=datetime.now(),
    )

    account_dict: AccountDict = {
        "id": uuid4(),
        "username": "johndoe",
        "email": "johndoe@example.com",
        "status": "ACTIVE",
        "inserted_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }

    print(f"Class: {account}")
    print(f"Dict: {account_dict}")


if __name__ == "__main__":
    main()
