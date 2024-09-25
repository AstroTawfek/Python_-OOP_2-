"""
Python Program to Find LCM
===========================
Author : Tawfek
Date   : 25-09-2024

"""
def find_gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return find_gcd(num2, num1 % num2)

def find_lcm(num1, num2):
    return (num1 * num2) // find_gcd(num1, num2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The LCM of", num1, "and", num2, "is", find_lcm(num1, num2))