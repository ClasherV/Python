import numpy as np
arr=np.arange(24).reshape(4,6)
print(np.vsplit(arr,2))

"""
O/p: [array([[ 0,  1,  2,  3,  4,  5],
            [ 6,  7,  8,  9, 10, 11]]), array([[12, 13, 14, 15, 16, 17],
            [18, 19, 20, 21, 22, 23]])]
"""