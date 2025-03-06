# numbers=[10,0,-1,7,8,10,-67,0]
# print(numbers)
# copy=numbers
# copy[0]=23
# print(copy)
# print(numbers[:])

# """
# O/p: [10, 0, -1, 7, 8, 10, -67, 0]
#      [23, 0, -1, 7, 8, 10, -67, 0]
#      [23, 0, -1, 7, 8, 10, -67, 0]
# """

numbers=[10,0,-1,7,8,10,-67,0]
print(numbers)
copy=numbers.copy()
print(copy)
copy[0]=23
print(copy)
print(numbers[:])

"""
O/p: [10, 0, -1, 7, 8, 10, -67, 0]
     [10, 0, -1, 7, 8, 10, -67, 0]
     [23, 0, -1, 7, 8, 10, -67, 0]
     [10, 0, -1, 7, 8, 10, -67, 0]
"""