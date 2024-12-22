class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Hi myself {self.name} from Student Class")
s1=Student("Vaibhav")
print(s1.name)
s1.display()

"""
O/p: Vaibhav
     Hi myself Vaibhav from Student Class
"""