#!/usr/bin/python3
"""a class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """method for calculated area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if a num is integer"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
