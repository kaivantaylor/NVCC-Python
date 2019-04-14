import turtle as t
box_color = "blue"
x = 0
y = 0
height = 100

t.fillcolor(box_color) # Determine the color of the crescent
t.up()
t.goto(x,y) # Declare the position of the crescent
t.begin_fill() # Specif when the fill begins
t.down()
t.circle(height,extent=180) # Create two partial circles
t.circle(height,extent=-190)
t.end_fill() # Specify when the fill ends
