#!/usr/bin/python3
def remove_char_at(str, n):
    counter = 0
    new_str = ""
    for i in str:
        if counter != n:
            new_str += i
        counter += 1
    return(new_str)
