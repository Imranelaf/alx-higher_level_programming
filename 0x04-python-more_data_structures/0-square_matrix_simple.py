#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for line in matrix:
        new_matrix.append([p**2 for p in line])
    return new_matrix
