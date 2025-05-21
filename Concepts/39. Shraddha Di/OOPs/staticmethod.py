class greet:
    def __init__(self):
        self.name="Ada"

    @staticmethod
    def hello():
        print("Hello World")
obj=greet()
print(obj.name)
greet.hello()

"""
O/p: Ada
     Hello World
"""