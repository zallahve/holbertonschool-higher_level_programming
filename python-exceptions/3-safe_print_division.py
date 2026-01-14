#!/usr/bin/python3
"""Integers division with debug."""


def safe_print_division(a, b):
    """Divide two integers, print result in finally, and return it."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
