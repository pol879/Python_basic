import turtle as t
import math
t.shape('turtle')
grad = math.pi / 180
t.pensize(2)
t.pencolor('#0000CD')


def star(n, R):
    global grad
    beta = grad*(180 - 180/n)
    l = R*math.sqrt(2-2*math.cos(beta))
    t.right(90 - 90 / n)
    for i in range(n):
        t.forward(l)
        t.right(180 - 180/n)
    t.left(90 - 90/n)


# 1st star
t.penup()
t.goto(-200, 100)
t.pendown()
star(5, 100)
# 2nd star
t.penup()
t.forward(400)
t.pendown()
star(11, 100)

t.exitonclick()

