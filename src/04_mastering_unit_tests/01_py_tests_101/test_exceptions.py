"""
Use `pytest.raises` to assert that code raises the expected exception - and
`match` to pin down the message, so the test fails loudly if the wrong error
sneaks through instead of silently passing.
"""

import pytest

from calculator import apply_discount, divide
from shopping_cart import EmptyCartError, ShoppingCart


def test_divide_by_zero_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError, match="cannot divide by zero"):
        divide(10, 0)


def test_apply_discount_rejects_out_of_range_percent():
    with pytest.raises(ValueError):
        apply_discount(100, percent=150)


def test_checkout_on_empty_cart_raises():
    cart = ShoppingCart()

    with pytest.raises(EmptyCartError):
        cart.checkout()


def test_exception_carries_useful_context():
    # `pytest.raises` returns an ExceptionInfo, so you can inspect the actual
    # exception object once the `with` block exits.
    with pytest.raises(ValueError) as exc_info:
        apply_discount(100, percent=-10)

    assert "percent" in str(exc_info.value)
