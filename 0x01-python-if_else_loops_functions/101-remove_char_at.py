#!/usr/bin/python3
def remove_char_at(str, n):
    counter = 0
    new_str = ""
    for i in str:
        counter += 1
        if counter != n:
            new_str += i
    return(new_str)
