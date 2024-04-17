#!/usr/bin/python3
""" function converts a Python object into its
JSON representation as a string."""


import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the input object as a string.
    """
    return json.dumps(my_obj)
