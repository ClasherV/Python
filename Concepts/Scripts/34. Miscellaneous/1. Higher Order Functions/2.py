def greet():
    print("Hi")
def display(other_func_name):
    print("This is display() function")
    other_func_name()
display(greet)

"""
O/p: This is display() function
     Hi
"""