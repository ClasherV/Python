from turtle import Turtle,Screen
gullu=Turtle()
gullu.color("white")
screen=Screen()
screen.bgcolor("black")
def up():
    gullu.seth(90)
def down():
    gullu.seth(270)
def left():
    gullu.seth(180)
def right():
    gullu.seth(0)
def move():
    gullu.fd(20)
def clr():
    gullu.clear()
    gullu.penup()
    gullu.home()
    gullu.pendown()
screen.listen()
screen.onkey(fun=up,key="Up")
screen.onkey(fun=down,key="Down")
screen.onkey(fun=left,key="Left")
screen.onkey(fun=right,key="Right")
screen.onkey(fun=move,key="space")
screen.onkey(fun=clr,key="c")
screen.mainloop()