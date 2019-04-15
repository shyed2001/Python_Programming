import turtle

wn = turtle.Screen() # Turtle screen

print("#Creates a playground for turtle. Not must?")
tess=turtle.Turtle()    # Turtle assigned variables
alex=turtle.Turtle()    # Turtle assigned variables

alex.speed(1)
alex.pen()
alex.pendown()
alex.hideturtle()

alex.left(60)
alex.forward(100)
alex.right(150)
alex.forward(100)
alex.right(150)
alex.forward(100)
alex.right(140)
alex.forward(100)
alex.right(140)
alex.forward(100)
alex.right(140)

alex.speed(3)
alex.pensize(7)
alex.shape("arrow")
alex.color("blue")

alex.left(60)

alex.forward(100)
alex.right(145)
alex.forward(100)
alex.right(145)
alex.forward(100)
alex.right(145)
alex.forward(100)
alex.right(145)
alex.forward(100)
alex.right(145)

size=5
for i in range(30):
    tess.stamp()
    size=size+2
    tess.forward(size)
    tess.right(24)

tess.pendown()
tess.pensize(25)
tess.color("black")

for i in range(5):
    tess.forward(55)
    tess.right(72)


alex.speed(1)
alex.pen()
alex.pendown()
alex.hideturtle()

alex.forward(100)
alex.left(60)
for i in range(5):
    alex.forward(100)
    alex.right(150)


alex.speed(3)
alex.pensize(7)
alex.shape("arrow")
alex.color("blue")

alex.forward(100)
alex.left(60)

for i in range(5):
 alex.forward(100)
 alex.right(145)

alex.forward(100)
alex.speed(2)
alex.pensize(17)
alex.shape("turtle")
alex.color("red")
for i in range(12):
    #alex.penup()
    alex.stamp()
    alex.forward(77)
    alex.stamp()
    alex.backward(77)
    alex.right(30)
    alex.stamp()
alex.forward(-200)
alex.speed(2)
alex.pensize(37)
alex.shape("turtle")
alex.color("green")
for i in range(12):
    alex.penup()
    alex.stamp()
    alex.forward(77)
    alex.stamp()
    alex.backward(77)
    alex.right(30)
    alex.stamp()

alex.right(145)
alex.forward(50)
alex.speed(2)
alex.pensize(17)
alex.shape("turtle")
alex.color("red")
alex.penup()
alex.stamp()

for i in range(12):
    #alex.penup()
    #alex.stamp()
    alex.forward(77)
    alex.stamp()
    alex.backward(77)
    alex.right(30)
    #alex.stamp()
alex.forward(-300)
wn.mainloop()
