'''
Python Program to remove duplicates from a list
===============================================
Author : Tawfek
Date   : 26-09-2024

'''

def remove_duplicates(input_list):
    return list(set(input_list))

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print("Original List:", my_list)
print("List after removing duplicates:", remove_duplicates(my_list))



def remove_duplicates_ordered(input_list):
    seen = set()
    return [x for x in input_list if not (x in seen or seen.add(x))]

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print("Original List:", my_list)
print("List after removing duplicates (ordered):", remove_duplicates_ordered(my_list))