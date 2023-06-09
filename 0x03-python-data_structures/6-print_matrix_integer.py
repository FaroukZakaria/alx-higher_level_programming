#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return(None)
    for row in matrix:
        for i in row:
            if i != row[-1]:
                print(i, end=" ")
            else:
                print(i)
