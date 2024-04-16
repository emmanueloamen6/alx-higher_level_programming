#!/usr/bin/python3
"""Define the tex reading function."""


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
