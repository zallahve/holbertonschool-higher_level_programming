#!/usr/bin/python3
"""Print and count integers from a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list, but only integers.

    Non-integers are skipped silently.
    If x is bigger than the list length, IndexError is expected.
    Returns the number of integers printed.
    """
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            pass

    print()
    return count
