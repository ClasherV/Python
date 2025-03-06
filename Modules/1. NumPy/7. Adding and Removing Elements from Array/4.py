import numpy as np
a=np.array([[10,20],[30,40]])
print(np.insert(a,1,[50,60],axis=1))

"""
O/p: [[10 50 20]
      [30 60 40]]
"""