#!/usr/bin/python3

def safe_print_integer(value):
    """Print integer with new line.

    Args:
        value(int): integer to be printed
    Returns:
        if except IndexError or ValueError return
        true or flase.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (IndexError, ValueError):
        return (False)
