#!/usr/bin/python3
def element_at(my_list, idx):
    l = len(my_list)
    print(l)
    for i in my_list:
        if idx < 0 or idx >= len(my_list):
            return None
        else:
            my_list[idx]
