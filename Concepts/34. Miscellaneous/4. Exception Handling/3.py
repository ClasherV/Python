try:
    num=int(input("Enter a Number: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number Entered is not an Integer")
except IndexError:
    print("Index Error")

"""
O/p 1: Enter a Number: Vaibhav
       Number Entered is not an Integer

O/p 2: Enter a Number: 4
       Index Error
"""