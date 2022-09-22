#!/usr/bin/python3
import hidden_4 as h

if __name__ == '__main__':
    names =  dir(h)
    for name in names:
        if name.startswith('__'):
            continue
        print(name)
