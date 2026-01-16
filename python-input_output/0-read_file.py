#!/usr/bin/python3
"""Read a text file (UTF-8) and print it to stdout."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
