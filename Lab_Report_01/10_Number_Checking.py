'''
Python Program to check if a Number is Positive, Negative or Zero
=================================================================
Author : Tawfek
Date   : 24-09-2024

'''

def check_number(num):
    # Checking if the number is positive
    if num > 0:
        return "The number is Positive"
    # Checking if the number is negative
    elif num < 0:
        return "The number is Negative"
    # If the number is neither positive nor negative, it must be zero
    else:
        return "The number is Zero"

print(check_number(float(input("Enter a Number : "))))