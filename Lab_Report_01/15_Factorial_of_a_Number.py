'''
Python Program to Find the Factorial of a Number
=====================================================
Author : Tawfek
Date   : 24-09-2024

'''

def factorial(n):    # recursive Function to calculate the factorial of a number
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a Number : "))
# Calculating the factorial of the number
print(f"factorial of {n} is {factorial(n)}")