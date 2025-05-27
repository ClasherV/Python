class Human:
    def __init__(self):
        self.num_eyes=2
        self.num_nose=1
    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")
class Male(Human):
    def flirt(self):
        print("I can Flirt")
    def work(self):
        super().work()
        print("I can Code")
male_1=Male()
male_1.eat()
male_1.work()
male_1.flirt()
print()
print(male_1.num_eyes)
print(male_1.num_nose)

"""
O/p: I can Eat
     I can Work
     I can Code
     I can Flirt

     2
     1
"""