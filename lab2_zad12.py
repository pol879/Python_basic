import turtle as t
t.shape('turtle')
t.pensize(5)
t.pencolor('#556B2F')
t.left(90)


def half_circle(l):
    for i in range(180):
        t.forward(l)
        t.right(1)


t.speed(100)
for j in range(4):
    half_circle(1)
    half_circle(0.3)
half_circle(1)
t.exitonclick()
