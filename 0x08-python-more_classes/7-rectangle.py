#!/usr/bin/python3
"""
Defines a class Rectangle that represents a rectangle
"""


class Rectangle:
    """
    Represents a rectangle
    """
    count_instances = 0
    symbol_to_print = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with optional width and height
        """
        self.width = width
        self.height = height
        type(self).count_instances += 1

    @property
    def width(self):
        """
        Getter method for width
        """
        return self.__width

    @property
    def height(self):
        """
        Getter method for height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter method for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter method for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def calculate_area(self):
        """
        Calculates the area of the rectangle
        """
        return self.__width * self.__height

    def calculate_perimeter(self):
        """
        Calculates the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def display(self):
        """
        Displays the rectangle using '#' characters
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join([str(self.symbol_to_print)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __str__(self):
        """
        Returns a string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __repr__(self):
        """
        Returns a string representation of the rectangle for evaluation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a farewell message when an instance of Rectangle is deleted
        """
        type(self).count_instances -= 1
        print("Bye rectangle...")
