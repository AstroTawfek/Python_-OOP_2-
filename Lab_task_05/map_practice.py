# Defining a function my_cal that takes a string x and returns its length
def my_cal(x):
    return len(x)
"""
Using the map function to apply my_cal to each string in the tuple ("Mohammad","Ullah","Tawfek")
and print the resulting list of lengths
"""
print("The length :",list(map(my_cal , ("Mohammad","Ullah","Tawfek"))))


''' Defining a function make_cube that takes a single number x and returns its cube'''
def make_cube(x):
    return x**3
'''Using the map function to apply make_cube to each number in the tuple (1,3,4,5)
and print the resulting list of cubes'''
print("Showing cube :",list(map(make_cube,(1,3,4,5))))


# Defining a function make_cube that takes two numbers x and y and returns x to the power of y
def make_cube(x,y):
    return x**y
'''Using the map function to apply make_cube to corresponding pairs of numbers from the tuples (2,3,4,5) and (7,4,3,2)
and print the resulting list of results'''
print("Showing cube :",list(map(make_cube,(2,3,4,5),(7,4,3,2))))