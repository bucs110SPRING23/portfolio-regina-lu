import turtle

window = turtle.Screen()
x = turtle.Turtle()

def main():
    def square(side_length):  #draws a square, the parameter takes in the side length
        for _ in range(4):
            x.forward(side_length)
            x.right(90)

    fibo_nums = [1,1,2,3,5,8,13,21,34,55]
    num_squares = len(fibo_nums)   #the number of squares that need to be drawn = the # of Fibonacci numbers

    x.penup()  #does not want the turtle to draw anything as it changes its starting location
    x.goto(0,75)  #played around with numbers to make sure that the whole image can be seen
    x.pendown()  #pen down after the turtle is in position

    factor = 5  
    for num in range(num_squares):
        square(factor * fibo_nums[num]) #calls the square function and draws the square with a side length equal to 5 times the Fibonacci numbers
        #this way, the original lengths of 1 (the first two Fibonacci numbers can be seen)
        x.penup()
        x.forward(factor * fibo_nums[num]) 
        x.right(90)
        x.forward(factor * fibo_nums[num]) 
        #the two .forward() with the .right() in between moves the turtle two sides over, reorienting the turtle so that it can draw the next adjacent square
        x.pendown()  #pen down after turtle is in the right position to draw the next square

    #Bring pen back to its starting location
    x.penup() #lifts the pen so that it won't draw as it moves to the starting box
    x.goto(0,75) #goes back to the starting position
    x.setheading(0)  #sets the orientation of the turtle to an angle (0 = east)
    x.pencolor("red") #sets the color of the pen to red so the spiral will be drawin in red
    x.pensize(3) #the thickness of the line size
    x.pendown() #pen down after the turtle is in position

    #Drawing the sprial (quarter circle in each box)
    for fibo in range(num_squares):
        x.circle(-factor * fibo_nums[fibo], 90)   #(radius, degrees of the arc)
        # negative sign in front of factor to draw clockwise

main()