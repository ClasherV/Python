numbers=[10,0,-1,7,8,10,-67]
print(numbers)
numbers.sort()
print(numbers)
numbers=[10,0,-1,7,8,10,-67]
print(numbers)
print(numbers.sort())
print(numbers)
print(numbers.sort(reverse=True))
print(numbers)

"""
O/p: [10, 0, -1, 7, 8, 10, -67]
     [-67, -1, 0, 7, 8, 10, 10]
     [10, 0, -1, 7, 8, 10, -67]
     None
     [-67, -1, 0, 7, 8, 10, 10]
     [10, 10, 8, 7, 0, -1, -67]
"""