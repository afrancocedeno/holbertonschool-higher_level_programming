#!/usr/bin/python3


# how do I receive arguments froms another funciton in python?
def safe_print_list(my_list=[], x=0):
    items_give = 0
    for i in range(x):
        try:
            # end="" doesn´t print a new line
            print("{}".format(my_list[i]), end="")
        # not specifying the exception will consider all expressions
        except:
            # stop the loop
            break
        items_give += 1
    # print a new line at the end of the loop
    print()
    return items_give
