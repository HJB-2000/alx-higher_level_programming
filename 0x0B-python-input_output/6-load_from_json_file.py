#!/usr/bin/python3
"""This function loads a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.

    Args:
        filename: The name of the JSON file to load the object from.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
