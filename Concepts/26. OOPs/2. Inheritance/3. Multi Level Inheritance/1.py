class Human(object):
    def eat(self):
        print("I can Eat")
class Male(Human):
    def sleep(self):
        print("I can Sleep")
class Boy(Male):
    pass
boy_1=Boy()
boy_1.eat()
boy_1.sleep()

"""
O/p: I can Eat
     I can Sleep
"""