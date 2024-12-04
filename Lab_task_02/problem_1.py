# Function to calculate (a + b)^2

a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

def calculate(a, b) :
    return (a + b)**2
print("Square of sum of the two numbers :", calculate(a, b))