from turtle import Turtle,Screen
import random

WIDTH,HEIGHT=500,500
screen=Screen()
screen.setup(500,500)
screen.bgcolor("black")
color_list=["red","orange","yellow","green","blue","indigo","violet","pink","cyan","purple"]

def no_of_turtles():
    count=0
    while True:
        count=input("Enter the Number of Turtles (2 to 10): ")
        if count.isdigit():
            count=int(count)
        else:
            print("Invalid Input")
            continue
        if 2<=count<=10:
            return count
        else:
            print("Input out of Range!!...Try Again")
turtles=no_of_turtles()
print(turtles)

x_spacing=WIDTH//(turtles+1)
turtle_list=[]
for i in range(1,turtles+1):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.speed("slowest")
    new_turtle.left(90)
    new_turtle.color(color_list[i-1])
    new_turtle.penup()
    new_turtle.goto(-WIDTH//2+(i*x_spacing),-HEIGHT//2+30)
    turtle_list.append(new_turtle)

def race():
    is_race_on=True
    while is_race_on:
        for t in turtle_list:
            distance=random.randrange(1,20)
            t.forward(distance)
            x,y=t.pos()
            if y>=HEIGHT//2-30:
                print(f"The Winner is {t.pencolor()} Turtle")
                is_race_on=False
race()
screen.mainloop()