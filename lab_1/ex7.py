import turtle
import math

turtle.shape('turtle')
for phi in range(1000):
    x = 1 * (phi / 10) * math.cos(phi / 10)
    y = 1 * (phi / 10) * math.sin(phi / 10)
    turtle.goto(x, y)
