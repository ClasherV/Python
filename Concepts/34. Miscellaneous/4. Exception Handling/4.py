def func():
    try:
        lst=[1,2,3,4]
        i=int(input("Enter an Index: "))
        print(lst[i])
        return 1
    except:
        print("Some Error Occurred")
        return 0
    finally:
        print("I am always Executed")
x=func()
print(x)

"""
O/p 1: Enter an Index: 0
       1
       I am always Executed
       1

O/p 2: Enter an Index: 5
       Some Error Occurred
       I am always Executed
       0
"""