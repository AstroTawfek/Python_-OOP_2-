"""
Python Program to add two lists
===============================
Author : Tawfek
Date   : 26-09-2024

"""

def add_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")

    result = [x + y for x, y in zip(list1, list2)]
    return result

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = add_lists(list1, list2)
print(result)  # Output: [7, 9, 11, 13, 15]