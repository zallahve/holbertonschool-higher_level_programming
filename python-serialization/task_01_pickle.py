#!/usr/bin/python3
"""Pickle serialization/deserialization for a custom class."""
import pickle


class CustomObject:
    """Custom object that can be serialized/deserialized with pickle."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance to `filename`.

        Return None on failure (non-existent path, permission issues, etc.).
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and return an instance from `filename`.

        Return None if the file doesn't exist or is malformed.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
        except Exception:
            return None
        return None
