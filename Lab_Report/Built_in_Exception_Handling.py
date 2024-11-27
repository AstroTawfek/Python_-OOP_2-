"""
Scenario: 
You are working on a function that processes a list of values by dividing each by a
divisor provided by the user. If the divisor is zero, an error occurs. If the divisor is a non-integer
or non-numeric type, it should also raise an error.

Question:
Write a function divide_elements(values, divisor) that accepts a list of numbers and a divisor.
Use built-in exception handling to catch a ZeroDivisionError when dividing by zero and a
TypeError if the divisor is not numeric. Ensure the program provides meaningful error messages
to the user and gracefully continues processing if possible.

"""

def divide_elements(values, divisor) :
    # Check if the divisor is numeric
    if not isinstance(divisor, (int, float)) :
        raise TypeError("The divisor must be a numeric type (int or float).")
    
    results = []
    
    for value in values :
        try :
            result = value / divisor
            results.append(result)
        except ZeroDivisionError :
            print(f"Error : Division by zero for value {value}. Skipping this value.")
        except TypeError :
            print(f"Error : Non-numeric value {value} encountered. Skipping this value.")
    
    return results

values = [10, 20, "tawfek", 30, 0, 'a', 40]
divisor = 0 

try :
    results = divide_elements(values, divisor)
    print("Results :", results)
except TypeError as e :
    print(e)