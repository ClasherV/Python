class MyClass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"Value is {self._value}")
    @property
    def ten_value(self):
        return 10*self._value
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10
Obj=MyClass(10)
Obj.ten_value=67
print(Obj.ten_value)
Obj.show()

"""
O/p: 67.0
     Value is 6.7
"""