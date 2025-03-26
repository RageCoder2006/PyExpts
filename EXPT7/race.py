import random
import time
import turtle

t1 = turtle.Turtle()
t1.pencolor("red")
t1.penup()
t1.goto(-100, 0)
t1.pendown()
t1tot = 0
t1.speed(1)
match = True

t2 = turtle.Turtle()
t2.pencolor("blue")
t2.penup()
t2.goto(-100, -10)
t2.pendown()
t2tot = 0


def move_forward():
    global t2tot
    t2.forward(50)
    t2tot += 50


screen = turtle.Screen()
screen.listen()
time.sleep(2)

while match:
    t1rand = random.randint(0, 10)
    t1tot += t1rand
    t1.forward(t1rand)
    screen.onkey(move_forward, "Right")

    if t1tot >= 100 or t2tot >= 100:
        match = False
        break
w
if t1tot >= 100:
    print("Red Won!")
else:
    print("Blue Won!")

turtle.done()
