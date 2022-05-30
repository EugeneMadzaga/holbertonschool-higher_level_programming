#!/usr/bin/python3
"""4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """ Function return True/False if obj is an instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
