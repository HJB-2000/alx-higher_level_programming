#!/usr/bin/python3
"""Square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize Square with a size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
