# Write a Program to find the Area and Circumference of a Circle by using Object Oriented Programming

class Circle:
    PI=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=self.PI*self.radius**2
        return area
    def circumference(self):
        circumference=2*self.PI*self.radius
        return circumference
def main():
    circle1=Circle(4)
    circle2=Circle(2)
    print(f"Area: {circle1.area()}")
    print(f"Circumference: {circle1.circumference()}")
    print(f"\nArea: {circle2.area()}")
    print(f"Circumference: {circle1.circumference()}")
main()

"""
O/p: Area: 50.24
     Circumference: 25.12
     
     Area: 12.56
     Circumference: 25.12
"""