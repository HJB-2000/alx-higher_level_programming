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

    def to_json(self):
        """
        Returns a dictionary representation of the Student object.

        Returns:
            dict: A dictionary containing the attributes of the Student.
        """
        return self.__dict__
