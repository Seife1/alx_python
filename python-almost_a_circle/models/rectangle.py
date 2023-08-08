#!/usr/bin/python3
"""A module which have a class Rectangle that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")

        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")

        if type(self.__x) is not int:
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")

        if type(self.__y) is not int:
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")
        
        Base.__init__(self, id)

    @property
    def width(self):
        """Return the value of width"""
        return self.__width
    
    @width.setter
    def width(self, width):
        """Update the value of width"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Return the value of height"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """Update the value of height"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Return the value of x"""
        return self.__x
    
    @x.setter
    def x(self, x):
        """Update the value of x"""

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Return the value of y"""
        return self.__y
    
    @y.setter
    def y(self, y):
        """Update the value of y"""

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """To find the area of the rectangle"""
        return self.__width * self.__height
    
    def display(self):
        """A method to display # in row and column"""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
                for x in range(self.__x):
                    print(" ",end="")
                for j in range(self.__width):
                    if j < self.__width - 1:
                        print("#", end="")
                    else:
                        print("#")

    def __str__(self):
        """method to specify how the object should be displayed when using the print() function."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height,))
    
    def update(self, *args):
        """A method that assigns an argument to each attribute """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
