#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """
    Safely executes a function with the given arguments.
    Args:
    - fct: the function to execute
    - args: the arguments to pass to the function
    Returns:
    - the result of the function if it executes successfully
    """
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    return result
