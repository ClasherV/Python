class Students:
    standard=11
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no
    def getData(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.roll_no}")    
        print(f"Standard: {Students.standard}") 
    def setData(self,age,Standard):
        self.age=age
        Students.standard=Standard
student1=Students("Vaibhav",16,48)
student2=Students("Ayush",17,3)
student1.getData()
print()
student2.getData()
student1.setData(17,12)
student2.setData(18,12)
student1.getData()
print()
student2.getData()