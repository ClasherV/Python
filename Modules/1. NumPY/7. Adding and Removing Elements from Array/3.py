import numpy as np
a=np.array([[10,20],[30,40]])
print(np.insert(a,1,[50,60],axis=0))

"""
O/p: [[10 20]
      [50 60]
      [30 40]]
"""