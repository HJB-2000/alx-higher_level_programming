#!/usr/bin/python3
"""This function converts a JSON string into a
Python object (data structure)."""
import json


def from_json_string(my_str):
    """
    Return the Python object represented by a JSON string.

    Args:
        my_str: The JSON string to be converted to a Python object.

    Returns:
        object: The Python object represented by the input JSON string.
        """
    return json.loads(my_str)
