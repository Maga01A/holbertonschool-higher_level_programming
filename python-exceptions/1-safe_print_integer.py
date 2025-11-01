#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer value safely.
    Args:
        value: The value to be printed.
    Returns:
        bool: True if the value is an integer and printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False