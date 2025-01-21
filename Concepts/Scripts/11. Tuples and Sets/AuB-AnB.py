A={'Vaibhav','Sanjana','Sahil'}
B={'Sanjana','Aditi','Shraddha'}
C={'Adonis','Mayank','Vaibhav'}
# print(A.symmetric_difference(B))
# print(A.union(B)-A.intersection(B))
# print(A^B^C)
B.symmetric_difference_update(A)
print(A)
print(B)