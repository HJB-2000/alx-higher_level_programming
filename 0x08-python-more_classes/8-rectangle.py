#!/usr/bin/python3

"""
Defines a class Rectangle that represents a rectangle
"""


class Rectangle:
    """
    Represents a rectangle
    """
    count_instances = 0
    print_character = "#"

    def __init__(self, width=0, height=0):
        """
        Instantiates a rectangle with optional width and height
        """
        self.width = width
        self.height = height
        type(self).count_instances += 1

    @property
    def width(self):
        """
        Retrieves the width
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rectangle_1, rectangle_2):
        """
        Compares two rectangles and returns the one with the larger area
        """
        if type(rectangle_1) is not Rectangle:
            raise TypeError("rectangle_1 must be an instance of Rectangle")
        if type(rectangle_2) is not Rectangle:
            raise TypeError("rectangle_2 must be an instance of Rectangle")
        if rectangle_1.area() >= rectangle_2.area():
            return rectangle_1
        else:
            return rectangle_2

    def area(self):
        """
        Calculates and returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle using
        the specified print character
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = []
        for _ in range(self.__height):
            line = "".join(
                [str(self.print_character) for _ in range(self.__width)]
            )
            lines.append(line)
        return "\n".join(lines)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
       """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Decreases the count of instances of Rectangle and prints
        a farewell message upon deletion
        """
        type(self).count_instances -= 1
        print("Bye rectangle...")
