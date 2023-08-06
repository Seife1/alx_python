#!/usr/bin/python3
"""A module for a class Rectangle which is subclass of BaseGeometer"""


class HideInitSubclassMeta(type):
    """Hide the __init_subclass__ for ..."""
    def __dir__(cls):
        dir_list = super().__dir__()
        return [attr for attr in dir_list if attr != '__init_subclass__']
    
class MyBaseClass(metaclass=HideInitSubclassMeta):
    """Hide the __init_subclass__ for ..."""
    def __dir__(self):
        return [attr for attr in dir(self.__class__) if attr != '__init_subclass__']

class BaseGeometry(MyBaseClass):
    def __init__(self):
        pass
    def area(self):
        """A function to raise an exeption"""
        raise Exception ("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        
        self.__width = width
        self.__height = height

        self.integer_validator("height", self.__height)
        self.integer_validator( "width", self.__width)

    def __dir__(self):
        dir_list = super().__dir__()
        dir_list.insert(0, '_Rectangle__width')
        dir_list.insert(0, '_Rectangle__height')
        return dir_list