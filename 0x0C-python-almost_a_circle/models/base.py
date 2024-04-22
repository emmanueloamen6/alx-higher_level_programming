#!/usr/bin/python3
"""Defines a class Base"""
import json
import os.path
import csv
import turtle

class Base:
    """Class that defines the properties of Base.

    Attributes:
        id (int): Identity of each instance.
    """

    _nd_objects = 0

    def __init__(self, id=None):
        """Creates new instances of Base.

        Args:
            id(int, optional): Identity of each instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base._nd_objects += 1
            self.id = Base._nd_objects
