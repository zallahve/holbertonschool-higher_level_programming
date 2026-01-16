#!/usr/bin/python3
"""Return the dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """Return a dict of an object's serializable attributes."""
    return obj.__dict__
