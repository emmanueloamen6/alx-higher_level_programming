#!/usr/bin/python3

def safe_print_division(a, b):
    """
    divides two integers and prints the result
    catches divide by zero exception
    """
    try:
        value = a / b
    except:
        value = None
    finally:
        print("Inside result: {}".format(value))
    return (value)
