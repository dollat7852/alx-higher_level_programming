#!/usr/bin/python3
def no_c(my_string):
    filtered = ''
    for x in my_string:
        if x not in 'cC':
            filtered += x
    return (filtered)
