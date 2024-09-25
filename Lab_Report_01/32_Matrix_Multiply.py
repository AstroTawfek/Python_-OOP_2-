'''
Python Program to Multiply Two Matrices
=============================================
Author : Tawfek
Date   : 25-09-2024

'''

def multiply_matrices(A, B):
    
    num_rows_A = len(A)
    num_cols_A = len(A[0])
    num_rows_B = len(B)
    num_cols_B = len(B[0])

    # Checking if the matrices can be multiplied
    if num_cols_A != num_rows_B:
        return "Matrices cannot be multiplied"

    C = [[0 for _ in range(num_cols_B)] for _ in range(num_rows_A)]

    for i in range(num_rows_A):
        for j in range(num_cols_B):
            for k in range(num_cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C

A = [[5, 4, 3], 
     [2, 4, 6],
     [4, 7, 9]]  
B = [[3, 2, 4],
     [4, 3, 6], 
     [2, 7, 5]]

result = multiply_matrices(A, B)
for row in result:
    print(row)