# Write a Program to find whether the given Number is Prime or not using Functions

# number=int(input("Enter a Number: "))
# def isPrime(number):
#     is_prime=True
#     for i in range(2,number):
#         if number%i==0:
#             is_prime=False
#     if number==1 or number==0:
#         print(f"Given Number {number} is neither Prime nor a Composite Number")
#     elif is_prime==True:
#         print(f"Given Number {number} is a Prime Number")
#     else:
#         print(f"Given Number {number} is not a Prime Number")
# isPrime(number)

# number=int(input("Enter a Number: "))
# def isPrime(number):
#     flag=0
#     for i in range(1,number+1):
#         if number%i==0:
#             flag+=1
#     if number==1 or number==0:
#         print(f"Given Number {number} is neither Prime nor a Composite Number")
#     elif flag==2:
#         print(f"Given Number {number} is a Prime Number")
#     else:
#         print(f"Given Number {number} is not a Prime Number")
# isPrime(number)

import math
number=int(input("Enter a Number: "))
def isPrime(number):
    is_prime=True
    for i in range(2,math.ceil(number/2)+1):
        if number%i==0:
            is_prime=False
    if number==1 or number==0:
        print(f"Given Number {number} is neither Prime nor a Composite Number")
    elif is_prime==True:
        print(f"Given Number {number} is a Prime Number")
    else:
        print(f"Given Number {number} is not a Prime Number")
isPrime(number)

# Use Square Root Method, and one more find out

# import math
# number=int(input("Enter a Number: "))
# def isPrime(number):
#     is_prime=True
#     for i in range(2,math.floor(math.sqrt(number))+1):
#         if number%i==0:
#             is_prime=False
#     if number==1 or number==0:
#         print(f"Given Number {number} is neither Prime nor a Composite Number")
#     elif is_prime==True:
#         print(f"Given Number {number} is a Prime Number")
#     else:
#         print(f"Given Number {number} is not a Prime Number")
# isPrime(number)