import turtle as t
t.shape('turtle')
t.pensize(3)
t.pencolor('#FF1493')


def circle():
    for i in range(360):
        t.forward(1)
        t.left(1)
    for i in range(360):
        t.forward(1)
        t.left(-1)


t.speed(1000)
circle()
t.left(60)
circle()
t.left(60)
circle()
t.exitonclick()
