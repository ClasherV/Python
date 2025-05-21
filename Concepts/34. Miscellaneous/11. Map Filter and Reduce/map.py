def cube(x):
    return x**3
lst=[1,2,3,4,5,6]
print(map(cube,lst))
print(list(map(cube,lst)))

"""
O/p: <map object at 0x0000024CA5E7B070>
     [1, 8, 27, 64, 125, 216]
"""