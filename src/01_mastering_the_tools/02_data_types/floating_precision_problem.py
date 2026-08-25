from enum import StrEnum, auto


class EmployeeType(StrEnum):
    FULL_TIME = "full"
    PART_TIME = auto()
    CONTRACTOR = auto()


def main() -> None:
    sum = 0.1 + 0.1 + 0.1
    expected = 0.3

    full_time_employee = EmployeeType.PART_TIME

    print(f"first emplyee is {full_time_employee}")
    print(f"sum = {sum}, expected = {expected}")
    assert sum == expected


if __name__ == "__main__":
    main()
