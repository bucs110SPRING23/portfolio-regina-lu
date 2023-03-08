import turtle
import random

screen = turtle.Screen()
turtlemain = turtle.Turtle()
(x_pos, y_pos) = screen.screensize()
xpos = x_pos / 2
ypos = y_pos / 2
(turtle_xpos, turtle_ypos) = turtlemain.pos()
turtlex = abs(turtle_xpos)
turtley = abs(turtle_ypos)

turtlemain.penup()
turtlemain.goto(0,0)

def flipcoin():
    return(random.choice(["Heads","Tails"]))

while turtlex <= xpos and turtley <= ypos:
    flipcoin()
    if flipcoin() == "Heads":
        turtlemain.left(90)
        turtlemain.forward(50)
    elif flipcoin() == "Tails":
        turtlemain.right(90)
        turtlemain.forward(50)

screen.exitonclick()