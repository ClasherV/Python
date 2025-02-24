import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array({1,2,3,4,5})
print(f"{arr1} and {arr1.dtype}")
print(f"{arr2} and {arr2.dtype}")

"""
O/p: [1 2 3 4 5] and int64
     {1, 2, 3, 4, 5} and object
"""