#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    list = []

    for i in range(len(matrix)):
        list = matrix[i]
        for j in range(len(list)):
            print(list[j], end=' ')
        print()