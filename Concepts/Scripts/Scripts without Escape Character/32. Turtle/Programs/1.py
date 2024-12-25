import turtle
i=True
turtle.speed("fastest")
while i!=150:
    turtle.fd(i)
    turtle.circle(i)
    turtle.lt(90)
    turtle.circle(i)
    turtle.fd(i)
    turtle.circle(i)
    turtle.lt(90)
    turtle.circle(i)
    turtle.fd(i)
    turtle.circle(i)
    turtle.lt(90)
    turtle.circle(i)
    turtle.fd(i)
    turtle.circle(i)
    i+=1
    # if i==50:
    #     i=75
    # elif i==100:
    #     i==51
turtle.mainloop()