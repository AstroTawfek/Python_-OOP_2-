"""
Scenario: 
You have two arrays representing data from two different branches of a store. To
analyze combined sales, you need to merge the data by joining arrays along different axes.

Question:
Given two 1D NumPy arrays representing sales, write code to:
● Join the arrays horizontally to represent two branches as columns.
● Join the arrays vertically to represent two branches as additional rows.
Demonstrate both types of joins and explain in which scenario each type would be useful.

"""


import numpy as np

# Sample sales data for two branches
branch_a_sales = np.array([100, 200, 300])
branch_b_sales = np.array([150, 250, 350])

# Joining arrays horizontally (as columns)
horizontal_join = np.column_stack((branch_a_sales, branch_b_sales))
print("Horizontal Join (as columns) :")
print(horizontal_join)

# Joining arrays vertically (as rows)
vertical_join = np.vstack((branch_a_sales, branch_b_sales))
print("\nVertical Join (as rows) :")
print(vertical_join)