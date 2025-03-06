try:
    a=int(input("Enter a Number between 5 and 9: "))
    if (a<5 or a>9):
        raise ValueError("Enter a Number between 5 and 9 only")
except ValueError as V:
    print(V)

"""
O/p: Enter a Number between 5 and 9: 11
     Enter a Number between 5 and 9 only
"""