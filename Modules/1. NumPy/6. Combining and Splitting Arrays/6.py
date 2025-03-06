import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([[10,20,30],[40,50,60]])
print(np.array_split(a,3))
print()
print(np.array_split(b,3))

"""
O/p: [array([1, 2]), array([3, 4]), array([5])]
     
     [array([[10, 20, 30]]), array([[40, 50, 60]]), array([], shape=(0, 3), dtype=int64)]
"""