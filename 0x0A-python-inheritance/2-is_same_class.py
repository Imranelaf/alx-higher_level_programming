#!/usr/bin/python3
"""
module returns True if the object is exactly an instance of the specified class; otherwise False
"""


def is_same_class(obj, a_class):
    """Method that return True if an object is an instance of a class"""

       return type(obj) is a_class
