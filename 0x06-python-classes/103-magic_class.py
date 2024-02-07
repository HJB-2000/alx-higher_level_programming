#!/usr/bin/python3
"""
This module defines a MagicClass class.
"""


import math


class MagicClass:
    """
    This class represents a magic circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance.

        Args:
            radius (int, float): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) not in [int, float]:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
