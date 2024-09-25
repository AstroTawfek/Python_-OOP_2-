# Assigning values to variables
a = "hello"
b = "b2b2b2"
c = "3g3g       "

# Concatenating strings
d = a + " " + b + " " + c
print(d)

# Printing the length of the string
print("Length : ", len(d))

# Printing the string without the last 3 characters
print(d[:-3])

# Printing the string in reverse order
print(d[::-1])

# Printing the string in uppercase
print("Upper : ", d.upper())

# Printing the string in lowercase
print("Lower : ", d.lower())

# Printing the string with leading and trailing whitespaces removed
print("Strip : ", d.strip())

# Printing the length of the string after removing leading and trailing whitespaces
print("length after strip : ", len(d.strip()))

# Checking if the string contains only digits
print("Is there any digit : ", d.isdigit())

# Finding the index of the first occurrence of "3g"
print("Find 39 : ", d.find("3g"))

# Capitalizing the first letter of the string
print("capitalize : ", d.capitalize())

# Checking if the string contains only alphanumeric characters
print("IsAlNum : ", d.isalnum())

# Counting the occurrences of "a2" in the string
print("counting b2 : ", d.count("a2"))

# Splitting the string into a list of words
print("using split fun. : ", d.split())

# Counting the occurrences of "a2" in the string
print("Counting a2 : ", d.count("a2"))

# Replacing "hello" with "python" in the string
print("Replace  : " , d.replace("hello" , "python"))

# Swapping the case of the string
print("Swapcase : ", d.swapcase())

# Capitalizing the first letter of each word in the string
print("Using title fun. : ", d.title())

# Checking if "a2" is present in the string
if "a2" in d :
    print("true")
else:
    print("False")