class Father:
    def eat(self):
        print("Eating")
    def sleep(self):
        print("Sleeps from 10:00 PM to 5:00 AM")
class Son(Father):
    def sleep(self):
        print("Sleeps from 2:00 AM to 10:00 AM")
s=Son()
s.sleep()

"""
O/p: Sleeps from 2:00 AM to 10:00 AM
"""