'''
Python Program to Print Sum of First Ten Natural Numbers
===========================================================
Author : Tawfek
Date   : 25-09-2024

'''

def sum_of_first_ten_natural_numbers():
    sum = 0
    for i in range(1, 11):
        sum += i
    print("The sum of the first ten natural numbers is:", sum)

sum_of_first_ten_natural_numbers()