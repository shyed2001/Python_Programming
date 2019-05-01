import turtle

wn = turtle.Screen() # Turtle screen

print("#Creates a playground for turtle. Not must?")
#tess=turtle.Turtle()    # Turtle assigned variables
alex=turtle.Turtle()    # Turtle assigned variables

alex.speed(3)
alex.pen()
alex.pendown()
alex.hideturtle()
alex.forward(-150)
#alex.left(60)
for i in range (5):
    alex.forward(77)
    alex.right(144)
"""alex.forward(100)
alex.right(144)
alex.forward(100)
alex.right(144)
alex.forward(100)
alex.right(144)
alex.forward(100)
alex.right(144)"""
alex.penup()
alex.forward(150)
alex.right(144)
alex.pendown()


alex.left(60)
def draw_star(alex,l,a):
    for i in range (5):
        #alex=turtle.Turtle()   <== this will create error
        alex.forward(l)
        alex.right(a)
    return alex

alex.speed(3)
alex.pensize(7)
alex.shape("arrow")
alex.color("blue")

for i in range(5):
   l=77
   a=144
   draw_star(alex,l,a)
   alex.penup()
   alex.forward(199)
   alex.right(144)
   alex.pendown()

"""alex.forward(100)
alex.right(145)
alex.forward(100)
alex.right(145)
alex.forward(100)
alex.right(145)
alex.forward(100)
alex.right(145)"""
alex.forward(150)
alex.penup()
alex.forward(150)
alex.right(144)
alex.pendown()
alex.speed(3)
alex.pensize(2)
alex.shape("arrow")
alex.color("yellow")
def draw_star(alex,l,a):
    for i in range (5):
        #alex=turtle.Turtle()   <== this will create error
        alex.forward(l)
        alex.right(a)
    return alex

for i in range(5):
   l=77
   a=144
   draw_star(alex,l,a)
   #alex.penup()
   alex.forward(299)
   alex.right(144)
   #alex.pendown()
wn.mainloop()