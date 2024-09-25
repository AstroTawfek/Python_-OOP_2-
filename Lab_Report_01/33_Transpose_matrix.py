'''
Python Program to Transpose a Matrix
=====================================
Author : Tawfek
Date   : 25-09-2024

'''

A = [[5, 4, 3], 
     [2, 4, 6],  
     [4, 7, 9], 
     [8, 1, 3]]

A_transpose = list(map(list, zip(*A)))
for x in A_transpose :
    print(x)

"""   or   """

def tr(A):
    print()
    A_transpose=[]
    for i in range(len(A[0])):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        A_transpose.append(row)
    for x in A_transpose :
        print(x)

tr(A)