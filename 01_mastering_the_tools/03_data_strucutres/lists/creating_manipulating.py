def main() -> None:
    # Creating and manipulating a list of integers
    numbers = [1, 2, 3, 4, 5]
    print("Original List:", numbers)

    # Lists are mutable: elements can be changed
    numbers[0] = 10  # Changing the first element
    print(f"List after changing first element: {numbers}")

    # Accessing elements using their position
    second_element = numbers[1]
    print(f"second_element: {second_element}")

    # Slicing
    first_three = numbers[:3]
    print(f"Fifth three element: {first_three}")
    # Discussing memory management
    # Python lists automatically resize as items are added or removed
    numbers.append(6)
    print(f"List after appending an element: {numbers}")

    # Lists can contain different types of objects
    mixed_list = [1, "Hello", 3.14, [2, 4, 6]]
    print("Mixed Type List:", mixed_list)


if __name__ == "__main__":
    main()
