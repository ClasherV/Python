numbers=[10,0,-1,7,8,10,-67]
print(numbers)
print(numbers[::])
print(numbers[::1])
print(numbers[::2])
print(numbers[::3])
print(numbers[1:6:3])
print(numbers[-5:6:2])

"""
O/p: [10, 0, -1, 7, 8, 10, -67]
     [10, 0, -1, 7, 8, 10, -67]
     [10, 0, -1, 7, 8, 10, -67]
     [10, -1, 8, -67]
     [10, 7, -67]
     [0, 8]
     [-1, 8]
"""