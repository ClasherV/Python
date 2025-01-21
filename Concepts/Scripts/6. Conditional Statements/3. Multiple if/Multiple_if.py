height=int(input("Enter Your Height (in feets): "))
bill=0
if(height>=3):
    print("You can Ride")
    age=int(input("What's Your Age: "))
    if(age<12):
        print("Pay 150 Rs.")
        bill=150
    elif(age<=18):
        print("Pay 250 Rs.")
        bill=250
    else:
        print("Pay 500 Rs.")
        bill=500
    want_photo=input("Do You want a Photo (Y/N): ")
    if want_photo=='y' or want_photo=='Y':
        bill+=50
    print(f"Your Total Bill is {bill} Rs.")
else:
    print("You can't Ride")
print("Bye")

"""
O/p 1: Enter Your Height (in feets): 4
       You can Ride
       What's Your Age: 11
       Pay 150 Rs.
       Do You want a Photo (Y/N): Y
       Your Total Bill is 200 Rs.
       Bye

O/p 2: Enter Your Height (in feets): 5
       You can Ride
       What's Your Age: 18
       Pay 250 Rs.
       Do You want a Photo (Y/N): y
       Your Total Bill is 300 Rs.
       Bye

O/p 3: Enter Your Height (in feets): 5
       You can Ride
       What's Your Age: 19
       Pay 500 Rs.
       Do You want a Photo (Y/N): Y
       Your Total Bill is 550 Rs.
       Bye

O/p 4: Enter Your Height (in feets): 5
       You can Ride
       What's Your Age: 19
       Pay 500 Rs.
       Do You want a Photo (Y/N): N
       Your Total Bill is 500 Rs.
       Bye

O/p 5: Enter Your Height (in feets): 2
       You can't Ride
       Bye
"""