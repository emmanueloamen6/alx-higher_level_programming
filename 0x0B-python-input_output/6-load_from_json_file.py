#!/usr/bin/python3
"""Define JSON file reading function."""

import json
def load_from_json_file(filename):
    """Creates a python file from JSON file."""
    with open(filename) as f:
        return json.load(f)
