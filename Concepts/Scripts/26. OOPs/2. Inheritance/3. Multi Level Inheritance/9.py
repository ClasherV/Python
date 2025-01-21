class Human:
    def __init__(self,num_heart):
        print("Calling init from Human Class")
        self.eyes=2
        self.num_heart=num_heart
    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")
class Male(Human):
    def __init__(self,name):
        print("Calling init from Male Class")
        self.name=name
    def sleep(self):
        print("I can Sleep")
class Boy(Male):
    def __init__(self,name,heart,Gamer):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.isGamer=Gamer
    def work(self):
        super().work()
        print("I can Code")
boy_1=Boy("Vaibhav",1,True)
print(boy_1.name)
print(boy_1.num_heart)
print(boy_1.isGamer)
print(Boy.mro())

"""
O/p: Calling init from Human Class
     Calling init from Male Class
     Vaibhav
     1
     True
     [<class '__main__.Boy'>, <class '__main__.Male'>, <class '__main__.Human'>, <class 'object'>]
"""