"""
Fixtures provide reusable, composable setup (and teardown) for tests. Prefer
them over copy-pasted setup code or unittest-style setUp/tearDown methods.
"""

import pytest

from shopping_cart import ShoppingCart


@pytest.fixture
def cart_with_items(cart: ShoppingCart) -> ShoppingCart:
    # Fixtures can request other fixtures - pytest resolves the dependency
    # chain for you (`cart` here comes from conftest.py).
    cart.add_item("book", 12.5)
    cart.add_item("pen", 1.5)
    return cart


def test_total_sums_all_item_prices(cart_with_items):
    assert cart_with_items.total == 14.0


def test_remove_item_drops_it_from_the_cart(cart_with_items):
    cart_with_items.remove_item("pen")

    assert cart_with_items.items == {"book": 12.5}


@pytest.fixture
def tracked_cart():
    # A `yield` fixture splits into setup (before yield) and teardown (after
    # yield). The teardown always runs, even if the test fails.
    cart = ShoppingCart()
    print("\n[setup] cart created")
    yield cart
    print("[teardown] cart discarded")


def test_checkout_empties_the_cart(tracked_cart):
    tracked_cart.add_item("book", 12.5)

    tracked_cart.checkout()

    assert tracked_cart.items == {}


@pytest.fixture(scope="module")
def shared_catalog():
    # `scope="module"` builds this fixture once and reuses it for every test
    # in this file, instead of re-creating it per test (the default is
    # `scope="function"`). Use a wider scope for expensive, read-only setup.
    return {"book": 12.5, "pen": 1.5, "notebook": 4.0}


def test_catalog_has_a_book(shared_catalog):
    assert "book" in shared_catalog


def test_catalog_has_a_pen(shared_catalog):
    assert "pen" in shared_catalog


def test_writing_a_receipt_to_disk(tmp_path, cart_with_items):
    # `tmp_path` is a built-in pytest fixture: a fresh, isolated temp directory
    # per test, cleaned up automatically - no manual tempfile/shutil bookkeeping.
    receipt = tmp_path / "receipt.txt"
    receipt.write_text(f"Total: {cart_with_items.total}")

    assert receipt.read_text() == "Total: 14.0"
