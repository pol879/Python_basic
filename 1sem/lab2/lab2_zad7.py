import turtle as t
import math
t.shape("turtle")
x = 0
while x < 7:
    t.forward(x/2*math.pi)
    t.left(2*math.pi)
    x += 0.01
t.exitonclick()

