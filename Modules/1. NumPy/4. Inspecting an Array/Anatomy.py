import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10.0,11,12]])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(type(arr))
print(arr.dtype)
print(arr.itemsize)

"""
O/p: 2
     (4, 3)
     12
     <class 'numpy.ndarray'>
     float64
     8
"""