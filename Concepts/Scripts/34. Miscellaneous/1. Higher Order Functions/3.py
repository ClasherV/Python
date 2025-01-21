def greet_louder(name):
    print(f"Hi {name.upper()}")
def greet_softer(name):
    print(f"Hi {name.lower()}")
def hello(other_func_name,name):
    print("This is display() function")
    other_func_name(name)
hello(greet_louder,"Vaibhav")
print()
hello(greet_softer,"Vaibhav")

"""
O/p: This is display() function
     Hi VAIBHAV
     
     This is display() function
     Hi vaibhav
"""