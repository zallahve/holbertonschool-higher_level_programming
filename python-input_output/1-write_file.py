#!/usr/bin/python3
"""Write a string to a text file (UTF-8) and return the number of characters."""


def write_file(filename="", text=""):
    """Writes `text` to `filename` (UTF-8), overwriting existing content."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
