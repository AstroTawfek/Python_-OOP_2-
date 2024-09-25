'''
Python Program to Display Fibonacci Sequence Using Recursion
============================================================
Author : Tawfek
Date   : 25-09-2024

'''

def fibonacci(n):
    if n <= 0:
        print("Input should be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num_terms = int(input("Enter the number of terms in the sequence : "))

for i in range(1, num_terms + 1):
    print(fibonacci(i) , end='  ')