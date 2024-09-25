"""
Python Program to Convert Decimal to Binary, Octal and Hexadecimal
==================================================================
Author : Tawfek
Date   : 25-09-2024

"""

def convert_decimal():
    decimal_num = int(input("Enter a decimal number : "))

    # Converting to binary
    binary_num = bin(decimal_num).replace("0b", "")

    # Converting to octal
    octal_num = oct(decimal_num).replace("0o", "")

    # Converting to hexadecimal
    hex_num = hex(decimal_num).replace("0x", "")

    print(f"Binary: {binary_num}")
    print(f"Octal: {octal_num}")
    print(f"Hexadecimal: {hex_num}")


convert_decimal()