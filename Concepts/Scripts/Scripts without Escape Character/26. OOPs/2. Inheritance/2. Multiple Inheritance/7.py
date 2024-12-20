class Human:
    def __init__(self):
        print("Calling init from Human")
        self.num_eyes=2
        self.num_nose=1
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
    def sleep(self):
        print("I can Sleep")
    def work(self):
        print("I can Test")
boy_1=Boy()
print(boy_1.num_nose)

"""
O/p: Calling init from Human
     1
"""