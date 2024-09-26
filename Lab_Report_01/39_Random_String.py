"""
Python Program to generate a Random String
=============================================
Author : Tawfek
Date   : 25-09-2024

"""

import random
import string

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters_and_digits) for i in range(length))
    return result_str

print("Random string of length 10 is ", generate_random_string(10))