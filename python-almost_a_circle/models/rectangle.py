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

        Base.__init__(self, id)

    @property
    def width(self):
        """Return the value of width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Update the value of width"""
        self.__width = value

    @property
    def height(self):
        """Return the value of height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Update the value of height"""
        self.__height = value

    @property
    def x(self):
        """Return the value of x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Update the value of x"""
        self.__x = value

    @property
    def y(self):
        """Return the value of y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Update the value of y"""
        self.__y = value