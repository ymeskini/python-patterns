from src.temperature.convert import convert_temperature, TemperatureScale


def test_convert_celsius_to_fahrenheit():
    assert convert_temperature(0, TemperatureScale.FAHRENHEIT) == 32
    assert convert_temperature(100, TemperatureScale.FAHRENHEIT) == 212
    assert convert_temperature(-40, TemperatureScale.FAHRENHEIT) == -40


def test_convert_fahrenheit_to_celsius():
    assert convert_temperature(32, TemperatureScale.CELSIUS) == 0
    assert convert_temperature(212, TemperatureScale.CELSIUS) == 100
    assert convert_temperature(-40, TemperatureScale.CELSIUS) == -40
