#!/usr/bin/python3
"""
Module with class MyList
"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    pass

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(list(self)))
