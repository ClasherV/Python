# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this Function")
#     return mfx
# @greet
# def hello():
#     print("Hello World")
# hello()

# """
# O/p: Good Morning
#      Hello World
#      Thanks for using this Function
# """

# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this Function")
#     return mfx
# def hello():
#     print("Hello World")
# greet(hello)()

# """
# O/p: Good Morning
#      Hello World
#      Thanks for using this Function
# """

# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("Good Morning")
#         fx(*args,**kwargs)
#         print("Thanks for using this Function")
#     return mfx
# @greet
# def add(a,b):
#     print(a+b)
# add(1,2)

# """
# O/p: Good Morning
#      3
#      Thanks for using this Function
# """

# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("Good Morning")
#         fx(*args,**kwargs)
#         print("Thanks for using this Function")
#     return mfx
# def add(a,b):
#     print(a+b)
# greet(add)(1,2)

# """
# O/p: Good Morning
#      3
#      Thanks for using this Function
# """