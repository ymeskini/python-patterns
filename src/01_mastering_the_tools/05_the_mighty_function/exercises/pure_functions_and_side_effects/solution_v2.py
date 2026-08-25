import string
from datetime import datetime

# A fixed lookup table — doesn't change
LOOKUP_TABLE = string.ascii_uppercase + string.digits


def generate_id(length: int, seed: int) -> str:
    result: list[str] = []
    table_len = len(LOOKUP_TABLE)
    for i in range(length):
        # Simple deterministic pseudo-random index based on seed and position
        idx = (seed * (i + 1) + i**2) % table_len
        result.append(LOOKUP_TABLE[idx])
    return "".join(result)


def weekday(date: datetime) -> str:
    return f"{date:%A}"


def main() -> None:
    print(f"Today is a {weekday(datetime.today())}")
    # Using a fixed seed for deterministic output
    seed = 12345
    print(f"Your id = {generate_id(10, seed)}")


if __name__ == "__main__":
    main()
