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
    def work(self):
        super().work()
        print("I can Code")
boy_1=Boy("Vaibhav")
print(boy_1.name)
print(Boy.mro())

"""
O/p: Calling init from Male Class
     Vaibhav
     [<class '__main__.Boy'>, <class '__main__.Male'>, <class '__main__.Human'>, <class 'object'>]
"""