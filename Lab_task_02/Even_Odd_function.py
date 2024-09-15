def Even_Odd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"


def even_Odd_Count(x):
    even_count = 0
    odd_count = 0
    for i in x:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    print(f"total even Number : {even_count}\nTotal Odd number : {odd_count}")


def sum_of_even(x):
    sum = 0
    for i in x:
        if i % 2 == 0:
            sum += i
    return sum

def sum_of_odd(x):
    sum = 0
    for i in x:
        if i % 2 != 0:
            sum += i
    return sum



print(Even_Odd(int(input("Enter a number : "))))  # Outputs: Even if input is 10
numbers = [10, 21, 4, 45, 66, 93, 11]
even_Odd_Count(numbers)
print("Sum of even numbers : ",sum_of_even(numbers))
print("Sum of odd numbers : ",sum_of_odd(numbers))