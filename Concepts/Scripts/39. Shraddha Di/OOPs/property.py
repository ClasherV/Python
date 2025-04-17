class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    
    @property
    def percentage(self):
        return str(round((self.phy+self.chem+self.math)/3,2))+"%"
    
s1=Student(98,97,89)
print(s1.percentage)

s1.phy=97
print(s1.percentage)