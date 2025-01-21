class Human:
    def __init__(self,name,age):
        print("Calling init from Human Class")
        self.name=name
        self.age=age
    def getHuman(self):
        print(f"Name: {self.name}, Age: {self.age}")
    def eat(self):
        print("I can Eat")
class Male(Human):
    def sleep(self):
        print("I can Sleep")
class Female(Human):
    def work(self):
        print("I can Work")
male_1=Male("Vaibhav",19)
female_1=Female("Anjali",20)
print(male_1.name)
print(female_1.name)
print(male_1.age)
print(female_1.age)
male_1.getHuman()
female_1.getHuman()

"""
O/p: Calling init from Human Class
     Calling init from Human Class
     Vaibhav
     Anjali
     19
     20
     Name: Vaibhav, Age: 19
     Name: Anjali, Age: 20
"""