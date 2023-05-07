from Rectangle import Rectangle

class Surface():
    def __init__(self, filename, x, y, h, w):
        self.image = str(filename)
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)

        self.rect = Rectangle(x,y,h,w)

    def getRect(self):
        return self.rect