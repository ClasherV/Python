class Author:
    def __init__(self,name,book_name,pages):
        self.name=name
        self.book_name=book_name
        self.pages=pages
    def __str__(self):
        return f"{self.book_name} by {self.name}"
    def __len__(self):
        return self.pages
    def __call__(self,*args,**kwargs):
        print("Hi")
    def __del__(self):
        print("Object Deleted")
d=Author("Jenny","Python Basic to Advance",300)
print(d)
print(str(d))
print(len(d))
d()
del d

"""
O/p: Python Basic to Advance by Jenny
     Python Basic to Advance by Jenny
     300
     Hi
     Object Deleted
"""