#!/usr/bin/python3
Square = __import__('8-square').Square

s = Square(5)
print(s)
print (s.area())


try:
    s = Square("Love")
    print(s)
except Exception as e:
    print ("[{}] {}".format(e.__class__.__name__, e))