'''
Python Program to Print the Fibonacci sequence
=====================================================
Author : Tawfek
Date   : 24-09-2024

'''

def print_fibonacci(n):
    # Initializing the first two numbers in the sequence
    a, b = 0, 1
    # Printing the first two numbers in the sequence
    print(a,"  ", b, end="   ")
    # Loop to print the rest of the sequence
    for _ in range(2, n):
        # Calculating the next number in the sequence
        a, b = b, a + b
        # Printing the next number in the sequence
        print(b, end="   ")


x = int(input("How many terms you wanna show in the series : "))
print_fibonacci(x)