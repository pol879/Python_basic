import turtle as t
t.shape('turtle')
t.pensize(3)
t.pencolor('#00F5FF')


def circle(l):
    for i in range(360):
        t.forward(l)
        t.left(1)
    for i in range(360):
        t.forward(l)
        t.left(-1)


t.left(90)
n = 1
for j in range(10):
    t.speed(100)
    circle(n)
    n += 0.1
t.exitonclick()
