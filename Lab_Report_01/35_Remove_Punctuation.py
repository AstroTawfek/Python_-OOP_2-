'''
Python Program to Remove Punctuation from a String
=====================================================
Author : Tawfek
Date   : 25-09-2024

'''

def remove_punctuation(str):

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    no_punct = ""
    for char in str:
        if char not in punctuations:
            no_punct += char

    return no_punct

input_string = "Hello, World! How's it going?"
print("Original string :", input_string)
print("String without punctuation :", remove_punctuation(input_string))