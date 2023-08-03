#!/usr/bin/python3
""" A module for a function that check if an object is instancec of a specified class"""

def inherits_from(obj, a_class):
    """A function which is used to check class inheritance"""
    return issubclass(type(obj), a_class) and not type(obj) is a_class
