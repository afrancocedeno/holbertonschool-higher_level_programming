#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    items_give = 0
    for i in range(x):
        try:
            # print only integers {:d}
            print("{:d}".format(my_list[i]), end="")
            items_give += 1
        except:
            continue
    print()
    return items_give
