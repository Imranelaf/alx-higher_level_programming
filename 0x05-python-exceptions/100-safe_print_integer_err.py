#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    """Attempts to print the provided value as an integer using the
    "{:d}".format() method. If a TypeError or ValueError occurs,
    an appropriate error message is printed to standard error"""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):    
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
