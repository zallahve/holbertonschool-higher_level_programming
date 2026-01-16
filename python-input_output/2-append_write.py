#!/usr/bin/python3
"""Append a string to a UTF-8 text file and return chars added."""


def append_write(filename="", text=""):
    """Append `text` to `filename` (UTF-8) and return number of chars."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
