class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.isborrowed = False

    def info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Year: {self.year}')

class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)
    
    def display_books(self):
        for book in self.books:
            book.info()
            print()
    
    def search_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def add_book_from_input(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        year = input("Enter the book year: ")

        book = Book(title, author, year)
        self.add_book(book)
        print("Book added succesfully!")

    def add_reader(self):
        name = input("Enter the reader name: ")
        reader = Reader(name)
        self.readers.append(reader)

    def borrow_book(self, title, reader_name):
        book = self.search_title(title)
        if book:
            if book in self.books and book.isborrowed == False:
                for reader in self.readers:
                    if reader.name == reader_name:
                        reader.borrowed_books.append(book)
                        book.isborrowed = True
                        print(f'{reader_name} borrowed {book.title} by {book.author} {book.year}.')
                        return
                print("No reader found")
            else: 
                print("The book is not available")
        else:
            print("No book")

class Reader:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    




library = Library()


print("Welcome to the library!")
choice = None
while choice != 0:
    print("What do you want to do?:")  
    print("1. Add book")
    print("2. Add new reader")
    print("3. Borrow a book")
    print("0. Exit")
    choice = int(input(""))

    if choice == 1: #Add book
        library.add_book_from_input()
        library.display_books()

    elif choice == 2: #Add a new reader
        library.add_reader()

    elif choice == 3: #Borrow a book
        reader_name = input("Enter reader's name: ")
        title = input("Enter book's tile:")
        library.borrow_book(title, reader_name)