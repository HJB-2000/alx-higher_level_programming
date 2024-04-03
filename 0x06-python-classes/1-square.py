#!/usr/bin/python3

"""
This module defines a Square class with a constructor.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
