#simple print
print("Hello World! I Don't Give a Bug")

# sample comment 
# This is Python Comment
name = "Tawfek"
print(name)

# An integer assignment
age = 22

# A floating point
salary = 0.000000

# A string
name = "Tawfek"

print(age)
print(salary)
print(name)

x = "Hello World" # string
x = 50  # integer
x = 60.5  # float
x = 3j  # complex
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple
x = {"name": "Suraj", "age": 24} # dict
x = {"geeks", "for", "geeks"} # set
x = True  # bool
x = b"Geeks" # binary

# Python program show input and Output
val = input("Enter your value: ") 
print(val)

#Arithmetic Operators
a = 9
b = 4
add = a + b 
sub = a - b 
mul = a * b
div = a / b
integer_division = a//b
mod = a % b 
exponential = a ** b
print(add) 
print(sub) 
print(mul)
print(div)
print(integer_division)
print(mod) 
print(exponential)

# logical operators
a = True
b = False
print(a and b) # print False
print(a or b)  # print True
print(not a)   # print False as a is True

#Bitwise Operators
a = 10
b = 4
print(a & b) 
print(a | b) 
print(~a) 
print(a ^ b) 
print(a >> 2) 
print(a << 2)

#Assignment Operators
a = 10
b = a 
print(b) 
b += a 
print(b) 
b -= a 
print(b) 
b *= a 
print(b) 
b <<= a 
print(b)

#Python IF-Else
i = 20
if (i < 15): 
    print("i is smaller than 15") 
    print("i'm in if Block") 
else: 
    print("i is greater than 15") 
    print("i'm in else Block") 
print("i'm not in if and not in else Block")

#Python if-elif-else ladder
i = 20
if (i == 10): 
    print("i is 10") 
elif (i == 15): 
    print("i is 15") 
elif (i == 20): 
    print("i is 20") 
else: 
    print("i is not present")

#Python For Loop
for i in range(0, 10, 2): 
    print(i)

#Python While Loop
count = 0
while (count < 3): 
    count = count + 1
    print("Hello Tawfek")

#Python Functions
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
# Driver code to call the function
evenOdd(2)
evenOdd(3)