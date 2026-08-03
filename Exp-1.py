# Experiment 1
# Title: Introduction to OOP Concepts

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron, book):
        if not book.is_borrowed:
            book.borrow()
            patron.borrow_book(book)
            print(patron.name, "borrowed", book.title)
        else:
            print(book.title, "is already borrowed.")

    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            book.return_book()
            patron.return_book(book)
            print(patron.name, "returned", book.title)
        else:
            print("Book was not borrowed by", patron.name)

    def display(self):
        print("\nBooks in Library:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(book.title, "-", book.author, "-", status)

        print("\nPatron Details:")
        for patron in self.patrons:
            print(patron.name, "Borrowed Books:")
            if patron.borrowed_books:
                for book in patron.borrowed_books:
                    print("  ", book.title)
            else:
                print("None")

library = Library()

book1 = Book("Python Programming", "John", "101")
book2 = Book("Data Structures", "David", "102")
book3 = Book("Machine Learning", "Andrew", "103")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

patron1 = Patron("ABC", 1)
patron2 = Patron("XYZ", 2)

library.register_patron(patron1)
library.register_patron(patron2)

library.borrow_book(patron1, book2)
library.borrow_book(patron2, book3)

library.return_book(patron2, book3)

library.display()