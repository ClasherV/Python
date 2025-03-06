a=int(input("Enter the Number 1: "))
b=int(input("Enter the Number 2: "))
if a%2==0 and b%2==0:
    print("%d and %d both are Even Numbers"%(a,b))
elif a%2==0 and b%2!=0:
    print("%d is an Even Number but %d is not an Even Number"%(a,b))
elif a%2!=0 and b%2==0:
    print("%d is not an Even Number but %d is an Even Number"%(a,b))
elif a%2!=0 and b%2!=0:
    print("%d and %d both are not Even Numbers"%(a,b))