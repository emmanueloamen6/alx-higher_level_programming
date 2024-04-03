#!/usr/bin/python3

def safe_print_division(a, b):
    """Function that divides 2 integers and prints the result.

    Args:
        a (int): first integer.
        b (int): Second integer.

    Return:
        return the value.
    """
    try:
        value = a / b
    except:
        value = None
    finally:
        print("Inside result: {}".format(value))
    return (value)
