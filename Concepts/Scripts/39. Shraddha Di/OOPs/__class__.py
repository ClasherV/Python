class Person:
    name="Anonymous"
    def __init__(self):
        self.__class__.name="Ada"
p1=Person()
print(p1.name)
print(Person.name)

"""
O/p: Ada
     Ada
"""