VEHICLE_TYPES = ["vw", "bmw", "tesla"]
VEHICLE_COLORS = ["black", "red", "blue"]


def read_vehicle_type() -> str:
    vehicle_type = ""
    while vehicle_type not in VEHICLE_TYPES:
        vehicle_type = input(
            f"What type of vehicle would you like to rent ({', '.join(VEHICLE_TYPES)})? "
        )
    return vehicle_type


def read_vehicle_color() -> str:
    vehicle_color = ""
    while vehicle_color not in VEHICLE_COLORS:
        vehicle_color = input(
            f"What color vehicle would you like to rent ({', '.join(VEHICLE_COLORS)})? "
        )
    return vehicle_color


def read_rent_days() -> int:
    days = 0
    while days < 1:
        days_str = input(
            "How many days would you like to rent the vehicle? (enter a positive number) "
        )
        try:
            days = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return days


def read_kms_to_drive() -> int:
    km = 0
    while km < 1:
        km_str = input(
            "How many kilometers would you like to drive (enter a positive number)? "
        )
        try:
            km = int(km_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return km


def main() -> None:
    vehicle_type = read_vehicle_type()

    vehicle_color = read_vehicle_color()

    days = read_rent_days()

    kms = read_kms_to_drive()

    print(
        f"You rented a {vehicle_type} vehicle, color {vehicle_color}, for {days} days",
        f"and you're allowed to drive {kms} kilometers.",
    )


if __name__ == "__main__":
    main()
