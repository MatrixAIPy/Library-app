class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Year: {self.year}')

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def display_books(self):
        for book in self.books:
            book.info()
            print()
    
    def search_author(self, author):
        found_books = []
        for book in self.books:
            if book.author == author:
                found_books.append(book)
        if found_books:
            print(f'Books by {author}: ')
            for book in found_books:
                print(book.info)
                print()
        else:
            print('No books found by this author.')

    def add_book_from_input(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        year = input("Enter the book year: ")

        book = Book(title, author, year)
        self.add_book(book)
        print("Book added succesfully!")



library = Library()


print("Welcome to the library!")
choice = None
while choice != 0:
    print("What do you want to do?:")  
    print("1. Add book.")
    choice = int(input(""))
    if choice == 1:
        library.add_book_from_input()
        library.display_books()