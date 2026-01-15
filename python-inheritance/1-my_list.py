#!/usr/bin/python3
"""Defines MyList class that inherits from list."""


class MyList(list):
    """Custom list with a method to print sorted contents."""

    def print_sorted(self):
        """Print the list sorted in ascending order (without modifying it)."""
        print(sorted(self))
