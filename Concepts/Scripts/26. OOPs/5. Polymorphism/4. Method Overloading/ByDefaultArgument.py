class Demo:
    def add(sel,a,b,c=0):
        return a+b+c
obj=Demo()
print(obj.add(1,2))
print(obj.add(1,2,3))

"""
O/p: 3
     6
"""