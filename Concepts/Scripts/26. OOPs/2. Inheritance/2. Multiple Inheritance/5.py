class Human:
    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")
class Male:
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
boy_1.flirt()
boy_1.work()
boy_1.sleep()
print(Boy.mro())   # Method Resolution Order

"""
O/p: I can Flirt
     I can Test
     I can Sleep
     [<class '__main__.Boy'>, <class '__main__.Human'>, <class '__main__.Male'>, <class 'object'>]
"""