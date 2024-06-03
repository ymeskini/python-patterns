from src.package_2.example import times_2


def test_times_2_integer_negative():
    # Test case 4: value is a negative integer
    value = -10
    expected_result = -20.0
    assert times_2(value) == expected_result


def test_times_2_float_negative():
    # Test case 5: value is a negative float
    value = -3.14
    expected_result = -6.28
    assert times_2(value) == expected_result


def test_times_2_large_integer():
    # Test case 6: value is a large positive integer
    value = 1000000
    expected_result = 2000000.0
    assert times_2(value) == expected_result


def test_times_2_large_float():
    # Test case 7: value is a large positive float
    value = 9999.99
    expected_result = 19999.98
    assert times_2(value) == expected_result
