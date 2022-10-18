#!/usr/bin/python3
""" Module that add two integers/floats together and returns interger"""

def add_integer(a, b=98):
    """This function adds two numbers together
        it has a default values of zero
        it takes only float/int and raise typeError otherwise
        It only returns int
        @args:
        a(int): first argument
        b(int): second argument
        """
        if type(a) is not int and type(a) is not int:
            raise TypeError("a must be an integer")
        if type(b) is not int and type(b) is not int:
            raise TypeError("b must be an integer")
        return int(a) + int(b)
