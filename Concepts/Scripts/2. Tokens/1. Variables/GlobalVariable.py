# x="awesome"
# def myFunc():
#     print("Python is "+x)
# myFunc()

# """
# O/p: Python is awesome
# """

# x="awesome"
# def myFunc():
#     x="fantastic"
#     print("Python is "+x)
# myFunc()
# print("Python is "+x)

# """
# O/p: Python is fantastic
#      Python is awesome
# """

# def myFunc():
#     global x
#     x="fantastic"
#     print("Python is "+x)
# myFunc()
# print("Python is "+x)

# """
# O/p: Python is fantastic
#      Python is fantastic
# """

x="awesome"
def myFunc():
    global x
    x="fantastic"
    print("Python is "+x)
myFunc()
print("Python is "+x)

"""
O/p: Python is fantastic
     Python is fantastic
"""