import turtle as tr
import math

def polygon(n, r):
    tr.penup()
    tr.goto(r, 0)
    tr.pendown()
    for i in range(1, n + 1):
        tr.goto(r * math.cos(2 * math.pi * i / n),
                r * math.sin(2 * math.pi * i / n))

r = 15
for i in range(3, 13):
    polygon(i, r)
    r += 15
    tr.penup()
    tr.goto(r, 0)
    tr.pendown()
