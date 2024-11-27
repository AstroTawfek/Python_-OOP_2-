"""
Scenario: 
You have a 3D array representing data collected from multiple devices over multiple
days, with each device’s daily data stored in a 2D matrix format. You need to process this data as
a single list.

Question:
Given a 3D NumPy array, write code to:
● Flatten the array into a 1D array.
● Explain why flattening might be necessary and what kind of operations it enables.
Demonstrate this operation with a sample 3D array.

"""


import numpy as np

# Create a sample 3D NumPy array (e.g., 2 devices, 3 days, 4 measurements each)
data = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],  # Device 1
    [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]  # Device 2
])

# Flatten the array into a 1D array
flattened_data = data.flatten()

print("Original 3D array :")
print(data)
print("\nFlattened 1D array :")
print(flattened_data)