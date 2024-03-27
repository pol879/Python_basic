import turtle as t
import numpy as np
s = str(141700)
t.shape('turtle')
t.pensize(5)
t.pencolor('#104E8B')
d = 50*np.sqrt(2)

# number 0
def zero():
    t.pendown()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.penup()
    t.left(180)
    t.forward(80)


# number 1
def one():
    t.penup()
    t.right(90)
    t.forward(50)
    t.left(135)
    t.pendown()
    t.forward(d)
    t.right(135)
    t.forward(100)
    t.penup()
    t.left(180)
    t.forward(100)
    t.right(90)
    t.forward(30)


# number 2
def two():
    t.pendown()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(45)
    t.forward(d)
    t.left(135)
    t.forward(50)
    t.penup()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(30)


# number 3
def three():
    t.pendown()
    t.forward(50)
    t.right(135)
    t.forward(d)
    t.left(135)
    t.forward(50)
    t.right(135)
    t.forward(d)
    t.penup()
    t.left(180)
    t.forward(d)
    t.left(45)
    t.forward(50)
    t.right(90)
    t.forward(30)


# number 4
def four():
    t.pendown()
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.penup()
    t.left(180)
    t.forward(50)
    t.pendown()
    t.forward(50)
    t.penup()
    t.right(90)
    t.forward(30)


# number 5
def five():
    t.penup()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.pendown()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.penup()
    t.forward(30)


# number 6
def six():
    t.penup()
    t.right(90)
    t.forward(50)
    t.pendown()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(135)
    t.forward(d)
    t.penup()
    t.right(45)
    t.forward(30)


# number 7
def seven():
    t.pendown()
    t.forward(50)
    t.right(135)
    t.forward(d)
    t.left(45)
    t.forward(50)
    t.penup()
    t.left(180)
    t.forward(50)
    t.right(45)
    t.forward(d)
    t.right(45)
    t.forward(30)


list_of_f = [zero, one, two, three, four, five, six, seven]

for i in range(len(s)):
    for j in range(len(list_of_f)):
        if int(s[i]) == j:
            list_of_f[j]()
t.exitonclick()


