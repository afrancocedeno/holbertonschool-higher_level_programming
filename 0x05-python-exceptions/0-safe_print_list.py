#!/usr/bin/python3


# how do I receive arguments froms another funciton in python?
def safe_print_list(my_list=[], items_qty=0):
    for i in range(items_qty):
        try:
            # end="" doesn´t print a new line
            print("{}".format(my_list[i]), end="")
        except:
            # stop the loop
            break
    # print a new line at the end of the loop
    print()
    return items_qty
