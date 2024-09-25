'''
Python program to find the area of a triangle
=============================================
Author : Tawfek
Date   : 23-09-2024
'''
import math

def triangle_area():
    print("which you prefer ?\n1. base and height of the triangle\n2. Three hands of the triangle\n1 or 2 ?")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        base = float(input("Enter the base of the triangle : "))
        height = float(input("Enter the height of the triangle : "))
        area = 0.5 * base * height
        print("Area of the triangle is : ", round(area, 2))
    
    else:
        a = float(input("Enter the first side of the triangle : "))
        b = float(input("Enter the second side of the triangle : "))
        c = float(input("Enter the third side of the triangle : "))

        if a+b<=c or b+c<=a or a+c<=b :
            print("This is not a valid triangle")
        else:
            #checking what kind of triangle it is
            if a==b==c:
                print("This is an equilateral triangle")
            elif a==b or b==c or a==c:
                print("This is an isosceles triangle")
            else:
                print("This is a scalene triangle")

            s = (a + b + c) / 2   # Calculating the semi-perimeter of the triangle
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            print("Area of the triangle is : ", round(area, 2))

# Calling the function
triangle_area()