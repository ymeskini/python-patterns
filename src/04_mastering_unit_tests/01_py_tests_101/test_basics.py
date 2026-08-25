"""
Pytest 101: the basics.

- Test files are named `test_*.py` (or `*_test.py`) so pytest can discover them.
- Test functions are named `test_*` - no base class or registration needed.
- Plain `assert` is enough: pytest rewrites it to show a helpful diff on failure.
- Structure each test as Arrange -> Act -> Assert, and keep one behaviour per test.
"""

from calculator import add, apply_discount


def test_add_returns_the_sum_of_two_numbers():
    # Arrange
    a, b = 2, 3

    # Act
    result = add(a, b)

    # Assert
    assert result == 5


def test_apply_discount_reduces_the_price():
    result = apply_discount(price=100, percent=25)

    assert result == 75


def test_add_item_stores_price_by_name(cart):
    # `cart` comes from the fixture in conftest.py - pytest injects it
    # automatically because the argument name matches the fixture name.
    cart.add_item("book", 12.5)

    assert cart.items == {"book": 12.5}
    assert cart.total == 12.5
