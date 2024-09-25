'''
Python program to convert Kilometres to Miles
=============================================
Author : Tawfek
Date   : 24-09-2024

'''
# Function to convert Kilometres to Miles
def km_to_miles(km):
    miles = km * 0.621371
    return round(miles , 3)

# Function to convert Miles to KiloMeters
def miles_to_km(miles):
    km = miles / 0.621371
    return round(km , 3)


# Testing the function
print("In Miles : ",km_to_miles(float(input("Enter parameter in KiloMeters : "))))
print("In KiloMeters : ",miles_to_km(float(input("Enter parameter in Miles : "))))