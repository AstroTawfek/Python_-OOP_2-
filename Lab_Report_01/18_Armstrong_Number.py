"""
Python Program to check Armstrong Number
========================================
Author : Tawfek
Date   : 24-09-2024

"""

def is_armstrong(num):
    # converting num to string to easily get the number of digits
    num_str = str(num)
    num_digits = len(num_str)

    # calculating the sum of the digits raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    # checking if the sum is equal to the original number
    return sum_of_digits == num

# test the function
num = int(input("Enter a number : "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")