#!/usr/bin/python3
"""
this module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """returns True if the obj is exact class a_class, otherwise False"""
    return (type(obj) == a_class)
