import time
def usingWhile():
    i=0
    while(i<5000):
        print(i)
        i+=1
def usingFor():
    for i in range(5000):
        print(i)
init=time.time()
usingWhile()
t1=time.time()-init
init=time.time()
usingFor()
t2=time.time()-init
print(t1)
print(t2)