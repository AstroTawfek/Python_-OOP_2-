'''
Python Program to Find the Sum of Natural Numbers
=====================================================
Author : Tawfek
Date   : 25-09-2024

'''

def sum_of_natural_numbers(n):
    return sum(range(1, n + 1))

n = int(input("Enter a Number : "))
result = sum_of_natural_numbers(n)
print(f"The sum of natural numbers up to {n} is {result}")