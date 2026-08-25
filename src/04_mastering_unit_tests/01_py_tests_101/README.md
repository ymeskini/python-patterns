# Pytest 101

Small, runnable examples covering the pytest fundamentals: plain `assert`,
fixtures, parametrization, exceptions, mocking, and markers.

## Files

- `calculator.py`, `shopping_cart.py`, `notifications.py` - the code under test.
- `conftest.py` - fixtures shared across every test file in this folder.
- `test_basics.py` - naming conventions, Arrange-Act-Assert, plain `assert`.
- `test_parametrize.py` - `@pytest.mark.parametrize` to cover many cases without duplicating tests.
- `test_fixtures.py` - fixtures, fixture composition, `yield` fixtures (setup/teardown), fixture scope, the built-in `tmp_path` fixture.
- `test_exceptions.py` - `pytest.raises` and `match`.
- `test_mocking.py` - `unittest.mock.Mock` and `monkeypatch` to isolate code from external dependencies.
- `test_markers.py` - `skip`, `skipif`, `xfail`, and a custom `slow` marker.
- `pytest.ini` - registers the custom `slow` marker.

## Running

From the repo root:

```bash
uv run pytest src/04_mastering_unit_tests/01_py_tests_101
```

Only the slow-marked tests:

```bash
uv run pytest src/04_mastering_unit_tests/01_py_tests_101 -m slow
```

Verbose, showing each parametrized case:

```bash
uv run pytest src/04_mastering_unit_tests/01_py_tests_101 -v
```

## Best practices demonstrated

1. Name tests for the behaviour they verify, not the implementation.
2. One logical assertion (one behaviour) per test.
3. Use fixtures instead of copy-pasted setup, and `yield` fixtures for teardown.
4. Use `parametrize` instead of looping inside a test or duplicating near-identical tests.
5. Assert on the specific exception type (and message) you expect, not just "it raised something".
6. Isolate unit tests from external systems with test doubles (`Mock`, `monkeypatch`).
7. Register custom markers so `pytest -m` stays discoverable and typo-free.
