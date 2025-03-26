import turtle

tout = turtle.Turtle()
tout.speed(0)


def square(n):
    for _ in range(4):
        tout.forward(n)
        tout.left(90)


colors = ["chartreuse3", "DarkSlateGray3"]

for j in range(10):
    for i in range(10):
        tout.fillcolor(colors[(i + j) % 2])
        tout.begin_fill()
        tout.penup()
        tout.goto(10 * i, 10 * j)
        tout.pendown()
        square(10)
        tout.end_fill()

turtle.done()
