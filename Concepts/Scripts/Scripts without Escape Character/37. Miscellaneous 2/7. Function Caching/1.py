from functools import lru_cache
import time
@lru_cache(maxsize=None) #Memoization
def fx(n):
    time.sleep(5)
    return n*5
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")
print(fx(61))
print("Done for 61")

"""
O/p: 100
     Done for 20
     10
     Done for 2
     30
     Done for 6 
     100        
     Done for 20
     10
     Done for 2 
     30
     Done for 6 
     305
     Done for 61
"""