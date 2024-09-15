# for loop

       #range() Function
for x in range(1,11):
    print(x,end=" ")      # Output : 1 2 3 4 5 6 7 8 9 10
print()

for y in range(0,20,2):
    print(y,end=" ")    # Output : 0 2 4 6 8 10 12 14 16 18
print()

a=10
for x in range(a):
    print(x,end=" ")   # Output : 0 1 2 3 4 5 6 7 8 9
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x , end=" ")      #output apple banana cherry
print()

for x in input() :
    print(x,end=" ")
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x,  end=" ")

  if x == "banana":
    break
print()        # Output : apple banana

for x in fruits:
  if x == "banana":
    break
  print(x,  end=" ")      # Output : apple
print()

for x in fruits:
  if x == "banana":
    continue
  print(x, end=" ")  
print()        # Output : apple cherry banana

    #Else in For Loop
for x in range(6):
  print(x , end=" ")
else:
  print("\nFinally finished!")

for x in range(6):
  if x == 3: break
  print(x, end=" ")
else:
  print("\nFinally finished!")  #If the loop breaks, the else block is not executed.
print()

      #Nested Loops
adj = ["red", "big", "tasty"]
for x in adj:
  for y in fruits:
    print(x, y, end="    ")
  print()

for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error without the pass statement



#while loop

i = 1
while i < 6:
  print(i, end=" ")
  i += 1
print()       # Output : 1 2 3 4 5
#The while loop will continue to execute as long as the condition is true.

i = 1
while i < 6:
  print(i, end=" ")
  if i == 3:
    break
  i += 1
print()       # Output : 1 2 3
#The while loop will stop executing when the condition is false or when the break statement is encountered.

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i, end=" ")
print()       # Output : 1 2 4 5 6
#The while loop will skip the execution of the code inside the loop when the continue statement is encountered

i = 1
while i < 6:
  print(i, end=" ")
  i += 1
else:
  print("\ni is no longer less than 6")
  #The else block will be executed when the loop finishes normally, i.e., without encountering a break