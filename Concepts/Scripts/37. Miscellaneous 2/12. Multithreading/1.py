import threading
import time

print_lock=threading.Lock()
def func(seconds):
    with print_lock:
        print(f"Sleeping for {seconds} Seconds")
    time.sleep(seconds)

print("Normal Code: \n")
time1=time.perf_counter()
func(4)
func(2)
func(1)
time2=time.perf_counter()
print(f"Time taken: {time2-time1}")

print("\nMultithreading: \n")
time1=time.perf_counter()
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time2=time.perf_counter()
print(f"Time taken: {time2-time1}")

"""
O/p: Normal Code: 
     
     Sleeping for 4 Seconds
     Sleeping for 2 Seconds
     Sleeping for 1 Seconds
     Time taken: 7.002595699999802
     
     Multithreading:
     
     Sleeping for 4 Seconds
     Sleeping for 2 Seconds
     Sleeping for 1 Seconds
     Time taken: 4.001481100000092
"""