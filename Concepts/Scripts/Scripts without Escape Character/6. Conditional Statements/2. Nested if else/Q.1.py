number=int(input("Enter a Number: "))
if(number%2==0):
    print(f"Number {number} is Even")
    if(number>30):
        print(f"Number {number} is Greater than 30")
print("Bye")

"""
O/p 1: Enter a Number: 12
       Number 12 is Even
       Bye

O/p 2: Enter a Number: 32
       Number 32 is Even
       Number 32 is Greater than 30
       Bye

O/p 3: Enter a Number: 15
       Bye
"""