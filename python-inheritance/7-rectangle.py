#!/usr/bin/python3
"""A module for a class Rectangle which is subclass of BaseGeometer"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A Rectangle class which inherits from BaseGeometry"""
    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        
        self.__width = width
        self.__height = height

        self.integer_validator("height", self.__height)
        self.integer_validator( "width", self.__width)

    def area(self):
        return self.__height * self.__width

    def __dir__(self):
        """Inserting the private attributes of the class into the list"""
        dir_list = super().__dir__()
        dir_list.insert(0, '_Rectangle__width')
        dir_list.insert(0, '_Rectangle__height')
        return dir_list
    
    def __str__(self):
        """method to specify how the object should be displayed when using the print() function."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
