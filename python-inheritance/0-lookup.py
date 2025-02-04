#!/usr/bin/python3
"""Module that defines the lookup."""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object

    Returns:
        list: The list
    """
    return dir(obj)
