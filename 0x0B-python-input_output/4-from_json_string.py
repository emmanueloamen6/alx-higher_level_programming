#!/usr/bin/python3
"""Define a function of Python object JSON.
"""
import json

def from_json_string(my_str):
    """Represent an object (Python data structure) to JSON string.
    """
    return json.loads(my_str)
