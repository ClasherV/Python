import numpy as np
arr=np.array([[1,2],[3,4],[5,6]])
arr1=np.array([1,2,3,4,5,6])
arr2=np.ndarray(shape=(2,3),dtype=np.int8)
arr3=np.ndarray(shape=(2,3),dtype=np.bool_)
arr4=np.ndarray(shape=(2,3),dtype=np.uint8)
print(arr1)
print()
print(arr1.reshape(2,3))
print()
print(arr.transpose())
print()
print(arr.T)
print()
print(arr2)
print()
print(arr3)
print()
print(arr4)

"""
O/p: [1 2 3 4 5 6]
     
     [[1 2 3]
      [4 5 6]]
     
     [[1 3 5]
      [2 4 6]]
     
     [[1 3 5]
      [2 4 6]]
     
     [[   0  -83   45]
      [-122  -64    1]]
     
     [[ True  True  True]
      [ True  True  True]]
     
     [[192 198  28]
      [142 192   1]]
"""