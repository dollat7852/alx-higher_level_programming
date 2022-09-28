#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    dic = sorted(a_dictionary)
    for k in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(k, dic[k]))
