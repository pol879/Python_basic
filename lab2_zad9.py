import turtle as t
import math
n = 3
R = 30
Rs = 30
grad = math.pi / 180
t.shape('turtle')
t.pensize(3)
t.pencolor('#191970')


def polygon(n, storona, angle_outside):
    for i in range(n):
        t.forward(storona)
        t.left(angle_outside)


for j in range(10):
    angle_inside = 180*(n-2)/n
    angle_outside = 360/n
    rotation_angle = (360 - angle_inside)//2
    storona = 2*Rs*math.cos(angle_inside*grad/2)
    # turtle part
    t.penup()
    t.forward(R)
    t.left(rotation_angle)
    t.pendown()
    polygon(n, storona, angle_outside)
    t.right(rotation_angle)
    n += 1
    Rs += 30

t.exitonclick()
