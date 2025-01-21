# Write a Program to manage the Orders of a Pizza Shop

pizza_size=input("What Size of Pizza do You want (S/M/L): ")
bill=0
if pizza_size=='S' or pizza_size=='s':
    bill=100
    print("Small Pizza Price is 100 Rs.")
elif pizza_size=='M' or pizza_size=='m':
    bill=200
    print("Medium Pizza Price is 200 Rs.")
elif pizza_size=='L' or pizza_size=='l':
    bill=300
    print("Large Pizza Price is 300 Rs.")
else:
    print("Abe ab kya hathi ke size ka pizza laake du")

if pizza_size=='S' or pizza_size=='s' or pizza_size=='M' or pizza_size=='m' or pizza_size=='L' or pizza_size=='l':
    add_pepporoni=input("Do You want Pepporoni on it (Y/N): ")
    if add_pepporoni=='Y' or add_pepporoni=='y':
        if pizza_size=='S' or pizza_size=='s':
            bill+=30
        if pizza_size=='M' or pizza_size=='m':
            bill+=50
        if pizza_size=='L' or pizza_size=='l':
            bill+=50
    
    extra_cheese=input("Do You want Extra Cheese (Y/N): ")
    if extra_cheese=='Y' or extra_cheese=='y':
        bill+=20
    print(f"Total Bill of Your Pizza is {bill}")

"""
O/p: What Size of Pizza do You want (S/M/L): S
     Small Pizza Price is 100 Rs.
     Do You want Pepporoni on it (Y/N): Y
     Do You want Extra Cheese (Y/N): Y
     Total Bill of Your Pizza is 150
"""