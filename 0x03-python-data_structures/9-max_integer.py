#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        number = my_list[0]
        for i in my_list:
            if i > number:
                number = i
        return number
    return None
