# PURPOSE: Create about 10 stars and crescent shapes using turtle
# and output to an "eps" file.
# Author: Kaivan Taylor
# Date: 11/14/17

import turtle as t # import turtle for drawing shapes
import random   # import random for random integers

def star(x, y, height, box_color):  
    t.fillcolor(box_color) # Determine the color of the star
    t.up()
    t.goto(x,y) # Declare the center of the star
    t.left(54)
    t.forward(height/2)
    t.left(54)
    t.begin_fill() # Specify when the fill begins
    for n in range (5): # Draw five triangles of the star and rotate accordingly
        t.down()
        t.forward(height)
        t.left(72*2)
        t.forward(height)
        t.right(72)
    t.end_fill() # Specify when the fill ends
    t.up()

def crescent(x,y,height,box_color):
    t.fillcolor(box_color) # Determine the color of the crescent
    t.up()
    t.goto(x,y) # Declare the position of the crescent
    t.begin_fill() # Specif when the fill begins
    t.down()
    t.circle(height,extent=180) # Create two partial circles
    t.left(10)
    t.circle(height,extent=-190)
    t.end_fill() # Specify when the fill ends
    t.up()
# ==================== main() starts here ===================#
t.colormode(255) # Set colormode for R,G,B input
t.tracer(-1) # Turn turtle animation off

for n in range(10):
    x = random.randint(-200, 200) # Create random coordinates
    y = random.randint(-200, 200)
    
    r = random.randint(0, 255) # Create random R,G,B inputs
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    box_color = (r, g, b) 
    
    height = random.randint(5, 60) # Create random height

    crescent(x,y,height,box_color) # Call Crescent method
    # and repeat 10 times
    
for n in range(10):
    x = random.randint(-200, 200) # Create random coordinates
    y = random.randint(-200, 200)
    
    r = random.randint(0, 255) # Create random R,G,B inputs
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    box_color = (r, g, b) 
    
    height = random.randint(5, 60) # Create random height

    star(x,y,height,box_color) # Call star method and repeat 10 times

# Write name in upper-left corner    
t.up()
t.goto(-350,300) # Use coordinates close to top left corner
t.down()
t.pencolor("black")
t.write("Name: Kaivan Taylor", font=("arial",18,"normal"))

# Output the canvas to an encapsulated postscript file
t.getcanvas().postscript(file = "homework_example.eps")
