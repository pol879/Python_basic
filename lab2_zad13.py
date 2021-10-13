import turtle as t
t.shape('turtle')
t.pensize(3)


def circle(l):
    for i in range(360):
        t.forward(l)
        t.left(1)


def half_circle(l):
    for i in range(180):
        t.forward(l)
        t.left(1)


t.speed(100)
t.right(90)
t.fillcolor('#FFDEAD')
t.begin_fill()
circle(2)
t.end_fill()
# mouth
t.left(90)
t.penup()
t.forward(40)
t.right(90)
t.pendown()
t.pensize(7)
t.pencolor('#B22222')
half_circle(1.3)
# nose
t.penup()
t.left(90)
t.forward(75)
t.right(90)
t.forward(5)
t.pendown()
t.pencolor('black')
t.forward(30)
# 1st eye
t.penup()
t.left(90)
t.forward(40)
t.left(180)
t.pendown()
t.fillcolor('#FFFFFF')
t.begin_fill()
circle(0.3)
t.end_fill()
# 2nd eye
t.penup()
t.forward(80)
t.pendown()
t.fillcolor('#FFFFFF')
t.begin_fill()
circle(0.3)
t.end_fill()

t.exitonclick()
