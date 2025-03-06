class Employee:
    company="Apple"
    def show(self):
        print(f"The Name is {self.name} and the Company is {self.company}")
    def changeCompany(cls,newCompany):
        cls.company=newCompany
e1=Employee()
e1.name="Vaibhav"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)

"""
O/p: The Name is Vaibhav and the Company is Apple
     The Name is Vaibhav and the Company is Tesla
     Apple
"""