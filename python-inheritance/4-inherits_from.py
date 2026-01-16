#!/usr/bin/python3
"""Check if an object is an instance of a subclass of a given class."""


def inherits_from(obj, a_class):
    """Return True if obj is instance of a subclass of a_class, else False."""
    return isinstance(obj, a_class) and type(obj) is not a_class
