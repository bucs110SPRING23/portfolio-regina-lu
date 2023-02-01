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