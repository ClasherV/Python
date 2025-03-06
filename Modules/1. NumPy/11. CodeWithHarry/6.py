import numpy as np
a=np.array([0,1,0,2,3])
arr1=np.tile([1,2,3],2)
arr2=np.repeat([1,2,3],2)
print(np.count_nonzero(a))
print()
print(arr1)
print()
print(arr2)

"""
O/p: 3
 
     [1 2 3 1 2 3]

     [1 1 2 2 3 3]
"""