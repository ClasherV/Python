class University:
    def __init__(self, u_name):
        self.u_name = u_name

    def showDetails(self):
        print(f"University Name: {self.u_name}")


class Course(University):
    def __init__(self, c_name, u_name):
        University.__init__(self, u_name)
        self.c_name = c_name

    def showDetails(self):
        #University.showDetails(self)
        print(f"Course Name: {self.c_name}")


class Branch(University):
    def __init__(self, b_name, u_name):
        University.__init__(self, u_name)
        self.b_name = b_name

    def showDetails(self):
        University.showDetails(self)
        print(f"Branch Name: {self.b_name}")


class Student(Course, Branch):
    def __init__(self, s_name, c_name, b_name, u_name):
        Course.__init__(self, c_name, u_name)
        Branch.__init__(self, b_name, u_name)
        self.s_name = s_name

    def showDetails(self):
        Course.showDetails(self)
        Branch.showDetails(self)
        print(f"Student Name: {self.s_name}")


class Faculty(Branch):
    def __init__(self, f_name, b_name, u_name):
        Branch.__init__(self, b_name, u_name)
        self.f_name = f_name

    def showDetails(self):
        Branch.showDetails(self)
        print(f"Faculty Name: {self.f_name}")


f = Faculty("Ashok", "AIDS", "DAVV")
s = Student("Vaibhav", "M-Tech(Integrated)", "AIDS", "DAVV")
b = Branch("AIDS", "DAVV")
c = Course("M-Tech(Integrated)", "DAVV")
u = University("DAVV")

f.showDetails()
print()
s.showDetails()
print()
b.showDetails()
print()
c.showDetails()
print()
u.showDetails()