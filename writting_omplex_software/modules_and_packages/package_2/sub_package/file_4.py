# from package_2.file_3 import file_3_function # This is a absolute import
from ..file_3 import file_3_function  # This is a relative import


def file_4_function():
    file_3_function()
    print("package_2.file_4_function")
