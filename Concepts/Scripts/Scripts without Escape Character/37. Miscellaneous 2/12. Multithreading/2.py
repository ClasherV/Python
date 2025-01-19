import threading
import time
from concurrent.futures import ThreadPoolExecutor

print_lock=threading.Lock()
def func(seconds):
    with print_lock:
        print(f"Sleeping for {seconds} Seconds")
    time.sleep(seconds)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1=executor.submit(func,3)
        future2=executor.submit(func,2)
        future3=executor.submit(func,4)
        print(future1.result())
        print(future2.result())
        print(future3.result())
poolingDemo()

"""
O/p: Sleeping for 3 Seconds
     Sleeping for 2 Seconds
     Sleeping for 4 Seconds
     None
     None
     None
"""