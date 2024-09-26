"""
Python Program to convert list to
string and vice versa
=================================
Author : Tawfek
Date   : 26-09-2024

"""

def list_to_string(lst):
    return ''.join(str(i) for i in lst)

def string_to_list(s):
    return list(s)

my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

converted_string = list_to_string(my_list)
print("Converted String:", converted_string)

reverted_list = string_to_list(converted_string)
print("Reverted List:", reverted_list)