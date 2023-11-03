import turtle as trtl
painter = trtl.Turtle()
painter.speed(50)
painter.width(3)
painter.up()
painter.goto(-150, 50)
painter.down()
painter.left(30)
#Draw first layer
for line in range(6):
    for line in range(4):
        painter.forward(200)
        painter.right(90)
    for line in range(1):
        painter.forward(50)
        painter.left(60)
        painter.forward(50)
        for line in range(4):
            painter.right(90)
            painter.forward(200)
    for line in range(1):
        painter.right(90)
        painter.forward(50)
        painter.left(60)
        painter.forward(50)
        painter.right(90)
#Draw Flower
painter.right(30)
painter.up()
painter.goto(0, 0)
painter.down()

wn = trtl.Screen()
wn.mainloop()