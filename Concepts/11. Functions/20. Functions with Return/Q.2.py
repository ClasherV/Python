# Write a Program to Print Number of Days in a Month

def leapYear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def daysInMonth(year,month):
    days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    leapYear(year)
    if leapYear(year) and month==2:
        return 29
    else:
        return days_list[month-1]

def main():
    year=int(input("Enter the Year: "))
    month=int(input("Enter the Month: "))
    days=daysInMonth(year,month)
    print(f"Number of Days in Month {month} of Year {year} are: {days} Days")
main()