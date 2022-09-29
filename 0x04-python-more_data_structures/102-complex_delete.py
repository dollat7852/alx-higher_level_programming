#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None
    del_key = None
    keys = tuple(a_dictionary.keys())
    for key in keys:
        if a_dictionary[key] == value:
            del(a_dictionary[key])
    return a_dictionary
