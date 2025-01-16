class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
P=Person("Vaibhav",19)
print(P.__dict__)

"""
O/p: {'name': 'Vaibhav', 'age': 19}
"""