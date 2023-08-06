#!/usr/bin/python3
""" Writing the first class Base """

class Base:
    """ This class will be base of all other classes
    in this project. Manage id attribute in all my future class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects