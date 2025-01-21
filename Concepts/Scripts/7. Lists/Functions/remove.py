numbers=[10,0,-1,7,8,10,-67,0]
print(numbers)
numbers.remove(0)
print(numbers)
numbers=[10,0,-1,7,8,10,-67,0]
print(numbers)
print(numbers.remove(0))
print(numbers)

"""
O/p: [10, 0, -1, 7, 8, 10, -67, 0]
     [10, -1, 7, 8, 10, -67, 0]
     [10, 0, -1, 7, 8, 10, -67, 0]
     None
     [10, -1, 7, 8, 10, -67, 0]
"""