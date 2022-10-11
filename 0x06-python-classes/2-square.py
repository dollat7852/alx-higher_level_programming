#!/usr/bin/python3


def class Square:

    def __init__(self, size=0):

        """ check whether size is of type int and greater than zero (0)"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
