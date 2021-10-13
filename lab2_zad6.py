import turtle as t
n = int(input())
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.stamp()
    t.left(180)
    t.forward(100)
    t.right(180 - int(360/n))

t.exitonclick()
