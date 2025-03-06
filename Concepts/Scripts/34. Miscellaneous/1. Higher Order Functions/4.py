def hello(name):
    print("Hello has been executed")
    def greet():
        print("Hare Krishna")
    def welcome():
        print("Jai Shree Ram")
    if name=="Vaibhav":
        return greet
    else:
        return welcome
new_func=hello("Vaibhav")
new_func()
print()
new_func=hello("Ayush")
new_func()
print()
print(new_func)

"""
O/p: Hello has been executed
     Hare Krishna
     
     Hello has been executed
     Jai Shree Ram
     
     <function hello.<locals>.welcome at 0x000002CAB512AAC0>
"""