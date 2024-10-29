numbers=[10,0,-1,7,8,10,-67]
print(numbers)
numbers.extend([45,46,47,78,89])
print(numbers)
numbers=[10,0,-1,7,8,10,-67]
print(numbers)
print(numbers.extend([45,46,47,78,89]))
print(numbers)

"""
O/p: [10, 0, -1, 7, 8, 10, -67]
     [10, 0, -1, 7, 8, 10, -67, 45, 46, 47, 78, 89]
     [10, 0, -1, 7, 8, 10, -67]
     None
     [10, 0, -1, 7, 8, 10, -67, 45, 46, 47, 78, 89]
"""