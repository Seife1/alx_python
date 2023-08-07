#!/usr/bin/python3
"""A module which have a class Rectangle that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")

        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")

        if type(self.__x) is not int:
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")

        if type(self.__y) is not int:
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")
        
        Base.__init__(self, id)

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

    @property
    def height(self):
        """Return the value of height"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """Update the value of height"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Return the value of x"""
        return self.__x
    
    @x.setter
    def x(self, x):
        """Update the value of x"""

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Return the value of y"""
        return self.__y
    
    @y.setter
    def y(self, y):
        """Update the value of y"""

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y