'''
Python program to display calendar using user input
===================================================
Author : Tawfek
Date   : 24-09-2024

'''

import calendar

def calender_show():
    year = int(input("Enter the year : "))
    month = int(input("Enter the month : "))
    print(calendar.month(year, month))

calender_show()