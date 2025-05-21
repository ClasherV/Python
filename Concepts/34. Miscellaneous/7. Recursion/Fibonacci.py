def fibonacci(n):
    if n<=0:
        return "Input must be a Positive Integer"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Enter a Number: "))
f=fibonacci(n)
print(f)