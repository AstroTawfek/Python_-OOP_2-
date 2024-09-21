"""
Question 5. Tuple & Set
You are developing a Python application to manage a collection of book records and unique tags
for a library system.
You have the following data structures:
1. A tuple of book records, where each record contains the title, author, and publication year
of a book.
2. A set of unique tags associated with these books.
Here is the initial data:
books = (

("To Kill a Mockingbird", "Harper Lee", 1960),
("1984", "George Orwell", 1949),
("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)
tags = {"classic", "dystopian", "novel", "literature"}

Perform the following tasks: 
a. Access the second book's author from the books tuple and print it.
b. Add a new record for the book "Brave New World" by Aldous Huxley, published in 1932, to
the books tuple. Note that tuples are immutable; you should demonstrate the correct approach to
updating the tuple.
c. Unpack the details of the third book into separate variables and print them.
d. Loop through the books tuple and print each book's title.
e. Add a new tag "sci-fi" to the tags set and print the updated set.
f. Use a method to remove the tag "novel" from the tags set and print the updated set.
"""


books = (
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)
tags = {"classic", "dystopian", "novel", "literature"}

print("Author of the second book :", books[1][1])

books = books + (("Brave New World", "Aldous Huxley", 1932),)
print("Updated books tuple :", books)

title, author, year = books[2]
print("Title :", title)
print("Author :", author)
print("Year :", year)

for x in books:
    print("Book title :", x[0])

tags.add("sci-fi")
print("Updated tags set :", tags)

tags.remove("novel")
print("Updated tags set :", tags)