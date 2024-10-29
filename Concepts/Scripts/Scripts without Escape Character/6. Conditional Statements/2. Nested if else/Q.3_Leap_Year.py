# Write a Program to find whether the Entered Year is a Leap Year or not

year=int(input("Enter the Year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"Given Year {year} is a Leap Year")
        else:
            print(f"Given Year {year} is not a Leap Year")
    else:
        print(f"Given Year {year} is a Leap Year")
else:
    print(f"Given Year {year} is not a Leap Year")

"""
O/p 1: Enter the Year: 2000
       Given Year 2024 is a Leap Year

O/p 2: Enter the Year: 3000
       Given Year 3000 is not a Leap Year
    
O/p 3: Enter the Year: 2024
       Given Year 2024 is a Leap Year

O/p 4: Enter the Year: 2023
       Given Year 2023 is not a Leap Year
"""