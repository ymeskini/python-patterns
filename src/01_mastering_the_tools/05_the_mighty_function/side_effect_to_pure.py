CUSTOMERS = {
    "Alice": {"phone_number": "2341", "credit_card": "2341"},
    "Bob": {"phone_number": "9102", "credit_card": "5342"},
}


type Directory = dict[str, dict[str, str]]


def update_phone_number(customers: Directory, key: str, new_number: str) -> Directory:
    new_customers: Directory = {}
    for k, v in customers.items():
        new_customers[k] = v.copy()

    new_customers[key]["phone_number"] = new_number
    return new_customers


def main() -> None:
    print(f"Before: {CUSTOMERS}")
    new_customers = update_phone_number(CUSTOMERS, "Alice", "1234")
    print(f"After (original): {CUSTOMERS}")
    print(f"After: {new_customers}")


if __name__ == "__main__":
    main()
