#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    dic = sorted(a_dictionary)
    for k, v in dic.items():
        print("{}: {}".format(k, v))
