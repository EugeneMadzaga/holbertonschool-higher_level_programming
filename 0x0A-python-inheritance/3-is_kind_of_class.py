#!/usr/bin/python3
"""3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """ Function / return True/False if obj is instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
