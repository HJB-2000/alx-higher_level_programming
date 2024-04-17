#!/usr/bin/python3
"""function for writing text to a UTF-8 encoded file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and
    return the number of characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
