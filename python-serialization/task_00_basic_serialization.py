#!/usr/bin/python3
"""Basic JSON serialization and deserialization for Python dictionaries."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to JSON and save it to `filename`."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON from `filename` and return the deserialized dictionary."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
