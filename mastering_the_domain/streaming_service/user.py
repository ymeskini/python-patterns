from dataclasses import dataclass

# This is an Entity
# Because it has an identity (id)
# It is mutable
# It has a lifecycle because of the inserted_at and updated_at fields


@dataclass
class User:
    id: str
    name: str
    email: str
