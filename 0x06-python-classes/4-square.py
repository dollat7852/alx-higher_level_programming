#!/usr/bin/python3

"""Defining a class square"""


class Square:
    """ Class definition"""

    def __init__(self, size=0):
        """ instantiation of the class

        Args:
        param size (int): the size of the square

        """
        """ check whether size is of type int and greater than zero (0)"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

        @property
    def size(self):
        """" getter method for private properties"""
        return (self.__size)

    """" setter method for private property """
    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        """ Return the area of a square"""
        return(self.__size**2)
