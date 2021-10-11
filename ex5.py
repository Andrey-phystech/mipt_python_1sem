import turtle

a = 10
x = 0
y = 0
turtle.shape('turtle')
for i in range(10):
    for j in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.penup()
    a += 10
    x -= 5
    y -= 5
    turtle.goto(x, y)
    turtle.pendown()
