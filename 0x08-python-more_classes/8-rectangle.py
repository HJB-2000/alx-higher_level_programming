#!/usr/bin/python3
"""Defines a class Rectangle representing rectangles."""


class Rectangle:
    """A representation of a rectangle."""
    number_of_instances = 0
    print_symbol = "#"  # The symbol used to represent rectangles in printing.

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance with optional width and height."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the larger area."""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (
            "\n".join(
                ["".join([str(self.print_symbol) for i in range(self.__width)])
                    for j in range(self.__height)]
                ))

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
