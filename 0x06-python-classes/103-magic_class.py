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

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")  # Raise an exception if the provided radius is not a number

        self.__radius = radius  # Set the radius attribute to the provided value

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)  # Calculate and return the area of the circle

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)  # Calculate and return the circumference of the circle
