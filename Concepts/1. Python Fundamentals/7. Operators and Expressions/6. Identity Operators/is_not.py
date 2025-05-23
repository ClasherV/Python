a,b,c,d=5,5,10,5.0
print("Id of a: "+str(id(a)))
print("Id of b: "+str(id(b)))
print("Id of c: "+str(id(c)))
print("Id of d: "+str(id(d)))
print("a is not b: "+str(a is not b))
print("a is not b: "+str(id(a)!=id(b)))
print("a is not c: "+str(a is not c))
print("a is not c: "+str(id(a)!=id(c)))
print("a is not d: "+str(a is not d))
print("a is not d: "+str(id(a)!=id(d)))

"""
O/p: Id of a: 140710162135608
     Id of b: 140710162135608
     Id of c: 140710162135768
     Id of d: 1946514795664
     a is not b: False
     a is not b: False
     a is not c: True
     a is not c: True
     a is not d: True
     a is not d: True
"""