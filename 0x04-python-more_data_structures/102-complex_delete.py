#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    for key in a_dictionary:
        if a_dictionary[key] == value:
            del(a_dictionary[key])
    return a_dictionary
