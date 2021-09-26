import turtle

n = int(input())
turtle.shape('turtle')
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.right(360 / n)
