"""

Scenario: 
You’re working with data that was initially stored as strings in a CSV file and
imported into a NumPy array. Now, you need to convert specific columns to integers or floats to
perform calculations.

Question:
Given a 2D NumPy array with string values, write code to:
● Convert an entire column to integer type if it represents whole numbers (e.g., age data).
● Convert a column to float type if it represents decimal values (e.g., salary or price).
Demonstrate the type casting on a sample NumPy array.

"""


import numpy as np

# Sample 2D NumPy array with string values
data = np.array([
    ['Alice', '25', '50000.50'],
    ['Bob', '30', '60000.00'],
    ['Charlie', '35', '70000.75']
])

# Function to convert columns based on their content
def convert_columns(arr):
    # Convert the second column (age) to integers
    arr[:, 1] = arr[:, 1].astype(int)  # Assuming the second column represents age

    # Convert the third column (salary) to floats
    arr[:, 2] = arr[:, 2].astype(float)  # Assuming the third column represents salary

    return arr

# Convert the columns
converted_data = convert_columns(data)

# Display the converted data and types
print("Converted Data :")
print(converted_data)
print("Data Types :")
print(converted_data.dtype)