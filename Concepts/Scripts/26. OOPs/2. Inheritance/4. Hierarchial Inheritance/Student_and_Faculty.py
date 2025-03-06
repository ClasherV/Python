class Person:
    def __init__(self,name,age):
        print("Calling init from Person Class")
        self.name=name
        self.age=age
    def getPerson(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self,s_name,s_age,roll_no):
        print("Calling init from Student Class")
        Person.__init__(self,s_name,s_age)
        self.roll=roll_no
    def getStudent(self):
        Person.getPerson(self)
        print(f"Roll Number: {self.roll}")
class Faculty(Person):
    def __init__(self,f_name,f_age,exp):
        print("Calling init from Faculty Class")
        Person.__init__(self,f_name,f_age)
        self.experience=exp
    def getFaculty(self):
        Person.getPerson(self)
        print(f"Experience: {self.experience}")
student_1=Student("Vaibhav",19,48)
faculty_1=Faculty("Ashok",92,0)
print()
student_1.getStudent()
print()
faculty_1.getFaculty()
print(f"\n{Person.mro()}")
print(f"\n{Student.mro()}")
print(f"\n{Faculty.mro()}")

"""
O/p: Calling init from Student Class
     Calling init from Person Class
     Calling init from Faculty Class
     Calling init from Person Class
     
     Name: Vaibhav, Age: 19
     Roll Number: 48
     
     Name: Ashok, Age: 92
     Experience: 0
     
     [<class '__main__.Person'>, <class 'object'>]
     
     [<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>]
     
     [<class '__main__.Faculty'>, <class '__main__.Person'>, <class 'object'>]
"""