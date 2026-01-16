#!/usr/bin/python3
"""Defines BaseGeometry with area and integer validation."""


class BaseGeometry:
    """Geometry base class."""

    def area(self):
        """Raise an exception since area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an int > 0."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
