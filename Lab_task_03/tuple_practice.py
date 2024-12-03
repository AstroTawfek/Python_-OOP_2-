# touple
a = (1, 3, 5, 7, 4)
print(len(a))
print(type(a))

# change [-3] = 50
a = list(a)
a[-3] = 50
a = tuple(a)
print(a) 

# a[2:4] a[ : -3]
c= a[2 : 4] 
print(c)
d = a[ : -3]
print(d)

# add in last index
a = list (a)
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
print(b)
b.sort()
b=tuple(b)
print(b)

# sum of odd numbers
sum = 0
for x in a:
    if x%2 != 0:
        sum += x
print(sum)