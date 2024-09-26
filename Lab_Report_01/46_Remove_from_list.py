'''
Remove an Element from a List in Python
=======================================
Author : Tawfek
Date   : 26-09-2024

'''

my_list = [1, 2, 3, 4, 5]
element = 3

my_list.remove(element)

print(my_list)  # Output: [1, 2, 4, 5]


my_list = [1, 2, 3, 4, 5]
element = 3

if element in my_list:
    my_list.remove(element)

print(my_list)  # Output: [1, 2, 4, 5]



my_list = [1, 2, 3, 4, 5]
index = 2

del my_list[index]

print(my_list)  # Output: [1, 2, 4, 5]