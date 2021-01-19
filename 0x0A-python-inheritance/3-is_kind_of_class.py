#!/usr/bin/python3

"""Function that returns True if the object is an instance of,"""
"""or if the object is an instance of a class that inherited from"""
""" otherwise False. """


def is_kind_of_class(obj, a_class):

    """ returns True if the object is an instance, otherwise False"""

    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
