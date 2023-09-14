#!/usr/bin/python3
"""Defines a base model class"""


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project
    Attributes:
        __nb_objects: The number of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base
        Args:
            id: The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
