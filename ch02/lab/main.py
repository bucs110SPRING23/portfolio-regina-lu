# Part A
import random

import turtle
window = turtle.Screen()

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.speed(1)
turtle2.speed(1)
turtle1.penup()
turtle2.penup()

turtle1.goto(-100, 20)
turtle2.goto(-100, -20)

# Race 1
turtle1.forward(random.randrange(1,101))
turtle2.forward(random.randrange(1,101))

turtle1.goto(-100, 20)
turtle2.goto(-100, -20)

# Race 2
for x in range(0, 10):
    turtle1.forward(random.randrange(1,11))
    turtle2.forward(random.randrange(1,11))

turtle1.goto(-100, 20)
turtle2.goto(-100, -20)

window.exitonclick()

# Part B
import math
import pygame
pygame.init()
window = pygame.display.set_mode()

window.fill("red")
pygame.display.flip()
pygame.time.wait(2000)

# Triangle
points = []
num_sides = 3
side_length = 50
xpos = 200
ypos = 200

for i in range(0, num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(window, "white", points)
pygame.display.flip()
pygame.time.wait(2000)

window.fill("blue")
pygame.display.flip()
pygame.time.wait(2000)

# Square
points = []
num_sides = 4
side_length = 50
xpos = 200
ypos = 200

for i in range(0, num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(window, "white", points)
pygame.display.flip()
pygame.time.wait(2000)

window.fill("purple")
pygame.display.flip()
pygame.time.wait(2000)

# Hexagon (6 sides)
points = []
num_sides = 6
side_length = 50
xpos = 200
ypos = 200

for i in range(0, num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(window, "white", points)
pygame.display.flip()
pygame.time.wait(2000)

window.fill("orange")
pygame.display.flip()

# Icosagon (20 sides)
points = []
num_sides = 20
side_length = 50
xpos = 200
ypos = 200

for i in range(0, num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(window, "white", points)
pygame.display.flip()
pygame.time.wait(2000)

window.fill("green")
pygame.display.flip()

# Hectagon (100 sides)
points = []
num_sides = 100
side_length = 50
xpos = 200
ypos = 200

for i in range(0, num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(window, "white", points)
pygame.display.flip()
pygame.time.wait(2000)

window.fill("yellow")
pygame.display.flip()

# circle -ish (360 sides)
points = []
num_sides = 360
side_length = 50
xpos = 200
ypos = 200

for i in range(0, num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])

pygame.draw.polygon(window, "white", points)
pygame.display.flip()
pygame.time.wait(2000)