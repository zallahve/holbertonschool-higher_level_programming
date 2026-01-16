#!/usr/bin/python3
"""Define a Student class with JSON serialization and reloading."""


class Student:
    """Represent a student with basic attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the instance.

        If `attrs` is a list of strings, only keys in `attrs` are returned
        (and only if they exist). Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the instance using the given dict."""
        for key, value in json.items():
            setattr(self, key, value)
