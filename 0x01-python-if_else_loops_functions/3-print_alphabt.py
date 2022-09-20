#!/usr/bin/python3

for i in range(97, 97 + 26):
    if f"{i:c}" in ('e', 'q'):
        continue
    print("{ch:c}".format(ch=i), end='')
