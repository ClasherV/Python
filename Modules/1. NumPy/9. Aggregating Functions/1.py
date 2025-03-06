import numpy as np
arr=np.array([10,20,30,40,50])
print(arr)
print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.size(arr))
print(np.mean(arr))
print(np.cumsum(arr))
print(np.cumprod(arr))

"""
O/p: [10 20 30 40 50]
     150
     10
     50
     5
     30.0
     [ 10  30  60 100 150]
     [      10      200     6000   240000 12000000]
"""