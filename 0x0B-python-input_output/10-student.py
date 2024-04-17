#!/usr/bin/python3
"""
Defines a class representing a Student.
"""


class Student:
    """
    Represents a student with basic information.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student.

        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student object.

        If attrs is provided as a list of strings, includes only
        those attributes in the dictionary.

        Parameters:
            attrs (list): (Optional) List of attribute names to
                include in the dictionary.

        Returns:
            dict: A dictionary containing the specified attributes
                of the Student.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
