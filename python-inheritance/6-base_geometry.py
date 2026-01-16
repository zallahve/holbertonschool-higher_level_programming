#!/usr/bin/python3
"""Defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Geometry base class."""

    def area(self):
        """Raise an exception since area is not implemented."""
        raise Exception("area() is not implemented")
