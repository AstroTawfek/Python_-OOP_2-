'''
Python Program to Add Two Matrices
=====================================
Author : Tawfek
Date   : 25-09-2024

'''

def add_matrices(matrix1, matrix2):

    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    # Checking if the matrices can be added
    if rows_matrix1 != rows_matrix2 or cols_matrix1 != cols_matrix2:
        return "Matrices cannot be added"

    result_matrix = [[0 for _ in range(cols_matrix1)] for _ in range(rows_matrix1)]

    for i in range(rows_matrix1):
        for j in range(cols_matrix1):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return result_matrix


# Example usage
matrix1 = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]

matrix2 = [[10, 11, 12], 
           [13, 14, 15], 
           [16, 17, 18]]

result = add_matrices(matrix1, matrix2)
print(result)