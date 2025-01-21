height=int(input("Enter Your Height (in feets): "))
if(height>=3):
    print("You can Ride")
    age=int(input("What's Your Age: "))
    if(age<=18):
        print("Pay 250 Rs.")
    else:
        print("Pay 500 Rs.")
else:
    print("You can't Ride")
print("Bye")

"""
O/p 1: Enter Your Height (in feets): 5
       You can Ride
       What's Your Age: 18
       Pay 250 Rs.
       Bye

O/p 2: Enter Your Height (in feets): 5
       You can Ride
       What's Your Age: 19
       Pay 500 Rs.
       Bye

O/p 3: Enter Your Height (in feets): 2
       You can't Ride
       Bye
"""