class A:
    def display(self):
        print("Display from A")
class B(A):
    def display(self):
        print("Display from B")
class C:
    def display(self):
        print("Display from C")
class D(B,C):
    def display(self):
        print("Display from D")
        A.display(self)
d1=D()
d1.display()

"""
O/p: Display from D
     Display from A
"""