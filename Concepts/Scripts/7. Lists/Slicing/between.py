numbers=[10,0,-1,7,8,10,-67]
print(numbers)
print(numbers[0:0])
print(numbers[0:1])
print(numbers[0:5])
print(numbers[2:6])
print(numbers[6:2])
print(numbers[2:])
print(numbers[:6])

"""
O/p: [10, 0, -1, 7, 8, 10, -67]
     []
     [10]
     [10, 0, -1, 7, 8]
     [-1, 7, 8, 10]
     []
     [-1, 7, 8, 10, -67]
     [10, 0, -1, 7, 8, 10]
"""