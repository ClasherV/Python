import numpy as np
tobacco_consumption=[30,50,10,30,50,40]
deaths=[100,120,70,100,120,112]
print(np.corrcoef(tobacco_consumption,deaths))

"""
O/p: [[1.         0.99015454]
      [0.99015454 1.        ]]
"""