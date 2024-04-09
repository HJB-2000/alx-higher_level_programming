#!/usr/bin/python3
"""Defines a class Rectangle that represents a rectangle."""


class Rectangle:
    """Represents a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiates a rectangle with optional width and height."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Returns a string representation of the rectangle using the
        specified print character."""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for _ in range(self.__height):
            result += "".join(
                [str(self.print_symbol) for _ in range(self.__width)]
            ) + "\n"
        return result[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Decreases the count of instances of Rectangle and prints
        a farewell message upon deletion."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
