#length & type
a = [1, 3, 5, 7, 4]
b = len(a)
print(b)
print(type(a))

# change [-3] = 50
a[-3] = 50
print(a) 

# a[2:4] a[ : -3]
c= a[2 : 4] 
print(c)
d = a[ : -3]
print(d)

# add in last index
a.append(100)
print(a)
a.insert(2, 200)
print(a)

# remove last index
a.remove(100)
print(a)

# join with[2,4,6]
z = [2, 4, 6]
x = a + z 
print(x)

# copy in list & sort 
a = [1, 3, 5, 7, 4]
b = a.copy()
print("After copy: ",b)
a.sort()
print(a)

# sum of odd numbers
sum = 0
for x in a :
    if x%2 != 0 :
        sum += x
print(sum) 

# sum of odd index
a = [1, 3, 5, 7, 4]
sum = 0
for i in range (len(a)) :
    if i%2 != 0 :
        sum += a[i]
print(sum)  

# count number of odd even
a = [1, 3, 5, 7, 4]
odd= 0
even = 0
for i in range (len(a)) :
    if a[i]%2 != 0 :
        odd += 1   
    elif i %2 == 0 :
        even += 1
print("odd number : ", odd)
print("even number : ", even)

# list constructor
a = list(("Tawfek", 1827, "CSE"))
print(a)

# clear
a.clear()
print(a)