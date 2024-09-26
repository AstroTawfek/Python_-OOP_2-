"""
Python Program to check whether given string is a palindrome or not
===================================================================
Author : Tawfek
Date   : 26-09-2024

"""

def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string : ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")