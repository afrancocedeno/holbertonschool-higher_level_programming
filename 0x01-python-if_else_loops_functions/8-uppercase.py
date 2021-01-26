#!/usr/bin/python3
"""Not allowed to use str.upper() module
"""


def uppercase(str):
    for i in list(str):
        if 97 <= ord(i) <= 122:
            aux = chr(ord(i) - 32)
        else:
            aux = i
        print("{:s}".format(aux), end="")
    print()
