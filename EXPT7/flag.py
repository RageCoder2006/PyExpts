import turtle

t = turtle.Turtle()


def flagborder():
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(75)
        t.left(90)


def japan():
    flagborder()
    t.penup()
    t.goto(-160, 12.5)
    t.pendown()
    t.fillcolor("DarkRed")
    t.begin_fill()
    t.circle(25)
    t.end_fill()


def bangladesh():
    t.fillcolor("DarkGreen")
    t.penup()
    t.goto(-50, 0)

    t.pendown()
    t.begin_fill()
    flagborder()
    t.end_fill()
    t.penup()
    t.goto(0, 12.5)
    t.pendown()
    t.fillcolor("DarkRed")
    t.begin_fill()
    t.circle(25)
    t.end_fill()


def france():
    flagborder()
    t.penup()
    t.goto(110, 0)
    t.pendown()
    t.fillcolor("DarkBlue")
    t.begin_fill()
    t.left(90)
    t.forward(75)
    t.right(90)
    t.forward(33.3)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(33.3)
    t.end_fill()
    t.penup()
    t.goto(176.6, 0)
    t.pendown()

    t.fillcolor("DarkRed")
    t.begin_fill()
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(33.3)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(33.3)
    t.end_fill()


t.penup()
t.goto(-210, 0)
t.pendown()
japan()

t.penup()
t.goto(-110, 0)
t.pendown()
bangladesh()

t.penup()
t.goto(110, 0)
t.pendown()
france()

turtle.done()
