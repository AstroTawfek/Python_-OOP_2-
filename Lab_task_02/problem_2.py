
a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

# Lambda function for the same formula
x = lambda a, b : (a + b)**2

print("Output with lambda function : ", x(a, b))