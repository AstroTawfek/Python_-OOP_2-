# Defining two sets, 'a' and 'b', with initial elements
a = {1, 3, 5, 8, 3, 7}  # Set 'a' with duplicate element 3
b = {0, False, 1, 5}  # Set 'b' with mixed data types

# Printing the length and type of set 'a'
print("Length of the set : ", len(a), "\nType : ", type(a))

# Adding a new element 10 to set 'a'
a.add(10)
print("After adding 10 : ", a)

# Removing the element 8 from set 'a'
a.discard(8)
print("After removing 8 : ", a)

# Performing a union operation between sets 'a' and 'b'
a_union = a.union(b)
print("After union operation : ", a_union)

# Finding the intersection of sets 'a' and 'b'
a_intersection = a.intersection(b)
print(f"Intersection of a & b : {a_intersection}")

# Finding the difference of sets 'a' and 'b' (i.e., elements in 'a' but not in 'b')
a_difference = a.difference(b)  # Corrected to a.difference(b) instead of a.difference(a, b)
print("After difference a-b : ", a_difference)

# Iterating over the elements of set 'a' and print them until 5 is found
for x in a:
    if x == 5:
        break
    print(x)

# Performing a union operation between set 'a' and a new set containing elements 2, 3, and 4
print(a.union(set([2, 3, 4])))

# Checking if the element 3 is present in set 'a'
if 3 in a:
    print("3 is present")

# Checking if set 'a' is a superset of set 'b'
print(a.issuperset(b))

# Checking if set 'a' is a subset of set 'b'
print(a.issubset(b))