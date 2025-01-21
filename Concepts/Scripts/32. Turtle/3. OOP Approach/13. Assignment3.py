from turtle import Turtle,Screen
gullu=Turtle()
gulluScreen=Screen()
gulluScreen.bgcolor("black")
gullu.color("white","red")
gullu.pu()
gullu.hideturtle()
gullu.goto(-200,0)
gullu.showturtle()
i=1
while i!=10:
    gullu.pu()
    gullu.fd(25)
    gullu.pd()
    gullu.fd(25)
    i+=1
gulluScreen.mainloop()