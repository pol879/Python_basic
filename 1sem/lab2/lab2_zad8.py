import turtle as t
t.shape("turtle")
x = 1
while x < 50:
    t.forward(20*x)
    t.left(90)
    x += 1
t.exitonclick()
