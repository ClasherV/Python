class Duck:
    def swim(self):
        print("I am a Duck and I can Swim")
    def speak(self):
        print("Quack Quack")
class Dog:
    def swim(self):
        print("I am a Dog and I can Swim")
    def speak(self):
        print("Woof Woof")
def display(obj):
    obj.swim()
    obj.speak()
    print("Information Displayed")
d=Duck()
dog=Dog()
display(d)
print()
display(dog)

"""
O/p: I am a Duck and I can Swim
     Quack Quack
     Information Displayed
     
     I am a Dog and I can Swim
     Woof Woof
     Information Displayed
"""