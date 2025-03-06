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
        super().work()
        print("I can Code")
class Programmer(Boy):
    def work(self):
        print("I can Write Programs")
boy_1=Boy()
prog_1=Programmer()
boy_1.work()
prog_1.work()

"""
O/p: I can Work
     I can Code
     I can Write Programs
"""