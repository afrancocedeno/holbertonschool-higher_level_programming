#!/usr/bin/python3
"""Not allowed to use str.upper() module
"""


def uppercase(str):
    for i in list(str):
        if 97 <= ord(i) <= 122:
            print(chr(ord(i) - 32), end="")
        else:
            print(i, end="")
    print()
