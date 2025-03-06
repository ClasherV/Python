import random
from turtle import Turtle,Screen
gullu=Turtle()
gulluScreen=Screen()
gulluScreen.bgcolor("black")
gullu.pensize(5)
colors=["red","green","pink","orange","blue","gray","alice blue","aquamarine","brown","burlywood","chocolate1","cyan","beige","blanched almond","blue4"]
for i in range(3,11):
    angle=360/i
    gullu.pencolor(random.choice(colors))
    for _ in range(i):
        gullu.fd(100)
        gullu.lt(angle)
gullu.screen.mainloop()