from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from address import Address
from email_address import EmailAddress
from user import User

# This Account class is an Entity
# Because it has an identity (id)
# It is mutable
# It has a lifecycle because of the inserted_at and updated_at fields
# It also has value objects (Address and EmailAddress)


@dataclass
class Account:
    id: UUID
    owner: User
    users: list[User]
    address: Address
    email_address: EmailAddress
    inserted_at: datetime
    updated_at: datetime

    def __post_init__(self):
        self.users = [self.owner]

    def add_user(self, user: User):
        self.users.append(user)
