          #for Lecture one

print('Hello World\nI am learning python')

#Variables in Python
x = 40    
y = "Bangladesh" 
print(x)
print(type(y))

#Print Function
print("Welcome to Python!")
print("welcome","to","python")
print("Welcome\tto\tPython")

#Printing Expression with Escape Sequences
print("""sum is""",7+3)
print('Display \'Hi\' in quotes') #\'
print("Display \"Hi\" in quotes") #\""
print('''Display 'Hi' and "Bye" in quotes''')

#Getting Input from the User
name = input("What's your name: ")
print(name)
value1 = input('Enter first number: ')
value2 = input('Enter second number: ')
add = value1 + value2
print(add)

#Multiple Input from the User
a , b = input().split()
print (a, b)
print(type(a))

#Objects and Dynamic Typing
print(type(7))
print(type(1.1))
print(type("cat"))

#Variables Refer to Objects
x=10
print(x+7)
print(x)


           # For Lecture two

#if…elif…else Statement
grade = 77
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

#While Statement
product = 3
while product <= 50 :
    product*=3
print(product)

#For Statements
for character in 'Programming':
    print(character, end='  ')

#Iterables , Lists and Iterators
total = 0
for number in [2, -3, 0, 17, 9]:
    total += number
print(total)

#Built-In range Function
total=0
for number in range(10):
    total += number
print(total)

#Built-In Function range: A Deeper Look
for number in range(5, 10):
    print(number , end=' ')
for number in range(0, 10, 2):
    print(number,end=' ')
for number in range(10, 0, -2):
    print(number,end=' ')
total=0
for number in range(2, 101, 2):
    total += number
print(total)

#Augmented Assignments
total=0
for number in [1, 2, 3, 4, 5]:
    total = total + number
print(number)

#Break and continue Statements
for number in range(15):
    if number == 10:
        break
    print(number,end=' ')
for number in range(10):
    if number == 5:
        continue
    print(number,end=' ')

#Sequence-Controlled Repetition
total = 0 # sum of grades
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94] # list of 10 grades
for grade in grades:
    total += grade # add current grade to the running total
    grade_counter += 1 # indicate that one more grade was 
average = total / grade_counter
print(f'Class average is {average:.2f}')

#Formatted Strings
name = 'John'
age = 30
print(f'Hello, my name is {name} and I am {age} years old')

#Implementing Sentinel-Controlled Iteration
"""Class average program with sentinel-controlled iteration."""
total = 0
grade_counter = 0  # number of grades entered
while grade != -1:
    grade = int(input('Enter grade, -1 to end: '))  # get one grade
    total += grade
    grade_counter += 1
if grade_counter != 0:
    average = total / (grade_counter - 1)
    print(f'Class average is {average:.2f}')
else:
    print('No grades were entered')

#Implementing the Algorithm using Nested Control Statements
"""Using nested control statements to analyze examination results."""
passes = 0  # number of passes
failures = 0  # number of failures
for student in range(10):
    result = int(input('Enter result (1=pass, 2=fail): '))
    if result == 1:
        passes += 1
    else:
        failures += 1
print('Passed:', passes)
print('Failed:', failures)
if passes > 8:
    print('Bonus to instructor')