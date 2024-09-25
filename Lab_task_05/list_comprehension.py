# Creating a list of fruits
fruits = ["apple","banana","cherry","kiwi","mango"]
# Creating an empty list to store fruits that contain the letter "a"
new_list=[]
# Iterating over each fruit in the fruits list
for x in fruits :
    # Checking if the fruit contains the letter "a"
    if "a" in x:
        # If it does, add it to the new_list
        new_list.append(x)

# Printing the new_list
print(new_list)

# Creating a list of numbers
a=[1,3,6,8,2]
# Creating an empty list to store even numbers
b=[]
# Iterating over each number in the list a
for i in a :
    # Checking if the number is even (i.e., it leaves a remainder of 0 when divided by 2)
    if i%2==0 :
        # If it is, add it to the list b
        b.append(i)

# Printing the list b
print(b)