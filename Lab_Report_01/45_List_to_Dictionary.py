'''
Python Program to convert list to dictionary
============================================
Author : Tawfek
Date   : 26-09-2024

'''

def convert_list_to_dict(lst):
    """
    Returns:
        dict: A dictionary where the keys are the indices of the list and the values are the corresponding elements.
    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    return {i: elem for i, elem in enumerate(lst)}


my_list = [1, 2, 3, 4, 5]
print(convert_list_to_dict(my_list))  # Output: {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}




def convert_list_to_dict1(lst):
    """
    Returns:
        dict: A dictionary where the keys and values are the corresponding elements from the input list.
    Raises:
        TypeError: If the input is not a list or if the list contains non-tuple elements.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    if not all(isinstance(elem, tuple) and len(elem) == 2 for elem in lst):
        raise TypeError("All elements in the list must be tuples with two elements")

    return dict(lst)


my_list1 = [(1, 'a'), (2, 'b'), (3, 'c')]
print(convert_list_to_dict1(my_list1))  # Output: {1: 'a', 2: 'b', 3: 'c'}