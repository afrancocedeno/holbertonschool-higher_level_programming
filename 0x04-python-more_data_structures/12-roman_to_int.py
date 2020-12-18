#!/usr/bin/python3
def roman_to_int(roman_string):
    n_dictionary = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    while i < len(roman_string):
        if roman_string[i] in n_dictionary:
            total += n_dictionary[roman_string[i]]
        i += 1
    return total
