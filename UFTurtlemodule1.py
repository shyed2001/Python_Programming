#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     27/04/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle
def draw_turtlr_square(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        t.stamp()

wn=turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("turtle function")
alex=turtle.Turtle()
draw_turtlr_square(alex,255)
def draw_turtlr_square(t,sz,a):
    for i in range(4):
        t.forward(sz)
        t.left(a)
        t.stamp()

wn=turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("turtle function")
alex=turtle.Turtle()
draw_turtlr_square(alex,255,90)
def draw_mc_sq(t,sz):
     for i in ["red", "blue", "purple", "black", "orange"]:
         t.color(i)
         t.forward(sz)
         t.left(90)

tess=turtle.Turtle()
tess.pensize(7)
size=177
for i in range (7):
    draw_mc_sq(tess,size)
    size=size+1
    tess.forward(10)
    tess.left(77)

wn.mainloop()

