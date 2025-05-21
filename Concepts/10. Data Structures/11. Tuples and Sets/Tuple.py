tuple0=(1,)
print(type(tuple0),tuple0)
tuple1=(12,3.0,'Jenny',True)
tuple2=(12,10,53,4)
tuple3=(tuple1,tuple2)
tuple4=tuple1+tuple2
lst=[5,10,15,20]
tuple5=tuple(lst)
tuple6=(10,)*5
print(tuple1)
print(min(tuple2))
print(tuple3)
print(len(tuple3))
print(tuple4)
print(tuple5)
print(tuple6)

"""
O/p: <class 'tuple'> (1,)
     (12, 3.0, 'Jenny', True)
     4
     ((12, 3.0, 'Jenny', True), (12, 10, 53, 4))
     2
     (12, 3.0, 'Jenny', True, 12, 10, 53, 4)
     (5, 10, 15, 20)
     (10, 10, 10, 10, 10)
"""