class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
P=Person("Vaibhav",19)
help(Person)

"""
O/p: Help on class Person in module __main__:
     
     class Person(builtins.object)
      |  Person(name, age)
      |
      |  Methods defined here:
      |
      |  __init__(self, name, age)
      |      Initialize self.  See help(type(self)) for accurate signature.
      |
      |  ----------------------------------------------------------------------
      |  Data descriptors defined here:
      |
      |  __dict__
      |      dictionary for instance variables
      |
      |  __weakref__
      |      list of weak references to the object
     
"""