import turtle

class Num:
    def __init__(self, n):
        self.data = n #instance variables for Num type objects
        self.x = "string"
    
    #double under
    def __str__(self):
        

    def addone(self):
        self.data += 1

def main():
    mynum = Num(7)
    mynum2 = Num(9)
    mynum3 = {'data', }

    print(mynum.data)
    print(mynum2.data)
    print(mynum3['data', "x", "string"])
    print(mynum('date'))

    t = turtle.Turtle()
    t.forward(56)

    mylist =[]
    mylist.fowrard() #arrow
    mylist.append()
    mylist.remove(index())

main()