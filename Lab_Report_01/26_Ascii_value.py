'''
Python Program To Find ASCII value of a character
=====================================================
Author : Tawfek
Date   : 25-09-2024

'''

def find_ascii(char):
    return ord(char)

char = input("Enter a character : ")
print("The ASCII value of", char, "is", find_ascii(char))