import turtle

# simulate pen and paper
pen = turtle.Turtle()
pen2 = turtle.Turtle()
pen.shape('turtle')
pen2.shape('turtle')
pen2.color('purple')
pen.color('orange')
pen.speed(1)
pen2.speed(0)
window = turtle.Screen()
# variable = module.function()

pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)

pen2.fd(50)
pen2.left(5)
pen2.up()
pen2.fd(50)
pen2.left(5)
pen2.down()
pen2.fd(50)
pen2.left(5)
pen2.up()
pen2.fd(50)
pen2.left(5)
pen2.down()
pen2.fd(50)
pen2.left(5)
pen2.up()
pen2.fd(50)
pen2.left(5)
pen2.down()
pen2.fd(50)
pen2.left(5)
pen2.up()
pen2.fd(50)
pen2.left(5)
pen2.down()

# var = math.pi
pen2.home()
pen.goto(0,0)

# interface: what can I tell it to do
# state: value of all its attributes

var = [1, 2, 3, 4, 5]
var.append(6)  # will add to the end

# always must be the last turtle command
window.exitonclick()

## Pygame
# framework

# TOP OF THE FILE
import pygame

pygame.init()

screen = pygame.display.set_mode()

# screen: variable
# pygame: modules that contain modules are called frameworks
# display: submodule of pygame
# set_mode: function of the display submodule

screen.fill('red')
pygame.display.flip()
pygame.time.wait(2000)
screen.fill('blue')
pygame.display.flip()
pygame.time.wait(2000)
screen.fill('green')
pygame.display.flip()
pygame.time.wait(2000)

screen_size = screen.get_size()

# [x, y, width, height]
dimensions = [screen_size[0] / 2, screen_size[1] / 2, 250, 250]
pygame.draw.rect(screen, "red", dimensions)

pygame.draw.rect(screen, "red")
pygame.display.flip()
pygame.time.wait(5000)

