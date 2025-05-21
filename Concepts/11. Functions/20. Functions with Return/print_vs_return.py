def func1(a,b):
    c=a+b
    return c
def func2(x):
    return x+1
def main():
    a=int(input("Enter the Number 1: "))
    b=int(input("Enter the Number 2: "))
    output1=func1(a,b)
    output2=func2(output1)
    print(output1)
    print(output2)
main()