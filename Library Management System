books=["MFC", "MCD", "DSA"]

def show_book(self): 
    print ("Books", self.books)

def borrow_book(self, book1, book2):
    self.book1=book1
    self.book2=book2
    
    if book1 in self.books:
        self.books.remove(book1)
    print (book1, "borrowed successfully")
    print(self.books)
    print("Book not available")

    if book2 in self.books: 
        self.books.remove(book2) 
        print(book2, "borrowed successfully") 
        print(self.books)
    
    else:
        print("Book not available")

def return_book(self, book): 
    self.books.append(book) 
    print(book, "returned successfully") 
    print(self.books)

lib = library()
lib.show_book() 
borrow_book(input ("Enter 1'st book: "),input("Enter 2'nd book: "))
return_book(str(input ("Enter the book you want to return:")))
