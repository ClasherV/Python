lst=[1,2,3,2,1]
lst1=lst.copy()
lst1.reverse()
if lst1==lst:
    print(f"{lst} is a Palindrome List")
else:
    print("Not a Palindrome")

"""
O/p: [1, 2, 3, 2, 1] is a Palindrome List
"""