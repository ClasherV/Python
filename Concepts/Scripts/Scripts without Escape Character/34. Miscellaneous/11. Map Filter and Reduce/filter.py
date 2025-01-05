def check(x):
    return x>2
lst=[1,2,3,4,5,6]
print(filter(check,lst))
print(list(filter(check,lst)))

"""
O/p: <filter object at 0x000002BBDAAEB040>
     [3, 4, 5, 6]
"""