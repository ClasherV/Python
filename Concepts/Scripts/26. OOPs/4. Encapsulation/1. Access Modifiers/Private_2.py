class Student:
    def __init__(self,name,roll_no,age):
        self.name=name
        self._roll_no=roll_no
        self.__age=age
    def __display(self):
        print(f"Age: {self.__age}")
    def displayAge(self):
        self.__display()
class Branch(Student):
    pass
s1=Student("Vaibhav",48,19)
s1.displayAge()

"""
O/p: Age: 19
"""