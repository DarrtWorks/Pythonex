import turtle
t = turtle.Turtle()
n = 70
for i in range(20):
    t.circle(n)
    n = n -20
    t.left(1)
    t.forward(1)