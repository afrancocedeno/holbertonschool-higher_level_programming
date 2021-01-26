#!/usr/bin/python3
"""Not allowed to use str.upper() module
"""


def uppercase(str):
    for i in list(str):
        if 97 <= ord(i) <= 122:
            print("{:s}".format(chr(ord(i) - 32)), end="")
        else:
            print("{:s}".format(i), end="")
    print()
