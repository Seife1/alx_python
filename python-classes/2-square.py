#!/usr/bin/python3
""" A module which have a class known as Square. """
class Square:
    """ A class which is used to compute the area of square"""
    def __init__(self, size=0):
        """ defining a funtion to instantiation 
        
            Args:
                size (float): the first parameter
            Returns: 
                Nothing for now    
        """
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError ("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        
    def area(self):
        """ Calculates the area of a square 
            Args:
                No
            Returns:
                area of square.
        
        """
        return self.__size ** 2