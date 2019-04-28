import turtle
def draw_poly(t, n, sz):
    for i in range(7):
        t.left(51)
        t.forward(sz)


wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()      # Create tess and set some attributes
tess.pensize(3)
tess.speed(3)

draw_poly(tess, 8, 50)

wn.mainloop()


