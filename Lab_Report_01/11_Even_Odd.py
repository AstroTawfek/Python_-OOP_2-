"""
Python Program to Check if a Number is Odd or Even
=====================================================
Author : Tawfek
Date   : 24-09-2024


"""

def Odd_Even():
    num = int(input("Enter a number : "))
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

Odd_Even()