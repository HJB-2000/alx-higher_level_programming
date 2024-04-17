#!/usr/bin/python3
"""This function writes a Python object to a text
file using its JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to be serialized to
            JSON and saved to the file.
        filename: The name of the file to save the JSON representation.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
