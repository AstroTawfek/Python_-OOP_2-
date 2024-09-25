'''
Python program to solve quadratic equation
==========================================
Author : Tawfek
Date   : 23-09-2024

'''

import cmath

def find_root():
    # Takeing the input from the user
    equation = input("Enter the quadratic equation in form of ax^2 + bx + c : ")
    
    # Removing spaces and splitting the equation into parts
    equation = equation.replace(" ", "").replace("-", "+-")
    parts = equation.split("+")
    
    # Extracting coefficients
    a = float(parts[0].replace("x^2", ""))
    b = float(parts[1].replace("x", ""))
    c = float(parts[2])
    print(f"here,  a = {a : .2f}    b = {b : .2f}   c = {c : .2f}")
    
    # Calculating the discriminant
    d = (b**2) - (4*a*c)
    
    # Finding the roots
    if a==0 :
        print("This is not a quadratic equation.")
    
    else :
        root1 = 0
        root2 = 0
        if d > 0:
            print("The roots are real and distinct")
            root1 = (-b + cmath.sqrt(d)) / (2*a)
            root2 = (-b - cmath.sqrt(d)) / (2*a)
        elif d == 0:
            print("The roots are real and equal")
            root = -b / (2*a)
            root2 = root1 = root
        else:
            print("The roots are complex")
            root1 = (-b + cmath.sqrt(d)) / (2*a)
            root2 = (-b - cmath.sqrt(d)) / (2*a)
        
        print(f"Root 1 = {root1 : .2f}")
        print(f"Root 2 = {root2 : .2f}")

find_root()