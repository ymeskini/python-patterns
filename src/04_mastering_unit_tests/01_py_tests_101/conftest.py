import pytest

from shopping_cart import ShoppingCart


@pytest.fixture
def cart() -> ShoppingCart:
    """A fresh, empty cart for every test that asks for one.

    Fixtures defined in conftest.py are shared across every test file in this
    folder (and its subfolders) without needing to be imported.
    """
    return ShoppingCart()
