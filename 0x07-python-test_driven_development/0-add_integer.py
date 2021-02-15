#!/usr/bin/python3
def add_integer(a, b=98):
    """add_integer: function that adds 2 integers

    Args:
        a datatype of (int) or (float)

    """

    if not type(a) in (int, float):
        raise TypeError('a must be an integer')
    elif not type(b) in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
