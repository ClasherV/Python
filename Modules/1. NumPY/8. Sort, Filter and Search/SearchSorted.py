import numpy as np
arr=np.array([1,2,3,4,5])
print(np.searchsorted(arr,2))
print(np.searchsorted(arr,5))

"""
O/p: 1
     4
"""