#!/usr/bin/python3
"""function to read and print the contents of a UTF-8 text file."""


def read_file(filename=""):
    """Reads a UTF-8 encoded text file and prints its contents
    to the standard output (stdout)."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
