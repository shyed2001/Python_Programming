import turtle
def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in range(4):
        t.forward(sz)
        #t.right(90)

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()      # Create tess and set some attributes
tess.pensize(3)
tess.speed(7)
size = 7                 # Size of the smallest square
for i in range(43):
    draw_multicolor_square(tess, size)
    size = size + 1     # Increase the size for next time
    tess.right(90)      #    and give her some turn
    #tess.penup()
    #tess.forward(10)        # Move tess along a little
    #tess.left(90)            #    and give her some turn
    #tess.forward(-10)        # Move tess along a little
   #tess.pendown()
                                         #    and give her some turn


wn.mainloop()

