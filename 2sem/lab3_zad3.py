import turtle as tu

v_ox = 40
v_oy = 70
tu.shape('circle')
tu.speed(10)
tu.pensize(3)
tu.penup()
tu.goto(-600, 0)
tu.pendown()
chi = 9.8/2

def parabola(v_ox, v_oy):
    t = 0
    i = (1 / chi) * v_oy
    x_o = tu.xcor()

    while t < i:
        x = x_o + v_ox * t
        y = v_oy * t - chi * t ** 2
        tu.goto(x, y)
        t += 0.05


for i in range(5):
    parabola(v_ox, v_oy)
    v_oy /= 1.3
    v_ox /= 1.7

tu.exitonclick()
