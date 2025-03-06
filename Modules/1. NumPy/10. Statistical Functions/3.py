import numpy as np
price=[300,100,350,150,200]
sales=[10,20,7,17,3]
print(np.corrcoef([price,sales]))

"""
O/p: [[ 1.         -0.66621445]
      [-0.66621445  1.        ]]
"""