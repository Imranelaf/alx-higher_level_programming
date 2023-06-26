#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
     '''Prints an integer using "{:d}".format().

    Args:
        value (int): The value to print as an integer.
    Returns:
        True if the value is successfully printed as an integer,
        False otherwise. If an error occurs, the error message
        is printed to stderr preceded by "Exception:".
    '''
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
