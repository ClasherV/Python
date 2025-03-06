a=input("Enter a Number: ")
print("Multiplication Table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
print("Some IMP Lines of Code")
print("End of Program")

"""
O/p 1: Enter a Number: 5
       Multiplication Table of {a} is: 
       5 X 1 = 5
       5 X 2 = 10
       5 X 3 = 15
       5 X 4 = 20
       5 X 5 = 25
       5 X 6 = 30
       5 X 7 = 35
       5 X 8 = 40
       5 X 9 = 45
       5 X 10 = 50
       Some IMP Lines of Code
       End of Program

O/p 2: Enter a Number: Vaibhav
       Multiplication Table of {a} is: 
       invalid literal for int() with base 10: 'Vaibhav'
       Some IMP Lines of Code
       End of Program
"""