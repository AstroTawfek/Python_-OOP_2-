"""
Python Program to Find Factorial of Number Using Recursion
===========================================================
Author : Tawfek
Date   : 25-09-2024

"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number : "))
result = factorial(num)
print("The factorial of", num, "is", result)