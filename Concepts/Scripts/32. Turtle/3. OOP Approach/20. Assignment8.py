import random
import turtle
from turtle import Turtle,Screen
turtle.colormode(255)
gullu=Turtle()
gulluScreen=Screen()
gulluScreen.bgcolor("black")
print(gulluScreen.screensize())
gulluScreen.screensize(400,400)
print(gulluScreen.screensize())
gullu.penup()
gullu.speed(0)
color_list=[(16, 22, 47), (124, 92, 60), (47, 13, 34), (205, 149, 95), (181, 11, 56), (52, 40, 29), (241, 50, 89), (170, 45, 79), (175, 127, 70), (245, 224, 191)]
for _ in range(300):
    gullu.pencolor(random.choice(color_list))
    gullu.goto(random.randint(-300,300),random.randint(-300,300))
    gullu.dot(20)
gulluScreen.mainloop()