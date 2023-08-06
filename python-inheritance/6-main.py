#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle
BaseGeometry = __import__('5-base_geometry').BaseGeometry


r = Rectangle(3, 5)

print(r)
print(r.area())
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(-4, "4")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

print(issubclass(Rectangle, BaseGeometry))