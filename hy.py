import turtle
turtle.goto(400,0)
turtle.goto(-300,0)
turtle.speed(10)
vx = 1.7
a = 1.2
vy = 17
y = 0
x = -300
for i in range(1000):
    vy -= a
    if y + vy < 0:
        y = vy
        vy = -vy
    turtle.goto(x + vx, y + vy)
    x = turtle.xcor()
    y = turtle.ycor()
