import numpy as np
a=np.zeros((2,3))
b=np.ones((2,3))
c=np.empty((2,3))
d=np.eye(3)
e=np.diag([1,2,3])
print(a)
print()
print(b)
print()
print(c)
print()
print(d)
print()
print(e)

"""
O/p: [[0. 0. 0.]
      [0. 0. 0.]]
     
     [[1. 1. 1.]
      [1. 1. 1.]]
     
     [[3.33772792e-307 4.22786102e-307 3.22650139e-307]
      [4.00537740e-307 4.22787121e-307 0.00000000e+000]]
     
     [[1. 0. 0.]
      [0. 1. 0.]
      [0. 0. 1.]]
     
     [[1 0 0]
      [0 2 0]
      [0 0 3]]
"""