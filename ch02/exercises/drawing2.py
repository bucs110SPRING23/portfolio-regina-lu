import turtle

sides = int(input('Enter the number of sides: '))
length = int(input('Enter the number of sides: '))

pen = turtle.Turtle()
pen.color('orange')

window = turtle.Screen()

for s in range(sides):
    pen.forward(length)
    pen.right(360/sides)

window.exitonclick()