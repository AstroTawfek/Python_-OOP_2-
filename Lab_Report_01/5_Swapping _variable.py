'''
Python program to swap two variables
====================================
Author : Tawfek
Date   : 23-09-2024

'''

def swapping():
    a = input("Enter some input : ")
    b = input("Enter some input : ")
    print("Before swapping : ")
    print("a =", a)
    print("b =", b)
    a , b = b , a
    print("After swapping : ")
    print("a =", a)
    print("b =", b)

swapping()