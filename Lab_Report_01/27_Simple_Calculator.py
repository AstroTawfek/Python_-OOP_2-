"""
Python Program to Make a Simple Calculator
=============================================
Author : Tawfek
Date   : 25-09-2024

"""

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   if y == 0:
      return "Error! Division by zero is not allowed."
   else:
      return x / y

def remainder(x, y):
   if y == 0:
      return "Error! Division by zero is not allowed."
   else:
      return x % y

def floor_division(x, y):
   if y == 0:
      return "Error! Division by zero is not allowed."
   else:
      return x // y

def exponential(x, y):
   return x ** y

print("Select operation.")
print("1. Addition")

print("2. Subtraction")

print("3. Multiply")
print("4. Divide")
print("5. Remainder")
print("6. Floor Division")
print("7. Exponential")

while True:
   choice = input("Enter choice(1/2/3/4/5/6/7) : ")
   
   if choice in ('1', '2', '3', '4', '5', '6', '7'):
      num1 = float(input("Enter first number : "))
      num2 = float(input("Enter second number : "))

      if choice == '1':
         print(num1, "+", num2, "=", add(num1, num2))

      elif choice == '2':
         print(num1, "-", num2, "=", subtract(num1, num2))

      elif choice == '3':
         print(num1, "*", num2, "=", multiply(num1, num2))

      elif choice == '4':
         print(num1, "/", num2, "=", divide(num1, num2))

      elif choice == '5':
         print(num1, "%", num2, "=", remainder(num1, num2))

      elif choice == '6':
         print(num1, "//", num2, "=", floor_division(num1, num2))

      elif choice == '7':
         print(num1, "**", num2, "=", exponential(num1, num2))
      
      next_calculation = input("Do you want to do another calculation? (yes/no) : ")
      if next_calculation.lower() != "yes":
         break
    
   else:
      print("Invalid Input")