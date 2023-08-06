#!/usr/bin/python3
"""A module for a class Square which is subclass of Rectangle"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """This is the class which inherits Rectangle class"""

    def __init__(self, size):
        """A initial method"""
        self.__size = size

        Rectangle.integer_validator(self, "size", self.__size)

    def area(self):
        """Square Area"""

        return self.__size ** 2

    def __str__(self):
        """method to specify how the object should be
        displayed when using the print() function."""

        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
