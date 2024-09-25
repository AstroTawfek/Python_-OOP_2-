"""
Python Program to Display the Multiplication Table
=====================================================
Author : Tawfek
Date   : 24-09-2024

"""

def display_multiplication_table():

    n = int(input("Enter a Number to get Multiplication Table : "))
    for i in range(1,11):
        print(f"{n} * {i} = {n * i}")

display_multiplication_table()