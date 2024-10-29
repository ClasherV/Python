# Write a Program to calculate the Sum of Positive Integers only, if User enter -1 or 0, end the loop

sum=0
number=int(input("Enter a Positive Integer (0 or negative Integer to Quit): "))
while number>0:
    sum+=number
    number=int(input("Enter a Positive Integer (0 or negative Integer to Quit): "))
else:
    print(sum)