class Student:
    def __init__(self,name,roll_no,age):
        self.name=name
        self._roll_no=roll_no
        self.__age=age
    def display(self):
        print(f"Hi myself {self.name} from Student Class")
class Branch(Student):
    pass
s1=Student("Vaibhav",48,19)

"""
O/p: 
"""