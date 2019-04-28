import turtle



def draw_equitriangle(t, sz):
    #"""Make turtle t draw a multi-color square of sz."""
        t.forward(sz)
        t.left(n)
        return t
tess = turtle.Turtle()      # Create tess and set some attributes
tess.pensize(3)
tess.speed(1)
wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

def draw_poly(t, n, sz):
    for i in range(3):
      t.forward(sz)
      t.left(n)

draw_poly(tess, 120, 50)


wn.mainloop()
