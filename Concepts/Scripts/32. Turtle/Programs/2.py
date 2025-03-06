from turtle import Turtle,Screen
gullu=Turtle()
gullu.shape("turtle")
gullu.speed("fastest")
i=0
while i!=200:
    gullu.color("green","yellow")
    gullu.fd(i)
    gullu.begin_fill()
    gullu.circle(i)
    gullu.end_fill()
    gullu.lt(90)
    gullu.circle(i)
    gullu.fd(i)
    gullu.circle(i)
    gullu.lt(90)
    gullu.circle(i)
    gullu.fd(i)
    gullu.circle(i)
    gullu.lt(90)
    gullu.circle(i)
    gullu.fd(i)
    i+=1
gullu.screen.mainloop()