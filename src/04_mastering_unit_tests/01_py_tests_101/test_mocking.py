"""
Best practice: unit tests shouldn't hit real external systems (email,
network, disk, the clock...). Replace the dependency with a test double.

- `unittest.mock.Mock` / `MagicMock` record how they were called, so you can
  assert on the interaction instead of on a real side effect.
- `monkeypatch` swaps out attributes, functions, dict entries, or environment
  variables for the duration of a test, and restores the original
  automatically afterwards - even if the test fails.
"""

import os
from unittest.mock import Mock

import calculator
from notifications import send_order_confirmation


def test_send_order_confirmation_calls_the_email_client():
    # A `Mock` stands in for the real EmailClient - no network call happens.
    client = Mock()

    send_order_confirmation(email="a@example.com", total=42.5, client=client)

    client.send.assert_called_once_with(
        to="a@example.com",
        subject="Order confirmation",
        body="Thanks for your order! Total: $42.50",
    )


def test_send_order_confirmation_can_be_called_for_multiple_orders():
    client = Mock()

    send_order_confirmation(email="a@example.com", total=10, client=client)
    send_order_confirmation(email="b@example.com", total=20, client=client)

    assert client.send.call_count == 2


def test_monkeypatch_setattr_replaces_a_function(monkeypatch):
    # Swap out `calculator.add` itself, e.g. to isolate a caller from a
    # dependency you don't want to exercise in this test.
    monkeypatch.setattr(calculator, "add", lambda a, b: 999)

    assert calculator.add(1, 2) == 999


def test_monkeypatch_setenv_sets_an_environment_variable(monkeypatch):
    monkeypatch.setenv("DISCOUNT_ENABLED", "true")

    assert os.environ["DISCOUNT_ENABLED"] == "true"
    # No cleanup needed: pytest restores the previous environment after the test.
