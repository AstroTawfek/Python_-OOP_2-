'''
Question 3. List
You are developing a Python script to manage a customer database for an online store. The
customers are stored in lists, and you need to perform several operations on these lists as the
store grows. Consider the following list of customer names:
customers = ["Alice", "Bob", "Charlie", "David", "Eve"]
As part of the database management system, you need to:
   a. Access the third customer in the list and print their name.
   b. Change the name of the second customer to "Ben".
   c. Add a new customer named "Frank" to the end of the list.
   d. Remove the customer "David" from the list.
   e. Sort the customer names alphabetically and print the final list.
Write a Python program that performs these operations and produces the expected final list.
'''

# Defining the list of customers
customers = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(customers)

# Accessing the third customer in the list and print their name
print(customers[2])  # Output: Charlie

# Changing the name of the second customer to "Ben"
customers[1] = "Ben"
print(customers)    # Output: ['Alice', 'Ben', 'Charlie', 'David', 'Eve]

# Adding a new customer named "Frank" to the end of the list
customers.append("Frank")
print(customers)
# Output: ['Alice', 'Ben', 'Charlie', 'David', 'Eve', 'Frank']

# Removing the customer "David" from the list
customers.remove("David")
print(customers)

# Sorting the customer names alphabetically and print the final list
customers.sort()
print(customers)