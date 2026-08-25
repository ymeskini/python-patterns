from dataclasses import dataclass, field


class EmptyCartError(Exception):
    """Raised when checking out a cart that has no items."""


@dataclass
class ShoppingCart:
    items: dict[str, float] = field(default_factory=dict)

    def add_item(self, name: str, price: float) -> None:
        if price < 0:
            raise ValueError("price cannot be negative")
        self.items[name] = price

    def remove_item(self, name: str) -> None:
        del self.items[name]

    @property
    def total(self) -> float:
        return sum(self.items.values())

    def checkout(self) -> float:
        if not self.items:
            raise EmptyCartError("cannot checkout an empty cart")
        total = self.total
        self.items.clear()
        return total
