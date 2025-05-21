class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
    def showInfo(self):
        print(f"The Library has {self.noBooks} Books. The Books are: ")
        for i in self.books:
            print(i)
l=Library()
l.addBook("Harry Potter")
l.addBook("Rich Dad Poor Dad")
l.addBook("Data Structures and Algortihms in Java")
l.showInfo()

"""
O/p: The Library has 3 Books. The Books are: 
     Harry Potter
     Rich Dad Poor Dad
     Data Structures and Algortihms in Java
"""