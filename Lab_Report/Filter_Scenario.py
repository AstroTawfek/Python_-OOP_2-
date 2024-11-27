"""
Scenario: You have an array representing product prices, and you need to filter out products that
fall within a certain price range for a sale promotion.

Question:
Given a 1D array of product prices, write code to:
● Use boolean indexing to filter products within a specified price range (e.g., between $20
and $50).
● Display only the filtered prices.
Demonstrate the filtering with a sample price array.

"""


import numpy as np

# Sample array of product prices
prices = np.array([10, 25, 30, 45, 60, 15, 50, 75, 20, 40])

# Define the price range
lower_bound = 20
upper_bound = 50

# Use boolean indexing to filter prices within the specified range
filtered_prices = prices[(prices >= lower_bound) & (prices <= upper_bound)]

# Display the filtered prices
print("Filtered prices within the range $20 to $50 :")
print(filtered_prices)