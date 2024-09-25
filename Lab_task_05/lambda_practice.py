# Defining a function lambda_fun that takes an argument x
def lambda_fun(x):
    # The function returns another function (a lambda function) that takes an argument y
    return lambda y: y**2

# Prompting the user to enter a number
num = int(input("Enter a number : "))

''' Calling lambda_fun with the user's input and store the result in square_function
Since lambda_fun returns a function, square_function is now a function that takes an argument '''
square_function = lambda_fun(num)

''' Calling the function stored in square_function with the user's input as an argument
This will return the square of the user's input '''
print(square_function(num))