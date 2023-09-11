#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """rebel version of an integer, perfect for opposite day!"""
    def __new__(cl, *args, **kargs):
        """create a new instance of the class"""
        return super(MyInt, cl).__new__(cl, *args, **kargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
