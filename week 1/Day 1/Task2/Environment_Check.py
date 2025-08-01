import sys
import os 


def display_info():

    py_version = sys.version
    current_directory = os.getcwd()

    print(f"Python Version is:",py_version)
    print(f"Your current working directory is:",current_directory)

if __name__ == "__main__" :
    display_info()
