#!/usr/bin/python3


# how do I receive arguments froms another funciton in python?
def safe_print_list(my_list=[], items_qty=0):
    for i in range(items_qty):
        # end="" doesn´t print a new line
        print("{}".format(my_list[i]), end="")
    # print a new line at the end of the loop
    print()
    return i
