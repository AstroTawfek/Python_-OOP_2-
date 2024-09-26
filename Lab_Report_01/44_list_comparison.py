'''
How to compare two lists in Python
===================================
Author : Tawfek
Date   : 26-09-2024

'''

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # Output: True

list1 = [1, 2, 3]
list2 = [3, 2, 1]
print(list1 == list2)  # Output: False

list1 = [1, 2, 3]
list2 = [3, 2, 1]
print(set(list1) == set(list2))  # Output: True

list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]
print(set(list1).issubset(list2))  # Output: True

list1 = [1, 2, 3]
list2 = [1, 2, 4]
for a, b in zip(list1, list2):
    print(a == b, end="  ")  # Output: True, True, False