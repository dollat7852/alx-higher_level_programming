#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    dic = sorted(a_dictionary)
    for k in dic.keys():
        print("{:s}: {}".format(k, dic[k]))
