import turtle as tr

tr.speed(0)

tr.begin_fill()
tr.circle(100)
tr.color("yellow")
tr.end_fill()

tr.penup()
tr.goto(-40, 130)
tr.color("black")
tr.pendown()
tr.begin_fill()
tr.circle(20)
tr.color("blue")
tr.end_fill()

tr.penup()
tr.goto(40, 130)
tr.color("black")
tr.pendown()
tr.begin_fill()
tr.circle(20)
tr.color("blue")
tr.end_fill()

tr.color("black")
tr.penup()
tr.goto(0, 110)
tr.pendown()
tr.width(10)
tr.goto(0, 90)

tr.color("red")
tr.penup()
tr.goto(40, 60)
tr.pendown()
tr.right(90)
tr.circle(-40, 180)
