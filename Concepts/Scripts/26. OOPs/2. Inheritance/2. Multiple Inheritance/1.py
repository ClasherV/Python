class Human:
    def eat(self):
        print("I can Eat")
class Male:
    def flirt(self):
        print("I can Flirt")
class Boy(Human,Male):
    pass
boy_1=Boy()
boy_1.flirt()

# O/p: I can Flirt