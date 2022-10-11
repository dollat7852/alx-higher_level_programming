#!/usr/bin/python3


class Square:

    def __init__(self, size=0):

        """ check whether size is of type int and greater than zero (0)"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

        """" getter method for private properties"""
        @property
    def size():
        return (self.__size)

    """" setter method for private property """
    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        """ Return the area of a square"""
        return(self.__size**2)
