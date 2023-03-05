# Part A
import random

x = random.randrange(1,10)
print(x)

import turtle
window = turtle.Screen()

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

turtle1.goto(-100, 20)
turtle2.goto(-100, -20)

# Race 1
turtle1.forward(x)
turtle2.forward(x)

turtle1.goto(-100, 20)
turtle2.goto(-100, -20)

# Race 2


turtle1.goto(-100, 20)
turtle2.goto(-100, -20)

window.exitonclick()

# Part B
import math
import pygame
pygame.init()
window = pygame.display.set_mode()


