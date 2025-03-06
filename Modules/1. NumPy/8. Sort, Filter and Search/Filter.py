import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
o=[True,False,True,False,True,False,True,False,True,False]
print(arr[o])
print()
print(arr[arr>5])
print()
print(arr[arr%2==0])

"""
O/p: [1 3 5 7 9]
     
     [ 6  7  8  9 10]
     
     [ 2  4  6  8 10]
"""