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
    pass
boy_1=Boy()
boy_1.flirt()
Male.work(boy_1)

"""
O/p: I can Flirt
     I can Code
"""