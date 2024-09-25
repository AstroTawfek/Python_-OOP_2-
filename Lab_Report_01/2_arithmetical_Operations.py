"""
Python program to do arithmetical operations
Addition
Subtraction
Multiplication
Division
floor division
modulus
exponential
===========================================
Author : Tawfek
Date   : 23-09-2024
"""

def arithmatic_operation():
    # Taking input from user
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    summation = num1 + num2
    substruction = num1 - num2
    multiplication = num1 * num2
    division = round(num1 / num2 , 2)
    floor_division = num1 // num2
    modulus = num1 % num2
    exponential = num1 ** num2
    print("Summation of two numbers is : ", summation)
    print("Substruction of two numbers is : ", substruction)
    print("Multiplication of two numbers is : ", multiplication)
    print("Division of two numbers is : ", division)
    print("Floor Division of two numbers is : ", floor_division)
    print("Modulus of two numbers is : ", modulus)
    print("Exponential of two numbers is : ", exponential)


arithmatic_operation()