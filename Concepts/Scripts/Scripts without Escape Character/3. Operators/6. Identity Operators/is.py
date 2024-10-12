a,b,c,d=5,5,10,5.0
print("Id of a: "+str(id(a)))
print("Id of b: "+str(id(b)))
print("Id of c: "+str(id(c)))
print("Id of d: "+str(id(d)))
print("a is b: "+str(a is b))
print("a is b: "+str(id(a)==id(b)))
print("a is c: "+str(a is c))
print("a is c: "+str(id(a)==id(c)))
print("a is d: "+str(a is d))
print("a is d: "+str(id(a)==id(d)))

"""
O/p: Id of a: 140710162135608
     Id of b: 140710162135608
     Id of c: 140710162135768
     Id of d: 2527031176336
     a is b: True
     a is b: True
     a is c: False
     a is c: False
     a is d: False
     a is d: False
"""