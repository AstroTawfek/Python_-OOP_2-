'''
Python Program to Find HCF
=====================================
Author : Tawfek
Date   : 25-09-2024

'''

def find_hcf(x, y):
    if y==0 :
        return x
    return find_hcf(y , x%y)

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("The HCF of", num1,"and", num2,"is", find_hcf(num1, num2))