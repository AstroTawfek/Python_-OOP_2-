'''
Question 2. String
Suppose you have given a string named sentence as follows:
sentence = "Learning Python is fun and rewarding.”
Write a Python program to:

a. Extract the substring "Python is fun" using negative slicing.

b. Modify the original string by replacing "rewarding" with "exciting".

c. Insert the phrase " Keep practicing!" after "exciting" in the modified string without directly
concatenating it to the end. Instead, insert it at the correct position programmatically.
d. Capitalize the first letter of each word in the final output.
'''

sentence = "Learning Python is fun and rewarding."
print(sentence[-28:-15])
sentence = sentence.replace("rewarding", "exciting")
print("After replacing \"rewarding\" with \"exciting\" :",sentence)
index = sentence.find("exciting")
sentence = sentence[:index + len("rewarding")] + " Keep practicing!" + sentence[index + len("rewarding") :]
print(sentence)
print("Capitalize the first letter of each word :",sentence.title())