# Defining a function called mult_table that takes one argument x
def mult_table(x):
    # Loop through numbers from 1 to 10 (excluding 11) with a step of 1
    for i in range(1, 11, 1):
        # If the current number is 4, skip this iteration and move to the next one
        if i == 4:
            continue
        
        # Printing the multiplication table for the number x and the current number i
        print(f"{x} * {i} = {x*i}")
        
        # If the current number is 8, break out of the loop
        if i == 8:
            break
    
# Asking the user to enter a number and pass it to the mult_table function
mult_table(int(input("Enter a Number : ")))