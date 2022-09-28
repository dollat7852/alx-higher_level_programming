#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = max(a_dictionary.values())
    for k in a_dictionary:
        if a_dictionary(k) == best:
            return k
