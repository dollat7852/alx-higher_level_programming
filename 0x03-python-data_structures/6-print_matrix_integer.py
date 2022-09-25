#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        fmt = " ".join(["{:d}".format(i) for i in row])
        print(fmt.format(*row))
