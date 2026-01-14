#!/usr/bin/python3
"""Safe printing of an integer"""


def safe_print_integer(value):
    """Prints value as an integer using "{:d}".format().

    Returns True if printed successfully (value is an integer), otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
