# PURPOSE: Create pong
# Name: Kaivan Taylor
# CSC 201 - Computer Science I
# Professor Seaman

from tkinter import *
import random # Used for creating random angles.

class Pong():

    def __init__(self):

        root = Tk()
        root.title("PySoccer by Kaivan") # Title for format.

#-------------------------------__init__ Variables------------------------------#
        self.width = 1000
        self.height = 700
        self.sleep_time = 10
        self.ismoving = True # Variable to stop/start game
        
        # Canvas for game
        self.canvas = Canvas(root, bg = 'black', \
                                width = self.width, height = self.height)
        self.canvas.create_line(500,0,500,\
                                1000, fill = 'white') # Static Mid-line
#--------------------------------Create Ball---------------------------------#
        self.radius = 30 # Fixed Variable

        self.x = self.radius # x starts from radius.
        self.y = self.height/2 # y starts half the height.

        # Create ball in canvas.
        self.canvas.create_oval(\
            self.x - self.radius, self.height/2 + self.radius,\
            self.x + self.radius, self.height/2 - self.radius,\
                              fill = "red", tags = "ball")
#-------------------------------Create Slot----------------------------------#        
       # Create golley slot for "ball" to enter.
        slot = self.canvas.create_rectangle(190,300,100,100,\
                                       fill = 'white', tags= "slot")
        self.canvas.move("slot",800,100) # Move slot to right-middle in canvas.
#-------------------------------Create Paddle--------------------------------#      
        self.recty = 150 # Variable to shift paddle along y-axis.
        self.canvas.create_rectangle(30,self.recty,10,310,\
                                     fill = "blue", tags = "paddle")
        root.bind("<KeyPress-Up>", self.up) # Bind to Up Arrow.
        root.bind("<KeyPress-Down>", self.down)# Bind to Down Arrow.
#--------------------------------Call Methods--------------------------------#
        self.canvas.pack()
        self.animate()
        root.mainloop()
#---------------------------------Methods------------------------------------#
    def animate(self):
        dy = 8
        dx = 8        
        while self.ismoving == True: # Animates until ball enters goal.
            ball_pos = self.canvas.coords("ball") # Position for ball/ paddle.
            paddle_pos = self.canvas.coords("paddle")

#----------------If the ball does NOT hit the paddle, or goal.---------------#
            if dx <= 12:
                self.canvas.move("ball", dx, dy) # Move right
                self.canvas.after(self.sleep_time) # Sleeps for a few ms            
                self.canvas.update() # Updates the canvas on new position.
                
                # Increments new x for re-draw
                self.x += dx
                if self.x + self.radius > self.width: # Ball hits right wall.
                    dx = -(dx + random.randint(1,2) ) # dx is negative.
                    
                elif self.x - self.radius <= 0: # Ball hits left wall.
                    dx = -dx + random.randint(1,2)  # dx is positive.

                # Increments new y for re-draw
                self.y += dy
                # Ball hits bottom wall.
                if self.y + self.radius > self.height: 
                    dy = -dy
                # Ball hits top wall.
                elif self.y - self.radius <= 0: 
                    dy = -dy
            else: # Max speed is 12, will slow down a number between 4,8.
                dx = random.randint(4,8)
                continue
                
#-------------If ball hit paddle, bounce with random direction.--------------#
            if (paddle_pos[1] <= ball_pos[3] <= paddle_pos[3])\
               and ball_pos[0] <= (paddle_pos[2] + self.radius - 10):                
                #print("Hit Paddle") 
                self.canvas.move("ball", random.randint(-1,1), dy)
                self.canvas.update() 

                # Increments new x for re-draw
                self.x += dx
                if self.x + self.radius > self.width: # Ball hits right wall.
                    dx = -(dx + random.randint(1,2) ) # dx is negative.
                    
                elif self.x - self.radius <= 0: # Ball hits left wall.
                    dx = -dx + random.randint(1,2) # dx is positive.

                # Increments new y for re-draw
                self.y += dy
                # Ball hits bottom wall.
                if self.y + self.radius > self.height: 
                    dy = -dy
                # Ball hits top wall.
                elif self.y - self.radius <= 0:
                    dy = -dy
                    
            # If score goal within boundaries, stop animate() and print "Goal!".
            if (893 <= ball_pos[0]) and (240 <= ball_pos[1] <= 335):
                #print("Hit Goal")
                self.ismoving = False
                self.canvas.create_text(500,50,font=('',50),\
                                text=str("Goal!"),fill='white')
                
    def up(self,event): # User hits up arrow key.
        self.recty = -18
        pos = self.canvas.coords("paddle")
    
        if pos[1] <= 0: # Stops movement at top wall.
            self.recty = -0
        self.canvas.move("paddle",0,self.recty)
        #print(pos)
        
    def down(self,event): # User hits down arrow key.
        self.recty = 18
        pos = self.canvas.coords("paddle")
        
        if pos[3] >= 700: # Stops movement at bottom wall.
            self.recty = 0
        self.canvas.move("paddle",0,self.recty)
        #print(pos)
        
#----------------------------Main-------------------------------------------#
Pong()

