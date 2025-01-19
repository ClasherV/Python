import numpy as np
a=np.array([[1,3],[5,7]])
b=np.array([[2,4],[6,8]])
print(np.concatenate([a,b],axis=0))

"""
O/p: [[1 3]
      [5 7]
      [2 4]
      [6 8]]
"""