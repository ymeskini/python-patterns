# from ..package_3.sub_package_1 import file_5  # This is not allowed
from package_3.sub_package_1 import file_5


def file_1_function():
    print("package_1.file_1_function")
    print(file_5.__name__)


def duplicate_function():
    print("package_1.file_1.duplicated_function")
