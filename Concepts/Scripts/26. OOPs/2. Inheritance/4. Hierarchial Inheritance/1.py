class Human:
    def eat(self):
        print("I can Eat")
class Male(Human):
    def sleep(self):
        print("I can Sleep")
class Female(Human):
    def work(self):
        print("I can Work")
male_1=Male()
female_1=Female()
male_1.eat()
male_1.sleep()
female_1.eat()
female_1.work()

"""
O/p: I can Eat
     I can Sleep
     I can Eat
     I can Work
"""