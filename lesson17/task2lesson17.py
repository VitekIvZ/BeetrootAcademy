#task2lesson17.py


"""
Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and 
adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books

'''

class Library:

    pass

 

class Book:

    pass

 

class Author:

    pass

'''    
"""


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name={self.name}, country={self.country}, birthday={self.birthday})"

    def __str__(self):
        return self.__repr__()


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book(name={self.name}, year={self.year}, author={self.author.name})"

    def __str__(self):
        return self.__repr__()


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name={self.name}, books={len(self.books)}, authors={len(self.authors)})"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    author1 = Author("J.K. Rowling", "UK", "1965-07-31")
    author2 = Author("George R.R. Martin", "USA", "1948-09-20")

    library = Library("City Library")

    book1 = library.new_book("Harry Potter and the Philosopher's Stone", 1997, author1)
    book2 = library.new_book("Harry Potter and the Chamber of Secrets", 1998, author1)
    book3 = library.new_book("A Game of Thrones", 1996, author2)

    print(library)
    print(library.group_by_author(author1))
    print(library.group_by_year(1997))
    print(Book.total_books)
    