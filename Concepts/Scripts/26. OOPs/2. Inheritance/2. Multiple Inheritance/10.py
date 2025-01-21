class Human:
    def __init__(self,num_heart):
        print("Calling init from Human")
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")
class Male:
    def __init__(self,name):
        print("Calling init from Male")
        self.name=name
    def flirt(self):
        print("I can Flirt")
    def work(self):
        print("I can Code")
class Boy(Human,Male):
    def __init__(self,name,heart,language):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.language=language
    def sleep(self):
        print("I can Sleep")
    def work(self):
        print("I can Test")
boy_1=Boy("Vaibhav",1,"Python")
print(boy_1.name)
print(boy_1.num_nose)
print(boy_1.num_heart)
print(boy_1.language)

"""
O/p: Calling init from Human
     Calling init from Male
     Vaibhav
     1
     1
     Python
"""