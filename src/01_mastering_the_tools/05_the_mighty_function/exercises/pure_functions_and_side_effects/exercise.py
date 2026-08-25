import random
import string
from datetime import datetime
from typing import Callable


def generate_id(length: int, generate: Callable) -> str:
    return generate(length)


def weekday(today: datetime) -> str:
    return f"{today:%A}"


def random_string(length: int):
    "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )


def main() -> None:
    print(f"Today is a {weekday(datetime.today())}")
    print(f"Your id = {generate_id(10, random_string)}")


if __name__ == "__main__":
    main()
