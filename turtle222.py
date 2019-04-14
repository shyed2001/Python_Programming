print("""

import turtle

wn = turtle.Screen()

print("#Creates a playground for turtle. Not must?")
tess=turtle.Turtle()
alex=turtle.Turtle()

alex.pen()
alex.backward(30)
alex.penup()
alex.right(-60)
alex.forward(-45)
alex.pendown()
alex.left(-30)
alex.backward(-20)
alex.penup()
alex.forward(-45)
alex.pendown()
alex.left(30)

tess.color('red')
tess.pensize(13)
tess.forward(-80)
tess.penup()
tess.stamp()
tess.forward(80)
tess.penup()
tess.forward(-80)
tess.penup()
alex.color('yellow')
alex.pensize(25)

for i in range (3):
    alex.forward(80)
    alex.right(90)
for i in [0,1,2,3]:
    tess.shape("square")
    tess.backward(55)
    tess.right(90)

alex.color('green')
alex.pensize(51)

for i in range (3):
    alex.speed(10)
    alex.forward(130)
    alex.right(120)

tess.color('blue')
tess.pensize(51)
for i in ("a","b","c"):
    tess.shape("circle")
    tess.speed(1)
    tess.forward(120)
    tess.right(120)
for i in ("a","b","c"):
    tess.shape("circle")
    tess.speed(0)
    tess.forward(120)
    tess.stamp()
    tess.right(-120)
for c in ["dark green", "red", "yellow", "black"]:
    alex.color(c)
    alex.speed(5)
    alex.forward(-380)
    alex.right(120)
tc= ["black", "light green", "orange", "pink"]
for c in tc:
    tess.shape("arrow")
    tess.color(c)
    tess.forward(100)
    tess.stamp()
    tess.right(120)
tc= ["black", "light green", "orange", "pink"]
for c in tc:
    tess.shape("arrow")
    tess.pendown()
    tess.color(c)
    tess.forward(-100)
    tess.right(120)
for i in [0,1,2,3]:
    tess.forward(-30)
    tess.penup()
    tess.forward(30)
    tess.stamp()
    tess.pendown()
    tess.shape("turtle")
    tess.forward(-28)
    tess.stamp()
    tess.right(90)
tess.shape("turtle")
tess.forward(30)
for i in [0,1,2,3]:
    tess.forward(30)
    tess.pensize(5)
    tess.penup()
    tess.forward(-30)
    #tess.pendown()
    tess.shape("turtle")
    tess.forward(-28)
    tess.right(90)
    tess.stamp()
tess.shape("turtle")
tess.penup()
tess.stamp()
tess.speed(3)
tess.right(90)
tess.forward(230)
tess.stamp()
tess.right(90)
tess.speed(10)
tess.right(90)
tess.backward(-130)
tess.stamp()
tess.right(90)
tess.speed(1)
tess.forward(-130)
tess.stamp()
wn.mainloop()
""")

import turtle

wn = turtle.Screen()

print("#Creates a playground for turtle. Not must?")
tess=turtle.Turtle()
alex=turtle.Turtle()

alex.pen()
alex.backward(30)
alex.penup()
alex.right(-60)
alex.forward(-45)
alex.pendown()
alex.left(-30)
alex.backward(-20)
alex.penup()
alex.forward(-45)
alex.pendown()
alex.left(30)

tess.color('red')
tess.pensize(13)
tess.forward(-80)
tess.penup()
tess.stamp()
tess.forward(80)
tess.penup()
tess.forward(-80)
tess.penup()
alex.color('yellow')
alex.pensize(25)

for i in range (3):
    alex.forward(80)
    alex.right(90)
for i in [0,1,2,3]:
    tess.shape("square")
    tess.backward(55)
    tess.right(90)

alex.color('green')
alex.pensize(51)

for i in range (3):
    alex.speed(10)
    alex.forward(130)
    alex.right(120)

tess.color('blue')
tess.pensize(51)
for i in ("a","b","c"):
    tess.shape("circle")
    tess.speed(1)
    tess.forward(120)
    tess.right(120)
for i in ("a","b","c"):
    tess.shape("circle")
    tess.speed(0)
    tess.forward(120)
    tess.stamp()
    tess.right(-120)
for c in ["dark green", "red", "yellow", "black"]:
    alex.color(c)
    alex.speed(5)
    alex.forward(-380)
    alex.right(120)
tc= ["black", "light green", "orange", "pink"]
for c in tc:
    tess.shape("arrow")
    tess.color(c)
    tess.forward(100)
    tess.stamp()
    tess.right(120)
tc= ["black", "light green", "orange", "pink"]
for c in tc:
    tess.shape("arrow")
    tess.pendown()
    tess.color(c)
    tess.forward(-100)
    tess.right(120)
for i in [0,1,2,3]:
    tess.forward(-30)
    tess.penup()
    tess.forward(30)
    tess.stamp()
    tess.pendown()
    tess.shape("turtle")
    tess.forward(-28)
    tess.stamp()
    tess.right(90)
tess.shape("turtle")
tess.forward(30)
for i in [0,1,2,3]:
    tess.forward(30)
    tess.pensize(5)
    tess.penup()
    tess.forward(-30)
    #tess.pendown()
    tess.shape("turtle")
    tess.forward(-28)
    tess.right(90)
    tess.stamp()
tess.shape("turtle")
tess.penup()
tess.stamp()
tess.speed(3)
tess.right(90)
tess.forward(230)
tess.stamp()
tess.right(90)
tess.speed(10)
tess.right(90)
tess.backward(-130)
tess.stamp()
tess.right(90)
tess.speed(1)
tess.forward(-130)
tess.stamp()

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

wn.mainloop()

