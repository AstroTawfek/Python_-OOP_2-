"""
Python Program to Print all Prime Numbers in an Interval
===========================================================
Author : Tawfek
Date   : 24-09-2024

"""

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def Calculate_prime():
    start = int(input("Enter the start of the interval : "))
    end = int(input("Enter the end of the interval : "))
    total_prime = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total_prime += 1
            print(num, end = " ")
    print("\nTotal prime numbers in the interval are : ", total_prime)

Calculate_prime()