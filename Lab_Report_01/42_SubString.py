"""
Python Program to find the occurrence of a substring within a string
====================================================================
Author : Tawfek
Date   : 26-09-2024

"""

def find_occurrence(string, substring):
   
    """ Returns:
        int: The number of occurrences of the substring in the string. """
    return string.count(substring)


main_string = "Hello, hello, hello world!"
search_string = "hello"
occurrences = find_occurrence(main_string, search_string)

print(f"The substring '{search_string}' occurs {occurrences} times in the string.")