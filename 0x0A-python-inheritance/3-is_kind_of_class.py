#!/usr/bin/python3
"""
modul that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""
    return True if isinstance(obj, a_class) else False
