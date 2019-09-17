#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for val in lists:
            print("{:d}".format(val), end='')
            if val != lists[-1]:
                print("".format(), end=' ')
        print()
