#!/usr/bin/python3
"""
This script defines a class Rectangle to represent a rectangle.
"""


class Rectangle:
    """
    This class represents a rectangle and provides methods for manipulating it.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with specified width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def calculate_area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.__width * self.__height

    def calculate_perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def display(self):
        """
        Displays the rectangle using '#' characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a farewell message when an instance of Rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
