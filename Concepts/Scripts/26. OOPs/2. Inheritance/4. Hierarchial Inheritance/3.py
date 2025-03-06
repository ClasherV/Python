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
    def __init__(self,m_name,m_age,location):
        print("Calling init from Male Class")
        Human.__init__(self,m_name,m_age)
        self.location=location
    def sleep(self):
        print("I can Sleep")
class Female(Human):
    def work(self):
        print("I can Work")
male_1=Male("Vaibhav",19,"Indore")
print(male_1.name)
print(male_1.age)
male_1.getHuman()
print(male_1.location)
print(Male.mro())

"""
O/p: Calling init from Male Class
     Calling init from Human Class
     Vaibhav
     19
     Name: Vaibhav, Age: 19
     Indore
     [<class '__main__.Male'>, <class '__main__.Human'>, <class 'object'>]
"""