#!/usr/bin/python3
"""Define a function that write object to text file in Json."""

import json

def save_to_json_file(my_obj, filename):
    """writes an Object to a text file in Json."""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
