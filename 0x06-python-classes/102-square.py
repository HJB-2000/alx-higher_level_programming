#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int, float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int, float): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int, float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares have equal areas.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two squares have unequal areas.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the areas are unequal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if the area of the current square is less
        than the area of another square.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of the current square is less than or equal
        to the area of another square.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if the area of the current square is greater than
        the area of another square.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of the current square is greater than or equal
        to the area of another square.

        Args:
            other (Square): Another square object.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()
