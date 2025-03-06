class Human:
    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")
class Male(Human):
    pass
male_1=Male()
male_1.eat()
male_1.work()

"""
O/p: I can Eat
     I can Work
"""