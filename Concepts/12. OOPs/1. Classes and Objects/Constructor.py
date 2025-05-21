class Student:
    def __init__(self,student_name,student_age,student_language):
        self.name=student_name
        self.age=student_age
        self.language=student_language
        self.Girlfriend=0
student1=Student('Vaibhav',19,'Python')
student2=Student('Ayush',20,'Javascript')
print(student1.name)
print(student1.age)
print(student1.language)
print()
print(student2.name)
print(student2.age)
print(student2.language)