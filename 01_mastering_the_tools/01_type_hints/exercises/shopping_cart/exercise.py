from typing import Callable, TypedDict


class Item(TypedDict):
    id: int
    quantity: int
    price: float


class ShoppingCart:
    def __init__(self, owner: str):
        """
        Initializes a shopping cart.

        Args:
            owner (str): The owner of the shopping cart.
        """
        self.owner = owner
        self.items: list[Item] = []

    def add_item(self, id: int, quantity: int, price: float) -> None:
        """
        Adds an item to the shopping cart.

        Args:
            id (int): The name of the item.
            quantity (int): The quantity of the item.
            price (float): The price per unit of the item.
        """
        self.items.append({"id": id, "quantity": quantity, "price": price})

    def calculate_total(self) -> float:
        """
        Calculates the total cost of items in the shopping cart.

        Returns:
            float: The total cost.
        """
        total_cost = sum(item["quantity"] * item["price"] for item in self.items)
        return total_cost

    def filter_items(self, filter_func: Callable[[Item], bool]):
        """
        Filters the items in the shopping cart.

        Args:
            filter_func (function): The function used to filter the items.
        """

        filtered_items = [item for item in self.items if filter_func(item)]
        return filtered_items


def main() -> None:
    alice_cart = ShoppingCart("Alice")

    alice_cart.add_item(1, 3, 1.50)
    alice_cart.add_item(2, 2, 0.75)
    alice_cart.add_item(3, 1, 15.99)

    total_cost_alice = alice_cart.calculate_total()
    print(total_cost_alice)


if __name__ == "__main__":
    main()
