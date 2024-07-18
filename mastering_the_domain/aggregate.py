from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4


# Value Object
@dataclass(frozen=True, slots=True)
class Email:
    value: str

    def __post__init__(self, value: str):
        if not self.validate_email(value):
            raise ValueError(f"Invalid email address: {value}")

    @staticmethod
    def validate_email(email: str) -> bool:
        return "@" in email and "." in email


# Entities
@dataclass
class User:
    id: UUID
    username: str
    created_at: datetime = datetime.now()


# Aggregate
# Invariants:
# - An account must have at least one user
@dataclass
class Account:
    id: UUID  # Aggregate root
    name: str
    email: Email
    _users: list[User]
    created_at: datetime = datetime.now()

    def __post_init__(self):
        if len(self._users) == 0:
            raise ValueError("An account must have at least one user")

    def add_user(self, user: User):
        self._users.append(user)

    def remove_user(self, id: UUID):
        new_users = [user for user in self._users if user.id != id]

        if len(new_users) == 0:
            raise ValueError("An account must have at least one user")

        self._users = new_users.copy()

    @property
    def users(self) -> list[User]:
        return self._users


# Example Usage


def main() -> None:
    user1 = User(id=uuid4(), username="alice")
    user2 = User(id=uuid4(), username="bob")

    account = Account(
        id=uuid4(), name="Arjan", email=Email("Arjan@example.com"), _users=[user1]
    )

    account.add_user(user2)

    print(account.users)


if __name__ == "__main__":
    main()
