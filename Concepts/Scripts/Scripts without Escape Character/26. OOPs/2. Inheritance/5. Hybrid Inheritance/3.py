class A:
    def display(self):
        print("Display from A")
class B(A):
    def display(self):
        print("Display from B")
        super().display()
class C:
    def display(self):
        print("Display from C")
class D(B,C):
    def display(self):
        print("Display from D")
        super().display()
d1=D()
d1.display()
print(D.mro())

"""
O/p: Display from D
     Display from B
     Display from A
     [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]
"""