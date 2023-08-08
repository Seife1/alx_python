#!/usr/bin/python3
"""A module which have a class Square that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("width must be an integer")
        if self.__size <= 0:
            raise ValueError("width must be > 0")
        self.__x = x
        self.__y = y
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def width(self):
        """Return the value of width"""
        return self.__width
    
    @width.setter
    def width(self, width):
        """Update the value of width"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    

    def __str__(self):
        """method to specify how the object should be displayed when using the print() function."""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, self.__size))