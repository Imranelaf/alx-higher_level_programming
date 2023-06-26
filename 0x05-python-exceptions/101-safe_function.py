import sys

def safe_function(fct, *args):
    """
    Safely executes a function with the given arguments, catching any exceptions that may occur.
    
    Args:
    - fct: the function to execute
    - args: the arguments to pass to the function
    
    Returns:
    - the result of the function if it executes successfully
    - None if an exception occurs
    """
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    return result
