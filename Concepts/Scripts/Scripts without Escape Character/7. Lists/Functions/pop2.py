numbers=[10,0,-1,7,8,10,-67,0]
print(numbers)
numbers.pop(2)
print(numbers)
numbers=[10,0,-1,7,8,10,-67,0]
print(numbers)
print(numbers.pop(2))
print(numbers)

"""
O/p: [10, 0, -1, 7, 8, 10, -67, 0]
     [10, 0, 7, 8, 10, -67, 0]
     [10, 0, -1, 7, 8, 10, -67, 0]
     -1
     [10, 0, 7, 8, 10, -67, 0]
"""