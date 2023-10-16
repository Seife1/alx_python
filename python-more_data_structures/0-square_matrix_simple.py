#!/usr/bin/python3
"""A function that computes the square value of all integers of a matrix"""

def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        row_square = map(lambda x: x**2, row)
        square_matrix.append(list(row_square))
    return square_matrix