# Write a Program to find the Area of a Rectangle

class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
rectangle1=Rectangle(3,4)
rectangle2=Rectangle(2,3)
print(f"Area: {rectangle1.area()}")
print()
print(f"Area: {rectangle2.area()}")

"""
O/p: Area: 12
     
     Area: 6
"""