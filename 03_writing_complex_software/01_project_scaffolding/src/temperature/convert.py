from enum import StrEnum
from typing import Callable


class TemperatureScale(StrEnum):
    CELSIUS = "C"
    FAHRENHEIT = "F"


TempatureMapper: dict[TemperatureScale, Callable[[int | float], int | float]] = {
    TemperatureScale.CELSIUS: lambda x: (x - 32) * 5.0 / 9.0,
    TemperatureScale.FAHRENHEIT: lambda x: (x * 9.0 / 5.0) + 32,
}


def convert_temperature(value: int | float, to_scale: TemperatureScale) -> float:
    return TempatureMapper[to_scale](value)
