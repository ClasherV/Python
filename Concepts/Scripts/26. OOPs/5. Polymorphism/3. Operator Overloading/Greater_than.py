class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        if self.age>other.age:
            return True
        else:
            return False
name1=input("Enter the Name of Person 1: ")
name2=input("Enter the Name of Person 2: ")
print()
age1=int(input("Enter the Age of Person 1: "))
age2=int(input("Enter the Age of Person 2: "))
p1=Person(name1,age1)
p2=Person(name2,age2)
print()
if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")

"""
O/p 1: Enter the Name of Person 1: Ayush   
       Enter the Name of Person 2: Vaibhav
       
       Enter the Age of Person 1: 20
       Enter the Age of Person 2: 19
       
       Ayush will pay the bill

O/p 2: Enter the Name of Person 1: Harshita
       Enter the Name of Person 2: Vaibhav
       
       Enter the Age of Person 1: 18
       Enter the Age of Person 2: 19
       
       Vaibhav will pay the bill
"""