#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    if l == 1:  # somthing that saves the number of arguments
        print("{:d} arguments.".format(l - 1))
    elif l == 2:  # somthing that saves the number of arguments
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{:d} arguments:".format(l - 1))
        arg_number = 1
        for i in argv:  # from the first argument till the last
            if i != argv[0]:  # not valid != 0
                print("{}: {}".format(arg_number, i))
                arg_number += 1
