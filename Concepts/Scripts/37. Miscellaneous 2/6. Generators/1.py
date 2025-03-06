def my_generator():
    for i in range(5000):
        yield i
gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

"""
O/p: 0
     1
     2
"""