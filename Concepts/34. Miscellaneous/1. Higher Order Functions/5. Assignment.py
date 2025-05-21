def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def calculator(func_name,x,y):
    return func_name(x,y)
a=calculator(add,10,5)
s=calculator(sub,10,5)
m=calculator(mul,10,5)
d=calculator(div,10,5)
print(a)
print(s)
print(m)
print(d)

"""
O/p: 15
     5
     50
     2.0
"""