from turtle import Turtle,Screen
gullu=Turtle()
gulluScreen=Screen()
gulluScreen.bgcolor("black")
gullu.speed("fast")
gullu.color("red","yellow")
gullu.pu()
gullu.goto(-250,0)
gullu.pd()
gullu.begin_fill()
while True:
    gullu.fd(500)
    gullu.lt(170)
    if gullu.heading()==0:
        break
gullu.end_fill()
gulluScreen.mainloop()