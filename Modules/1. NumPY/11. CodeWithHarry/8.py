import numpy as np
arr=np.identity(3)
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print()
print(arr1)
print()
print(arr1.ravel())
print()
print(arr1.flatten())
print()
print(arr1.flat)
print()
print(arr1.nbytes)

"""
O/p: [[1. 0. 0.]
      [0. 1. 0.]
      [0. 0. 1.]]
     
     [[1 2 3]
      [4 5 6]
      [7 8 9]]
     
     [1 2 3 4 5 6 7 8 9]
     
     [1 2 3 4 5 6 7 8 9]
     
     <numpy.flatiter object at 0x0000029C2A247230>

     72
"""