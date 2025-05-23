# Write a Program to find out how many Days, Weeks, Months we have left, if we live until 90 Years old (Year=365 Days)

age=int(input("Enter Your Age: "))
years=90-age
months=years*12
weeks=years*52
days=years*365
print(f"Days left: {days}\nWeeks Left: {weeks}\nMonths Left: {months}\nYears Left: {years}")

"""
O/p: Enter Your Age: 19
     Days left: 25915
     Weeks Left: 3692
     Months Left: 852
     Years Left: 71
"""