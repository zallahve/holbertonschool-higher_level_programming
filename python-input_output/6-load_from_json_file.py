#!/usr/bin/python3
"""Create a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Return the Python object represented by the JSON file `filename`."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
