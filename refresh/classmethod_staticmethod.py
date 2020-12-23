class Book:
    TYPES = ("hardcover", "paperback")
    
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book({self.name}, {self.book_type}, weighing {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover("Memorias Postumas", 900)
light = Book.paperback("São Bernardo", 500)

print(book)
print(light)


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def __str__(self):
        return f"{self.name}"
    
    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        total = int(store.stock_price())
        return "{}, total stock price: {}".format(store.name, total)


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("keyboard", 100)

print(store)
print(Store.store_details(store2))
