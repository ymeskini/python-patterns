"""
`@pytest.mark.parametrize` runs the same test body against many inputs, so you
avoid copy-pasting near-identical tests - and each case is reported (and can
fail) independently.
"""

import pytest

from calculator import add, apply_discount


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (-2, -3, -5),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "price, percent, expected",
    [
        # `pytest.param(..., id=...)` gives each case a readable name in the
        # test output (e.g. `test_apply_discount[half-off]`) instead of an index.
        pytest.param(100, 0, 100, id="no-discount"),
        pytest.param(100, 50, 50, id="half-off"),
        pytest.param(100, 100, 0, id="free"),
    ],
)
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected


@pytest.mark.parametrize("name, price", [("book", 12.5), ("pen", 1.0)])
def test_add_item_accepts_various_items(cart, name, price):
    # Fixtures and parametrize compose freely: pytest fills in `cart` from
    # conftest.py and `name`/`price` from the table above for every run.
    cart.add_item(name, price)

    assert cart.items[name] == price
