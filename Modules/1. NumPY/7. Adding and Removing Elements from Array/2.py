import numpy as np
a=np.array([1,2,3,4])
b=np.array([[10,20,30],[40,50,60]])
print(np.insert(a,1,[5,6]))
print()
print(np.insert(b,1,[70,80]))
print()
print(np.insert(b,4,[70,80]))

"""
O/p: [1 5 6 2 3 4]
     
     [10 70 80 20 30 40 50 60]
     
     [10 20 30 40 70 80 50 60]
"""