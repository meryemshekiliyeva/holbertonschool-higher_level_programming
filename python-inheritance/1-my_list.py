#!/usr/bin/python3
"""This module."""


class MyList(list):
    """
    a class MyList that inherits from list


    Methods
    -------
    print_sorted():
        Prints thr list
    """
    def print_sorted(self):
        """Returns a new list"""
        print(sorted(self))
        return sorted(self)
