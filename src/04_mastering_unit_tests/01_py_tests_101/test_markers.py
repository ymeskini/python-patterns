"""
Markers tag tests with metadata that pytest (or its plugins) can act on. The
most common ones:

- `@pytest.mark.skip` - never run this test (with a documented reason).
- `@pytest.mark.skipif` - skip only under a given condition.
- `@pytest.mark.xfail` - run it, but expect it to fail; doesn't break the
  suite, and flips to a loud failure ("XPASS") if it starts passing unnoticed.
- custom markers, e.g. `@pytest.mark.slow`, let you select subsets of the
  suite with `pytest -m slow` / `pytest -m "not slow"`. Register custom
  markers in pytest.ini (see this folder's pytest.ini) so pytest doesn't warn
  about typos.
"""

import sys

import pytest

from calculator import divide


@pytest.mark.skip(reason="not implemented yet - tracked in TICKET-123")
def test_divide_rounds_to_two_decimal_places():
    assert divide(1, 3) == 0.33


@pytest.mark.skipif(sys.version_info < (3, 12), reason="requires Python 3.12+")
def test_divide_runs_on_modern_python():
    assert divide(10, 2) == 5


@pytest.mark.xfail(reason="divide() intentionally raises instead of returning inf")
def test_divide_by_zero_returns_infinity():
    assert divide(1, 0) == float("inf")


@pytest.mark.slow
def test_a_slow_integration_style_check():
    # Run only the slow suite with: pytest -m slow
    # Skip it with:                 pytest -m "not slow"
    total = sum(divide(i, 1) for i in range(1000))
    assert total == sum(range(1000))
