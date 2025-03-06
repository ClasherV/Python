class Demo:
    def add(self,*args):
        total=0
        for i in args:
            total+=i
        return total
obj=Demo()
print(obj.add(1,2))
print(obj.add(1,2,3))
print(obj.add(1,2,3,4))
print(obj.add(1,2,3,4,5))

"""
O/p: 3
     6
     10
     15
"""