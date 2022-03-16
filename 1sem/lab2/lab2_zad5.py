import turtle as t
import numpy as np
t.shape('turtle')
x = 25
for j in range(10):
    for i in range(4):
        t.forward(x)
        t.left(90)
    if j != 9:
        t.right(135)
        t.penup()
        t.forward(25*np.sqrt(2))
        t.left(135)
        t.pendown()
        x += 50
t.hideturtle()
t.exitonclick()
