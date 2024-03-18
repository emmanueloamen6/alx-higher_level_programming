#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in range(len(matrix)):
        for n in range(len(matrix[arr])):
                print("{:d}".format(matrix[arr][n]), end="")
                if n != (len(matrix[arr]) - 1):
                    print(" ", end="")

        print("")
