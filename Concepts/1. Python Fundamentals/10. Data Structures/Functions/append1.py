numbers=[10,0,-1,7,8,10,-67]
print(numbers)
numbers.append(45)
print(numbers)
numbers=[10,0,-1,7,8,10,-67]
print(numbers)
print(numbers.append(45))
print(numbers)

"""
O/p: [10, 0, -1, 7, 8, 10, -67]
     [10, 0, -1, 7, 8, 10, -67, 45]
     [10, 0, -1, 7, 8, 10, -67]
     None
     [10, 0, -1, 7, 8, 10, -67, 45]
"""