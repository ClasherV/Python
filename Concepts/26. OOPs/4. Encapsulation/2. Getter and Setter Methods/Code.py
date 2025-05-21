class Student:
    def __init__(self,name,roll_no,age):
        self.name=name
        self._roll_no=roll_no
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>35:
            print("Invalid Age")
        else:
            self.__age=age
    def display(self):
        print(f"Hi myself {self.name} from Student Class")
s1=Student("Vaibhav",48,19)
print(s1.get_age())
s1.set_age(40)
s1.set_age(20)
print(s1.get_age())

"""
O/p: 19
     Invalid Age
     20
"""