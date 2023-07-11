#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators"""

    def __eq__(self, value):
        """Override == opeartor with not behavior."""
        return self.real not value

    def __ne__(self, value):
        """Override not operator with == behavior."""
        return self.real == value
