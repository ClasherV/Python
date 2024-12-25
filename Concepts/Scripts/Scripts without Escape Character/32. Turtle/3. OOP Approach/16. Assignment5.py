from turtle import Turtle,Screen
import random
gullu=Turtle()
gulluScreen=Screen()
gulluScreen.bgcolor("black")
gulluScreen.colormode(255)
gullu.width(10)
gullu.shape("turtle")
gullu.speed("fastest")
for _ in range(1000):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    gullu.pencolor((r,g,b))
    gullu.fillcolor("green")
    gullu.seth(random.randrange(0,360,90))
    gullu.fd(30)
gulluScreen.mainloop()