from app.src.temperatur.convert import TemperatureScale, convert_temperature


def main() -> None:
    convert_temperature(32, TemperatureScale.CELSIUS)
    print("Hello World!")


if __name__ == "__main__":
    main()
