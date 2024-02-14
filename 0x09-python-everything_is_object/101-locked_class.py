#!/usr/bin/python3
"""Defines a LockedClass with restricted attribute creation."""


class LockedClass:
    """
    Defines a class with limited attribute creation.

    Attributes:
        first_name (str): The first name attribute.
    """

    __slots__ = ('first_name',)

    def __init__(self):
        """Initializes LockedClass instances."""
        self.first_name = "first_name"
