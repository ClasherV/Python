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
        l=[3,5,1,2]
        results=executor.map(func,l)
        for result in results:
            print(result)
poolingDemo()

"""
O/p: Sleeping for 3 Seconds
     Sleeping for 5 Seconds
     Sleeping for 1 Seconds
     Sleeping for 2 Seconds
     None
     None
     None
     None
"""