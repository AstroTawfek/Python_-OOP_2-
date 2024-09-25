"""
Python program to convert Celsius to Fahrenheit
================================================
Author : Tawfek
Date   : 24-09-2024

"""

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit , 2)

#  Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius , 2)

# Testing the function with a value
print("In Fahrenheit : ",celsius_to_fahrenheit(float(input("Enter the Temperature in celsius : "))))
print("In Celsius : ",fahrenheit_to_celsius(float(input("Enter the Temperature in Fahrenheit : "))))