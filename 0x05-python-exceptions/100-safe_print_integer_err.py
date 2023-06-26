#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
     '''Prints an integer using "{:d}".format().

    Attempts to print the provided value as an integer using the
    "{:d}".format() method. If a TypeError or ValueError occurs,
    an appropriate error message is printed to standard error.

    Args:
        value (int): The value to print as an integer.

    Returns:
        bool: True if the value is successfully printed as an integer,
              False otherwise. If an error occurs, the error message
              is printed to stderr preceded by "Exception:".
    '''
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
