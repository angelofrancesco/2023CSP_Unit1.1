#Pseudocode
'''Import turtle
    Draw pattern
        Draw a square at an angle
        Repeat code 6 times each having a different angle
    Draw flower
        Make painter pink
        Draw oval
        Every oval drawn next to each other moving in a circle
            Repeat code 6 times'''



#Drawing Flower Pattern
import turtle as trtl
painter = trtl.Turtle()
painter.speed(50)
painter.width(3)
painter.up()
painter.goto(-150, 50)
painter.down()
painter.left(30)
#The pattern
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
#The Flower
painter.pencolor("pink")
painter.width(5)
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
#Flower 2nd part
painter.up()
painter.goto(12, 14)
painter.down()
for line in range (3):
    for line in range(25):
        painter.left(2)
        painter.forward(4)
    painter.left(120)
    for line in range(25):
        painter.left(3)
        painter.forward(4.3)

wn = trtl.Screen()
wn.mainloop()