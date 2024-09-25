'''
Python Program to Find Armstrong in an interval
==============================================
Author : Tawfek
Date   : 24-09-2024

'''

# Function to check if a number is Armstrong
def is_armstrong(num):
    # converting num to string to easily get the number of digits
    num_str = str(num)
    num_digits = len(num_str)

    # calculating the sum of the digits raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    # checking if the sum is equal to the original number
    return sum_of_digits == num

def total_armstrong():

    start = int(input("Starting range : "))
    end = int(input("Ending range : "))
    # Initializing a counter for Armstrong numbers
    count = 0
    # Looping through the interval
    for num in range(start, end + 1):
        # Checking if the number is Armstrong
        if is_armstrong(num):
            # Incrementing the counter if the number is Armstrong
            count += 1
            # Printing the Armstrong number
            print(num,end="   ")

    if count==0:
        print("No Armstrong numbers found in the given range")
    else:
        # Printing the total count of Armstrong numbers
        print(f"\nTotal Armstrong numbers : {count}")


total_armstrong()