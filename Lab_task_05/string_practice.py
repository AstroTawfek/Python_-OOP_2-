a = "hello"
b = "b2b2b2"
c = "3g3g       "
d = a+" "+b+" "+c
print(d)

print("Length : ",len(d))
print(d[:-3])
print(d[::-1])

print("Upper : ",d.upper())
print("Lower : ",d.lower())
print("Strip : ",d.strip())
print("length after strip : ",len(d.strip()))
print("Is there any digit : ", d.isdigit())
print("Find 39 : ", d.find("3g"))
print("capitalize : ", d.capitalize())
print("IsAlNum : ", d.isalnum())
print("counting b2 : ", d.count("a2"))
print("using split fun. : ", d.split())
print("Counting a2 : ",d.count("a2"))
print("Replace  : " , d.replace("hello" , "python"))
print("Swapcase : ", d.swapcase())
print("Using title fun. : ",d.title())

if "a2" in d :
    print("true")
else:
    print("False")