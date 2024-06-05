import module
from package_1.file_2 import file_2_function
from package_2.sub_package.file_4 import file_4_function
from package_3.sub_package_1.file_5 import file_5_function


def main() -> None:
    print(module.VOWELS)
    print(module.__file__)
    print(module.__name__)
    print(module.__package__)
    file_2_function()
    file_4_function()
    file_5_function()


if __name__ == "__main__":
    main()
