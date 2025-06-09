# Q.20 Write a program to input three numbers and swap them as this: 1st number becomes the 2nd number, 2nd number becomes the 3rd number and the 3rd number becomes the first number.

x=int(input("Enter the Number 1: "))
y=int(input("Enter the Number 2: "))
z=int(input("Enter the Number 3: "))
print("Original Numbers:",x,y,z)
x,y,z=y,z,x
print("After Swapping:",x,y,z)

"""
O/p: Enter the Number 1: 10
     Enter the Number 2: 5
     Enter the Number 3: 12
     Original Numbers: 10 5 12
     After Swapping: 5 12 10
"""