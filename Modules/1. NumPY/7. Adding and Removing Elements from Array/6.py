import numpy as np
a=np.array([[10,20],[30,40]])
print(np.delete(a,1))
print()
print(np.delete(a,1,axis=0))
print()
print(np.delete(a,1,axis=1))

"""
O/p: [10 30 40]
     
     [[10 20]]
     
     [[10]
      [30]]
"""