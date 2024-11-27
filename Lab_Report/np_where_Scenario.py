"""
Scenario: You’re analyzing temperatures recorded over several days. You want to identify days
when the temperature exceeded a certain threshold and replace any low temperatures with a
specified minimum value.

Question:
Given a NumPy array of temperatures, write code to:
● Use np.where to find indices where the temperature exceeds a certain threshold.
● Use np.where to replace temperatures below a certain threshold with a minimum
value.
Demonstrate this operation with a sample temperature array.

"""


import numpy as np

# Sample temperature array (in degrees Celsius)
temperatures = np.array([15, 22, 18, 30, 10, 25, 5, 29, 35, 20])

# Define the threshold and minimum value
threshold = 20
min_value = 10

# Use np.where to find indices where the temperature exceeds the threshold
exceeding_indices = np.where(temperatures > threshold)
print("Indices where temperature exceeds threshold :", exceeding_indices)

# Use np.where to replace temperatures below the minimum value with the minimum value
adjusted_temperatures = np.where(temperatures < min_value, min_value, temperatures)
print("Adjusted temperatures :", adjusted_temperatures)