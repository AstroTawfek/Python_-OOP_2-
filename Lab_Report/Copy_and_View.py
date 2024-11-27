"""
Scenario: 
You have a large dataset in a NumPy array and want to perform operations on a subset
without modifying the original data. You’re unsure whether to use a copy or view.

Question:
Given a 2D array of data, write code to:
● Create a view of a specific row.
● Create a deep copy of a specific column.
● Modify both the view and the copy, and observe which one affects the original array.
Explain the difference in behavior between the copy and view based on your code.

"""


import numpy as np

# Create a sample 2D NumPy array
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Create a view of the second row (index 1)
row_view = data[1]

# Create a deep copy of the first column (index 0)
column_copy = data[:, 0].copy()

# Modify the view (change the second row)
row_view[0] = 10  # This modifies the first element of the second row

# Modify the copy (change the first element of the copied column)
column_copy[0] = 20  # This modifies the first element of the copied column

# Print the original array and the modified view and copy
print("Original array after modifying the view :")
print(data)

print("\nModified row view (not affecting the original) :")
print(row_view)

print("\nModified column copy (not affecting the original) :")
print(column_copy)