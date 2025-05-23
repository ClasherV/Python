numbers=[10,0,-1,7,8,10,-67]
print(numbers)
numbers.clear()
print(numbers)
numbers=[10,0,-1,7,8,10,-67]
print(numbers)
del numbers[:]
print(numbers)

"""
O/p: [10, 0, -1, 7, 8, 10, -67]
     []
     [10, 0, -1, 7, 8, 10, -67]
     []
"""