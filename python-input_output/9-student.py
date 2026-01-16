#!/usr/bin/python3
"""Define a Student class."""


class Student:
    """Represent a student with basic attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of this Student."""
        return self.__dict__
