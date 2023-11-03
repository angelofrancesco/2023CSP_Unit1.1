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
painter.pencolor("pink")
painter.up()
painter.goto(15, 10)
painter.down()
for line in range (3):
    for line in range(25):
        painter.right(2)
        painter.forward(4)
    painter.right(120)
    for line in range(25):
        painter.right(3)
        painter.forward(4.3)

wn = trtl.Screen()
wn.mainloop()