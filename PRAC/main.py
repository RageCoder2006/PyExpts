import turtle
t = turtle.Turtle()
t.speed(0)

class FlowerDrawer:
    def __init__(self,color):
        self.color = color

    def petal(self):
        t.color(self.color)
        t.begin_fill()
        t.right(120)
        t.forward(50)
        #curve
        for i in range(0, 50, 10):
            t.left(i)
            t.forward(5 + i / 10)
        for i in range(0, 40, 20):
            t.left(i)
            t.forward(5 + i)
        for i in range(0, 50, 10):
            t.left(i)
            t.forward(5 + i / 10)
        t.left(22.5)
        t.forward(60)
        t.end_fill()

    def draw(self):
        t.penup()
        t.goto(20,85)
        t.pendown()
        for i in range(0,4):
            self.petal()
            t.penup()
            t.right(30)
            t.forward(5)
            t.pendown()

        #adjusting centre circle pos
        t.penup()
        t.forward(15)
        t.left(90)
        t.forward(10)
        t.pendown()
        t.fillcolor("chartreuse3")
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        turtle.done()

f = FlowerDrawer("chartreuse4")
f.draw()