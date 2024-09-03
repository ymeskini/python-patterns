# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Exercise: Adding type hints
# Level: Intermediate
#
# Add type hints to the following functions. There are a few different ways to do this.
# One solution is provided in the solution_intermediate.py file.
# Make sure that you try to solve this exercise on your own before looking at the solution.
# 
# If you are using an IDE that does not support type hints, you can skip this exercise.
# Make sure that you have installed pylance or similar to get type hints in your IDE.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class ShoppingCart:
    def __init__(self, owner):
        """
        Initializes a shopping cart.

        Args:
            owner (str): The owner of the shopping cart.
        """
        self.owner = owner
        self.items = []

    def add_item(self, id, quantity, price):
        """
        Adds an item to the shopping cart.

        Args:
            id (int): The name of the item.
            quantity (int): The quantity of the item.
            price (float): The price per unit of the item.
        """
        item = {"id": id, "quantity": quantity, "price": price}
        self.items.append(item)

    def calculate_total(self):
        """
        Calculates the total cost of items in the shopping cart.

        Returns:
            float: The total cost.
        """
        total_cost = sum(item["quantity"] * item["price"] for item in self.items)
        return total_cost

    def filter_items(self, filter_func):
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
