import turtle as t
import random
t.shape('turtle')
t.pensize(3)
t.pencolor('red')
c = 0
while c < 100:
    t.speed(10)
    t.left(random.randint(0, 360))
    t.forward(random.randint(1, 100))
    c += 1
t.exitonclick()