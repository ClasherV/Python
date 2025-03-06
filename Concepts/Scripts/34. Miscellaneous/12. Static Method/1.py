class Math:
    def __init__(self,n):
        self.num=n
    def add_to_num(self,n):
        return self.num+n
    @staticmethod
    def add(a,b):
        return a+b
a=Math(5)
print(a.num)
print(a.add_to_num(6))
print(Math.add(10,5))

"""
O/p: 5
     11
     15
"""