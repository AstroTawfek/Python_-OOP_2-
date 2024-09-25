'''
Python Program to Sort Words in Alphabetic Order
=====================================================
Author : Tawfek
Date   : 25-09-2024

'''

def sort_words(sentence):
    words = sentence.split()
    words.sort()
    return ' '.join(words)

# Test the function
sentence = input("Write a sentence : ")
print(sort_words(sentence))