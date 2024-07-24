VOWELS = "aeiouAEIOU"


def uppercase(strings: list[str]) -> list[str]:
    return [string.upper() for string in strings]


def remove_vowels(strings: list[str]) -> list[str]:
    return [
        "".join(char for char in string if char not in VOWELS) for string in strings
    ]
