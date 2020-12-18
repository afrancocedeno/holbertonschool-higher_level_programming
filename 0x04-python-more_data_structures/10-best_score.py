#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maximun_key = max(a_dictionary, key=a_dictionary.get)
        return maximun_key
    return None
