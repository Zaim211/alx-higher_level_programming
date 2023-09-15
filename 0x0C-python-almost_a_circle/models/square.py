#!/usr/bin/python3
"""
This module contains the "Square" class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
         """Initialize a new Square
        Args:
            size: The size of the new Square
            x: The x coordinate of the new Square
            y: The y coordinate of the new Square
            id: The identity of the new Square
        """
        super().__init__(self, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
