"""PURPOSE: Examples using Turtle Graphics
In-Class exercise; Date: 11/13/17
"""

import random
import turtle as t

def rectangle(x, y, length, height, box_color):
    """Draw a rectangle where the upper left-hand corner is
    at (x, y) of given length, height and color."""
    t.fillcolor(box_color)  # set the fill color to "box color"
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.forward(width)  # move to the right
    t.right(90)       # turn right 90 degrees to go "down"
    t.forward(height) # going down
    t.right(90)       # now heading back to the left
    t.forward(width)  # going back to the left
    t.right(90)       # turn right to go "up"
    t.forward(height)  # we are now back at the starting point
    t.right(90)       # face the direction in which we started

    t.end_fill()
    t.penup()   # done with the rectangle
    t.fillcolor("white") # set back to "stancard"
    
# ============================ main() starts here ====
t.colormode(255)  # need this to use the (r,g,b) colors
t.tracer(-1)

##t.circle(100)
##t.write("A circle.")
##
##t.forward(200)
##t.left(90)
##t.forward(150)

for n in range(50):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    # create an RGB color, each is an integr from 0 - 255.
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    box_color = (r, g, b)
    # select random widths and heights
    width  = random.randint(5, 60) #width in pixels
    height = random.randint(5, 60) #heigth in pixels
    # now draw the rectangle
    rectangle(x, y, width, height, box_color)
    
# write name in upper left-hand corner
t.penup()
t.goto(-350, 300)
t.pendown()
t.pencolor("black")
t.write("Name: Timothy Seaman", font=("arial", 18, "normal") )

# print the canvas to an encapsulated postscript file
t.getcanvas().postscript( file = "my_example.eps" )

