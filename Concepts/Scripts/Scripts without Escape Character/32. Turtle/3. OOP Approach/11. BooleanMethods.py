from turtle import Turtle,Screen
a=Turtle()
a.shape("turtle")
a.speed(10)
a.color("red","green")
a.begin_fill()
a.circle(100)
a.end_fill()
a.rt(90)
a.penup() # pu(), up()
print(a.isdown())
a.fd(100)
a.pendown() # pd(), down()
print(a.isdown())
a.hideturtle()
print(a.isvisible())
a.pensize(5)
a.color("green","orange")
a.begin_fill()
a.circle(50)
a.end_fill()
print(a.pos())
a.goto(-100,-100) # setposition(x,y) or setpos(x,y)
a.showturtle()
print(a.isvisible())
a.screen.mainloop()