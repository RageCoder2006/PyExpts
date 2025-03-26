import turtle

tout = turtle.Turtle()
tin = turtle.Turtle()
tin1 = turtle.Turtle()

for i in range(4):
    tout.forward(100)
    tout.left(90)

for j in range(5):
    tin.forward(10)
    tin.left(90)
    tin.forward(100)
    tin.right(90)
    tin.forward(10)
    tin.right(90)
    tin.forward(100)
    tin.left(90)

for k in range(5):
    tin1.forward(100)
    tin1.left(90)
    tin1.forward(10)
    tin1.left(90)
    tin1.forward(100)
    tin1.right(90)
    tin1.forward(10)
    tin1.right(90)

turtle.done()
