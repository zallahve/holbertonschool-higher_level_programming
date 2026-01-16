#!/usr/bin/python3
"""Write a string to a UTF-8 text file and return char count."""


def write_file(filename="", text=""):
    """Write `text` to `filename` (UTF-8), overwriting existing content."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
