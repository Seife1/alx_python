#!/usr/bin/python3
"""A module fon an empty class"""


class HideInitSubclassMeta(type):
    def __dir__(cls):
        dir_list = super().__dir__()
        return [attr for attr in dir_list if attr != '__init_subclass__']
    
class MyBaseClass(metaclass=HideInitSubclassMeta):
    def __dir__(self):
        return [attr for attr in dir(self.__class__) if attr != '__init_subclass__']

class BaseGeometry(MyBaseClass):
    pass