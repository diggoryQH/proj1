class Book:
    def __init__(self, id, title, author, price, stock):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock


class Cart:
    def __init__(self, id):
        self.id = id
        self.items = []


    def add_item(self, book, quantity):
        self.items.append((book, quantity))