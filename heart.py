import turtle
t=turtle.Turtle()
def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)
turtle.bgcolor("black")
t.color("red","red")
t.begin_fill()
t.left(140)
t.forward(111.65)
curve()
t.left(120)
curve()
t.forward(111.65)
t.end_fill()
turtle.done()