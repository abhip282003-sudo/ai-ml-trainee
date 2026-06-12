# #Create a mini Library Management System using OOP concepts.

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
    def display_book(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added successfully.")

    def show_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for book in self.books:
                book.display_book()

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{book.title}' issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book '{book.title}' returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")

library = Library()
book1 = Book(101, "Python Basics", "Abhishek")
book2 = Book(102, "Data Science", "Rahul")

library.add_book(book1)
library.add_book(book2)

print("\nAvailable Books:")
library.show_books()

print("\nIssue Book:")
library.issue_book(101)

print("\nBooks After Issue:")
library.show_books()

print("\nReturn Book:")
library.return_book(101)

print("\nBooks After Return:")
library.show_books()