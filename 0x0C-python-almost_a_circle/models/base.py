#!/usr/bin/python3

import json
from random import random as rn
from time import sleep

""" This is a base model for the programme"""

class Base():
    """Setting up the structure and  assign  id for instantiated objects"""
    __nb_objects = 0
    def __init__(self, id = None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def validate_size(self, name, val, low=1):
        """Validate sizes of shape"""
        if type(val) != int:
            raise TypeError(f"{name} must be an integer")
         if val < low:
             op = ">" if low else ">="
             raise ValueError(f"{name} must be {op} 0")
