from turtle import Turtle,Screen
gullu=Turtle()
gullu.color("white")
screen=Screen()
screen.bgcolor("black")
def move_forward():
    gullu.fd(10)
def move_backward():
    gullu.backward(10)
def turn_left():
    new_heading=gullu.heading()+20
    gullu.seth(new_heading)
    gullu.fd(10)
def turn_right():
    new_heading=gullu.heading()-20
    gullu.seth(new_heading)
    gullu.fd(10)
def clr():
    gullu.clear()
    gullu.pu()
    gullu.home()
    gullu.pd()
screen.listen()
screen.onkey(fun=move_forward,key="Up")
screen.onkey(fun=move_backward,key="Down")
screen.onkey(fun=turn_left,key="Left")
screen.onkey(fun=turn_right,key="Right")
screen.onkey(fun=clr,key="c")
screen.mainloop()