#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:  # matrix != None
        for i in matrix:
            for j in i[:-1]:
                print("{:d}".format(j), end=" ")
            if i:
                print("{:d}".format(i[-1]))
            else:
                print()
