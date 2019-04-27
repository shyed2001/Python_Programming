import turtle
__import__("turtle").__traceable__= False
print("""
import turtle
Set up the window with the given background color and title.
Returns the new window.
def make_window(color, title):

  window = turtle.Screen()
  window.bgcolor(color)
  window.title(title)
  return window
""")
def make_window(color, title):

  window = turtle.Screen()
  window.bgcolor(color)
  window.title(title)
  return window
print("""
def make_turtle(color, size, right, forward):
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    animal.right( right)
    animal.forward(forward)
    return animal

wn = make_window("lightgreen", "Tess and Alex dancing")
tess = make_turtle("hotpink", 5, 0, 25)
#tess.forward(5)
alex = make_turtle("black", 3, -35, 43)
#alex.right(45)
#alex.forward(45)
dave = make_turtle("yellow", 7, 55, -34)
#dave.left(45)
#dave.forward(45)
wn.mainloop()
""")
def make_turtle(shape, color, size, right, forward):
    animal = turtle.Turtle()
    animal.shape(shape)
    animal.color(color)
    animal.pensize(size)
    animal.right( right)
    animal.forward(forward)
    return animal

wn = make_window("lightgreen", "Tess and Alex dancing")
tess = make_turtle("turtle","hotpink", 5, 0, 115)
#tess.forward(5)
alex = make_turtle("arrow", "black", 3, -35, 142)
#alex.right(45)
#alex.forward(45)
dave = make_turtle("circle","yellow", 7, 55, -133)
#dave.left(45)
#dave.forward(45)
import turtle
__import__("turtle").__traceable__= False

window = turtle.Screen()

def make_window(color, title):
  window = turtle.Screen()
  window.bgcolor(color)
  window.title(title)
  return window
wn = make_window("lightgreen", "Tess and Alex dancing")

t=turtle.Turtle()
sz=20
def draw_turtlr_square(t,sz):
    for i in range(1):
        for a in range(4):
         t.forward(sz)
         t.left(90)
    t.penup()
    t.forward(2*sz)
    t.pendown()


draw_turtlr_square(turtle,20)
draw_turtlr_square(turtle,20)
draw_turtlr_square(turtle,20)
draw_turtlr_square(turtle,20)

wn.mainloop()
