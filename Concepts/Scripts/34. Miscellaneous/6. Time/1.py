import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
Hours=int(time.strftime('%H'))
print(Hours)
if 6<=Hours<=12:
    print("Good Morning")
elif 12<Hours<=18:
    print("Good Afternoon")
elif 18<Hours<=0:
    print("Good Evening")
elif 0<Hours<6:
    print("Good Night")