from package_3.sub_package_2.file_6 import *  # noqa: F403
from package_2.file_3 import *  # noqa: F403


def main() -> None:
    duplicate_function()  # noqa: F405


if __name__ == "__main__":
    main()
