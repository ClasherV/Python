# dict1={1:10,2:20,3:30}
# print(dict1.get(4))
# print(dict1.keys())
# print(dict1.values())

# """
# O/p: None
#      dict_keys([1, 2, 3])
#      dict_values([10, 20, 30])
# """

dict1={1:10,2:20,3:30}
dict2={4:40,5:50}
dict1.update(dict2)
print(dict1)
dict2.clear()
print(dict2)
dict1.pop(2)
dict1.popitem()
print(dict1)
del dict1[4]
print(dict1)

"""
O/p: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
     {}
"""