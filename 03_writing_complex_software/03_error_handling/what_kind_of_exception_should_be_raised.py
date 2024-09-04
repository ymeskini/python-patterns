import os


# Lower level io operations
def read_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with open(file_path, "r") as file:
            data = file.read()
        if not data:
            raise IOError("File is empty.")
        return data
    except IOError as e:
        raise IOError(f"Error reading file: {e}")


# Lower level arithmetic operations
def calculate_average(numbers: list[int | float]) -> float:
    if len(numbers) == 0:
        raise ValueError("The list of numbers cannot be empty.")

    return sum(numbers) / len(numbers)


def process_data_file(file_path: str):
    data = read_file(file_path)
    numbers = [float(num) for num in data.split()]
    average = calculate_average(numbers)
    print(f"Average of numbers in the file: {average}")


def main() -> None:
    # Assuming data.txt is a valid file with numbers
    process_data_file("data.txt")

    # This will trigger a FileNotFoundError
    process_data_file("invalid_file.txt")  # This will trigger a FileNotFoundError

    # This will trigger a ValueError for empty file
    process_data_file("empty.txt")

    # This will trigger a ValueError for invalid content
    process_data_file("invalid_data.txt")


if __name__ == "__main__":
    main()
