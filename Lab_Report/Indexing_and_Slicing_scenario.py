"""
Scenario: You have a 2D NumPy array representing sales data, where each row is a product, and
columns represent sales over several months. You need to analyze sales for specific months and
products.

Question:
Given a 2D array of sales data, write code to extract :
● Sales data for the first three products.
● Sales data for all products in the last two months.
● Sales data for a specific product and month (e.g., 2nd product in the 4th month).
Demonstrate these operations on a sample 2D array.

"""


import numpy as np

# Sample 2D array representing sales data
# Rows represent products, and columns represent sales over several months
sales_data = np.array([
    [100, 150, 200, 250],  # Product 1 sales
    [80, 120, 160, 200],   # Product 2 sales
    [90, 110, 130, 170],   # Product 3 sales
    [70, 90, 110, 140],    # Product 4 sales
    [60, 80, 100, 120]     # Product 5 sales
])

# 1. Sales data for the first three products
first_three_products = sales_data[:3, :]
print("Sales data for the first three products :")
print(first_three_products)

# 2. Sales data for all products in the last two months
last_two_months = sales_data[:, -2:]
print("\nSales data for all products in the last two months :")
print(last_two_months)

# 3. Sales data for a specific product and month (e.g., 2nd product in the 4th month)
specific_product_month = sales_data[1, 3]  # 2nd product (index 1) in the 4th month (index 3)
print("\nSales data for the 2nd product in the 4th month :")
print(specific_product_month)