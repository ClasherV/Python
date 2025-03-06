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
print(dir(s1))            # Name Mangling
print(s1._Student__age)   #

"""
O/p: ['_Student__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_roll_no', 'display', 'name']
     19
"""