class Student:
    def __init__(self,name,roll_no,age):
        self.name=name
        self._roll_no=roll_no
        self.__age=age
    def display(self):
        print(f"Hi myself {self.name} from Student Class")
class Branch(Student):
    pass
s1=Student("Ayush",3)
b1=Branch("Vaibhav",48)
print(b1.name)
print(b1._roll_no)

"""
O/p: Vaibhav
     48
"""