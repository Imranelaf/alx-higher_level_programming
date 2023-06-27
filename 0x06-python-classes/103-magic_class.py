#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0  # Initialize the radius attribute with a default value of 0

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")  # Raise a TypeError if the provided radius is not a number

        self.__radius = radius  # Set the radius attribute to the provided value

    def area(self):
        """Calculate and return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
