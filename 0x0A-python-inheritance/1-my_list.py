#!/usr/bin/python3
"""Module for Mylist class"""


class mylist(list):
    '''Subclass of list'''
    def print_sorted(self):
        '''Method that print sorted list'''
        print(sorted(self))
