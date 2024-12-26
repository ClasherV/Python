from turtle import Turtle,Screen
import turtle
import random
turtle.colormode(255)
gullu=Turtle()
gulluScreen=Screen()
gulluScreen.bgcolor("black")
gullu.shape("turtle")
gullu.speed("fastest")
while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    gullu.pencolor((r,g,b))
    gullu.fillcolor("green")
    gullu.circle(100)
    gullu.lt(5)
    if gullu.heading()==0:
        break
gulluScreen.mainloop()