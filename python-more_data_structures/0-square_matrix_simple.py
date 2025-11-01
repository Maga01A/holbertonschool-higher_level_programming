#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.
    Args:
        matrix (list of lists): A 2D matrix of integers.
    Returns:
        list of lists: A new matrix with the square value of each
        integer of the input matrix.
    """
    return [[j ** 2 for j in i] for i in matrix]
