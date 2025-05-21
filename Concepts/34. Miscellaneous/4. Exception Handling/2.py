a=input("Enter a Number: ")
print("Multiplication Table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input!!")
print("Some IMP Lines of Code")
print("End of Program")

"""
O/p: Enter a Number: Vaibhav
     Multiplication Table of {a} is: 
     Invalid Input!!
     Some IMP Lines of Code
     End of Program
"""