class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

class BookShelf:
    def __init__(self):
        self.books = []

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

    def add_book(self, book:Book):
        if isinstance(book, Book):
            self.books.append(book)
            return True
        return False

book = Book("Harry Potter")
book2 = Book("Python 3")

shelf = BookShelf()
print(shelf)
print(shelf.add_book(book))
print(shelf)

print(shelf.add_book(book))
print(shelf)

print(shelf.add_book({"name": "New Book"}))
print(shelf)