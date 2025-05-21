# a=int(input("Enter a Numnber: "))
# if a%2==0:
#     print(f"{a} is an Even Number")
# else:
#     print(f"{a} is an Odd Number")

num=int(input("Enter a Number: "))
if num&1:
    print(f"Given Number {num} is an Odd Number")
else:
    print(f"Given Number {num} is an Even Number")