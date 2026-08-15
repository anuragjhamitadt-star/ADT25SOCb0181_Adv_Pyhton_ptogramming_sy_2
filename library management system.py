class Library:
    def __init__(self):
        self.books = ["Python", "Java", "C++"]

    def display(self):
        print("Books:", self.books)

    def borrow(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "borrowed")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print(book, "returned")


lib = Library()

lib.display()
lib.borrow("Python")
lib.display()
lib.return_book("Python")
lib.display() 