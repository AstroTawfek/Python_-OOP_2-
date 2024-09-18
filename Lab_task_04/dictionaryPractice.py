# Create a dictionary to store information about an employee
emp = {
    "name" : "Tawfek",
    "age" : 22 ,
    "type1" : {
        "developer" : ["ios","android"]  # List of developer types
    } ,
    "parmanent" : True ,
    "salary" : 3000.5 ,
    100 : (1,2,3) ,  # Tuple
    4.5 : {5,6,True,7,1} ,  # Set
    True : 1  # Boolean key
}

# Printing the type of the emp dictionary
print("type :",type(emp))  # Output: <class 'dict'> (indicating it's a dictionary)

# Printing the number of key-value pairs in the dictionary
print("Length :",len(emp))  # Output: 8 (indicating there are 8 key-value pairs)

# Printing the dictionary for employee type
print(emp["type1"])  # Output: {'developer': ['ios', 'android']}

# Printing the employee age
print(emp["age"])  # Output: 22

# Printing the set with unknown purpose
print(emp[4.5])  # Output: {1, 5, 6, 7, True}

# Printing the list of developer types
print(emp["type1"]["developer"])  # Output: ['ios', 'android']

# Printing the second element of the developer types list
print(emp["type1"]["developer"][1])  # Output: 'android'

emp["parmanent"]=False  # Updating the value of 'parmanent' key

# Printing the updated dictionary
print(emp)

emp["gender"] = "male"  # Adding a new key-value pair

# Printing the updated dictionary
print(emp)

emp.pop("age")  # Removing the 'age' key-value pair

# Printing the updated dictionary
print("After removing age: ", emp)

for x in emp.keys():  # Iterating over the keys
    print(x)  # Printing each key

for x,y in emp.items():  # Iterating over the key-value pairs
    print(x,y)  # Printing each key-value pair

for x in emp.values():  # Iterating over the values
    print(x)  # Printing each value


# Creating a nested dictionary to store information about family members
myfamily = {
  "child1" : {  # Dictionary for child 1
    "name" : "Tawfek",
    "year" : 2004
  },
  "child2" : {  # Dictionary for child 2
    "name" : "Muhammad",
    "year" : 2001
  },
  "child3" : {  # Dictionary for child 3
    "name" : "Linus",
    "year" : 2002
  }
}

# Updating the name and add a CGPA for each child
myfamily["child1"]["name"] = "Tawfek"  # Updating child 1 name
myfamily["child1"]["CGPA"] = 3.96  # Adding child 1 CGPA
myfamily["child2"]["name"] = "Muhammad"  # Updating child 2 name
myfamily["child2"]["CGPA"] = 4.00  # Adding child 2 CGPA myfamily["child3"]["name"] = "john"  # Update child 3 name
myfamily["child3"]["CGPA"] = 3.75  # Adding child 3 CGPA

# Printing the updated nested dictionary
print(myfamily)