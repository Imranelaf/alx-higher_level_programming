#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = []
    for line in matrix:
        sqr.append([p**2 for p in line])
    return sqr
