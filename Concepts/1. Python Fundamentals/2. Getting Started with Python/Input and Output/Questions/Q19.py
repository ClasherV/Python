# Q.19 Write a Program to Input two Numbers and Swap them.

n1=int(input("Enter the Number 1: "))
n2=int(input("Enter the Number 2: "))
print("Original Numbers:",n1,n2)
n1,n2=n2,n1
print("After Swapping:",n1,n2)

"""
O/p: Enter the Number 1: 10
     Enter the Number 2: 5
     Original Numbers: 10 5
     After Swapping: 5 10
"""