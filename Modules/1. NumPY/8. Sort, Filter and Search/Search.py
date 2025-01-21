import numpy as np
arr=np.array([5,6,4,2,3])
print(np.where(arr==4))
print()
print(np.where(arr%2==0))

"""
O/p: (array([2]),)
     
     (array([1, 2, 3]),)
"""