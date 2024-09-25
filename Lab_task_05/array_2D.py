# Defining a 2D list (or matrix) with 3 rows and 3 columns
a = [
    [1, 2, 3],
    [2, 3, 4],
    [5, 6, 7]
]

# Modifying the element at the second row and first column to 9
a[1][0] = 9

# Printing the matrix using nested for loops
for i in range(3):
    for j in range(3):
        print(a[i][j], end="  ")
    print()

print()  # Printing an empty line for separation

# Printing the matrix again, but this time using a for-each loop
for row in a:
    for column in row:
        print(column, end="  ")
    print()