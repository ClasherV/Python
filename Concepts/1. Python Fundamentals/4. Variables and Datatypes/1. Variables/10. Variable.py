a=10
b=10
print(id(a),id(b))
c=(a+b)//2
d=(a+b)/2
print(id(c))
print(id(d))
b=5
print(id(b))

"""
O/p: 140730576807112 140730576807112
     140730576807112
     2924895589008
     140730576806952
"""