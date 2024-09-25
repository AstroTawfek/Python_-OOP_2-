'''
Python Program to Check Prime Number
=====================================
Author : Tawfek
Date   : 24-09-2024

'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(int(input("Enter a Number : "))):
    print("Number is Prime")
else:
    print("Number is not Prime")