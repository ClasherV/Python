class Human:
    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")
class Male(Human):
    def sleep(self):
        print("I can Sleep")
class Boy(Male):
    def work(self):
        print("I can Code")
boy_1=Boy()
boy_1.eat()
boy_1.sleep()
boy_1.work()

"""
O/p: I can Eat
     I can Sleep
     I can Code
"""