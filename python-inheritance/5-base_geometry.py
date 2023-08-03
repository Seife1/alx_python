#!/usr/bin/python3
"""A module for an empty class"""


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
    """A function to raise an exeption"""
    def area(self):
        raise Exception ("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))