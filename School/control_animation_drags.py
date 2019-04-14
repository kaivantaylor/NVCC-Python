# Tk_17_Control_Animation with mouse drags.
# Still uses buttons to stop, resume & control speed.

from tkinter import *
import random

class ControlAnimation:
    def __init__(self):

        my_window = Tk() # create a window
        my_window.title("Control Animation Demo")

        self.width  = 400
        self.height = 200
        
        self.line_x = 370
        self.line_top =  75
        self.line_bot = 125 
        self.dy = 5
        
        self.my_canvas = Canvas(my_window, bg = 'white', \
                width = self.width, height = self.height)
        self.my_canvas.pack()

        frm_control = Frame(my_window) # for command buttons below canvas
        frm_control.pack()
        btn_stop = Button(frm_control, text = 'Stop', \
                         command = self.stop)
        btn_stop.pack(side = LEFT)  
        btn_resume = Button(frm_control, text = 'Resume', \
                           command = self.resume)
        btn_resume.pack(side = LEFT)  
        btn_faster = Button(frm_control, text = 'Faster', \
                           command = self.faster)
        btn_faster.pack(side = LEFT)  
        btn_slower = Button(frm_control, text = 'Slower', \
                           command = self.slower)
        btn_slower.pack(side = LEFT)  

        self.radius = 20
        self.x = self.radius # just to start; y is at canvas center
        self.y = self.height/2 #half-way up/down
        # (x, y) is center of disk for this program, but ...
        # recall: x1,y1 and x2,y2 form a bounding box for disk
        self.my_canvas.create_oval(\
            self.x - self.radius, self.height/2 + self.radius,\
            self.x + self.radius, self.height/2 - self.radius,\
                              fill = "red", tags = "disk")
        self.my_canvas.create_line(self.line_x, self.line_top, \
                                   self.line_x, self.line_bot, \
                    width = 3, fill = "blue", tags = "paddle") 
        #self.my_canvas.bind("<KeyPress-Up>", self.move_paddle)
        #self.my_canvas.bind("<KeyPress-Down>", self.move_paddle)
        self.my_canvas.bind("<B1-Motion>", self.move_paddle)                              
        self.my_canvas.bind("<Button-1>", self.set_mouse_position)
        
        self.sleep_time = 50
        self.is_stopped = False
        self.my_canvas.focus_set() # give the canvas the focus at start-up
                              # to receive input from the keyboard
        self.animate()
        my_window.mainloop()

    def set_mouse_position(self, event):
        self.x_start = event.x
        self.y_start = event.y
        
    def move_paddle(self, event):
        print(" x-pos =", event.x)
        #print(" y-pos =", event.y)
        if event.x < self.line_x - 5 or event.x > self.line_x + 5:
            return
        #dx = event.x - self.x_start        
        dy = event.y - self.y_start
        print(" dy =", dy)
        self.y_start = event.y        
        #print("-----------------------------------")

        self.line_top += dy
        self.line_bot += dy
        self.my_canvas.move("paddle", 0, dy)         
        
    def stop(self):
        self.is_stopped = True

    def resume(self):
        self.is_stopped = False
        self.animate()

    def faster(self):
        if self.sleep_time > 5:
            self.sleep_time -= 15

    def slower(self):
        self.sleep_time += 15

    def animate(self):
        dx = 3
        dy = 3
        while not self.is_stopped :
            self.my_canvas.move("disk", dx, dy) # move right
            self.my_canvas.after(self.sleep_time) # sleep for a few ms            
            # redraw/update the canvas w/ new oval position
            self.my_canvas.update() 
            
            # increment x to set up for next re-draw
            self.x += dx
            if self.x + self.radius > self.width: # hit right boundary
                dx = -(dx + random.randint(0,2) ) # dx now negative
                
            elif self.x - self.radius <= 0: # hit left boundary
                dx = -dx + random.randint(0,2)  # dx now pos

            # increment y to set up for next re-draw
            self.y += dy
            if self.y + self.radius > self.height: # hit bottom boundary
                dy = -dy
            elif self.y - self.radius <= 0: # hit top boundary
                dy = -dy                
            
   
ControlAnimation() # create an instance of the GUI


