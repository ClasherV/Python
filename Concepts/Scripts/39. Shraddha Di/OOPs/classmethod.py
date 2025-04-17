class Person:
    name="Anonymous"

    @classmethod
    def change_name(cls,name):
        cls.name=name
p1=Person()
print(p1.name)
print(Person.name)
p1.change_name("Ada")
print()
print(p1.name)
print(Person.name)

"""
O/p: Anonymous
     Anonymous
     
     Ada
     Ada
"""