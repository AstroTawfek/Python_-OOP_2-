"""
Scenario: You are working on a library management system and need to create a
LibraryBook class to manage details about each book in the library. To prevent unauthorized
changes to critical information, you should use encapsulation principles, specifically by
employing private and protected attributes and methods.
Question:

1. Create a LibraryBook class with the following attributes and methods:

○ A private attribute ISBN that stores the book’s ISBN number, which should not
be accessible directly or modified from outside the class.
○ A protected attribute title to store the book’s title, which can be accessible
within subclasses but should not be modified directly from outside.
○ A protected method display_basic_info() that prints the title and author
of the book, intended to be used by subclasses for detailed display.
○ A public method get_ISBN() that returns the book’s ISBN in a secure way
(e.g., masked format).
○ A public method borrow_book(borrower_name) that:
■ Changes the book’s status to "borrowed".
■ Prints a message indicating the book has been borrowed by
borrower_name.

2. Create a subclass called DigitalLibraryBook that inherits from LibraryBook.
This subclass should:
○ Use the protected display_basic_info() method to print the book’s basic
info along with additional information specific to digital books (e.g., file format).

3. Perform the following actions:
○ Create an instance of LibraryBook with a specific title, author, and ISBN.
○ Display the masked ISBN using get_ISBN().
○ Borrow the book using borrow_book().
○ Create an instance of DigitalLibraryBook and display the book’s basic and
digital information using display_basic_info().

"""


class LibraryBook :
    def __init__(self, title, author, isbn):
        self._title = title         # Protected attribute
        self._author = author       # Assuming author is also protected
        self.__isbn = isbn          # Private attribute
        self.status = "available"    # Status of the book

    def __mask_isbn(self) :
        # Mask the ISBN for secure display (e.g., showing only the last 4 digits)
        return "****-****-****-" + self.__isbn[-4:]

    def get_ISBN(self) :
        # Public method to get the masked ISBN
        return self.__mask_isbn()

    def borrow_book(self, borrower_name) :
        # Public method to change the book's status to borrowed
        self.status = "borrowed"
        print(f"The book '{self._title}' has been borrowed by {borrower_name}.")

    def _display_basic_info(self) :
        # Protected method to display basic info
        print(f"Title : {self._title},  Author : {self._author}")


class DigitalLibraryBook(LibraryBook) :
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format  # Additional attribute for digital books

    def display_info(self) :
        # Use the protected method to display basic info
        self._display_basic_info()
        print(f"File Format : {self.file_format}")


# Example usage:
# Create an instance of LibraryBook
book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")

# Display the masked ISBN
print("Masked ISBN:", book.get_ISBN())

# Borrow the book
book.borrow_book("Alice")

# Create an instance of DigitalLibraryBook
digital_book = DigitalLibraryBook("Digital Fortress", "Dan Brown", "9780440240837", "PDF")

# Display the book's basic and digital information
digital_book.display_info()