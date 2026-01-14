#!/usr/bin/python3
"""Safe printing of an integer."""


def safe_print_integer(value):
    """Print value as an int with "{:d}".format().

    Return True if printed, otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
