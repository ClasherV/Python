class Car:
    def __init__(self):
        print("Car")
class SUV(Car):
    def __init__(self):
        Car.__init__(self)
        print("SUV")
class Sports(Car):
    def __init__(self):
        Car.__init__(self)
        print("Sports")
class EV(SUV,Sports):
    def __init__(self):
        SUV.__init__(self)
        Sports.__init__(self)
        print("EV")
ev=EV()
print(EV.mro())

"""
O/p: Car
     SUV
     Car
     Sports
     EV
     [<class '__main__.EV'>, <class '__main__.SUV'>, <class '__main__.Sports'>, <class '__main__.Car'>, <class 'object'>]
"""