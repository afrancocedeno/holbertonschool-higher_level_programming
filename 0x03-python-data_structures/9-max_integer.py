#!/usr/bin/python3
def max_integer(my_list=[]):
    number = 0
    if my_list:
        for i in my_list:
            if i > number:
                number = i
        return number
    return None
