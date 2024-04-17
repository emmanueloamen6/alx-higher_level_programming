#!/usr/bin/python3
"""Define a BaseGeometry class."""


class BaseGeometry:
    """Raise an exception."""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validate value."""
        if type(value) != int:
            raise TypeError(name + "must be an integer")
        if value <= 0:
            raise ValueError(name + "must be greater than 0")
