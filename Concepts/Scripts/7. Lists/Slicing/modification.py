numbers=[10,0,-1,7,8,10,-67]
print(numbers)
numbers[1]=45
print(numbers)
numbers=[10,0,-1,7,8,10,-67]
print(numbers)
numbers[1:6]=[1,2,3,4,5]
print(numbers)
numbers=[10,0,-1,7,8,10,-67]
print(numbers)
numbers[1:7:2]=[1,2,3]
print(numbers)
numbers=[10,0,-1,7,8,10,-67]
print(numbers)
numbers[-5:6:2]=[1,2]
print(numbers)

"""
O/p: [10, 0, -1, 7, 8, 10, -67]
     [10, 45, -1, 7, 8, 10, -67]
     [10, 0, -1, 7, 8, 10, -67]
     [10, 1, 2, 3, 4, 5, -67]
     [10, 0, -1, 7, 8, 10, -67]
     [10, 1, -1, 2, 8, 3, -67]
     [10, 0, -1, 7, 8, 10, -67]
     [10, 0, 1, 7, 2, 10, -67]
"""