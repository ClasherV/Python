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
    def __init__(self,f_name,f_age,can_dance):
        print("Calling init from Female Class")
        super().__init__(f_name,f_age)
        self.know_dancing=can_dance
    def getFemale(self):
        Human.getHuman(self)
        print(f"Know Dancing: {self.know_dancing}")
    def work(self):
        print("I can Work")
female_1=Female("Anjali",20,True)
female_1.getFemale()

"""
O/p: Calling init from Female Class
     Calling init from Human Class
     Name: Anjali, Age: 20
     Know Dancing: True
"""