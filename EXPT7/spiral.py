import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
color = ["orange", "yellow", "blue"]

for i in range(0, 500, 5):
    for j in color:
        t.pencolor(j)
        t.forward(10 + i)
        t.right(30)

turtle.done()
