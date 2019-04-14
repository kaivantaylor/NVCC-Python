# File: Tk_03_Intro_Classes.py
# Program using TKinter GUI to demo classes
# Author: T Seaman

from tkinter import *   # allows tk-interface graphics library access

class MyDemoClass:
    def __init__(self):
        my_window = Tk() # call constructor for a window
        my_window.title("Class Demo")

        # --- create a check button & variable to transfer 0 or 1 back
        self.checkbutton_response_obj = IntVar() # create an object
        ckb_bold = Checkbutton(my_window, text = "Bold", \
                               variable = self.checkbutton_response_obj, \
                               command = self.process_checkbutton)

        # --- create three radio buttons & variable to determine which was clicked
        self.radio_button_response_obj = IntVar() # create an object
        rbn_red   = Radiobutton(my_window, text = "Red", bg = "red", \
                              variable = self.radio_button_response_obj,\
                              value = 1, command = self.process_radiobutton)
        rbn_green = Radiobutton(my_window, text = "Green", bg = "green", \
                              variable = self.radio_button_response_obj,\
                              value = 2, command = self.process_radiobutton)
        rbn_blue  = Radiobutton(my_window, text = "Blue", bg = "blue", \
                              variable = self.radio_button_response_obj,\
                              value = 3, command = self.process_radiobutton)

        # --- place all objects on the window & register them
        ckb_bold.grid(  row = 1, column = 2)
        rbn_red.grid(   row = 2, column = 1)
        rbn_green.grid( row = 2, column = 2)
        rbn_blue.grid(  row = 2, column = 3)
        
        my_window.mainloop()  # start the event-handler process

    def process_checkbutton(self):
        print("check button is " + \
           ("checked" if self.checkbutton_response_obj.get() == 1 else "unchecked") )

    def process_radiobutton(self):
        # transfer info from graphic to local variable
        rbn_value_int = self.radio_button_response_obj.get() 
        if   rbn_value_int == 1:
            print("Red is selected")
        elif rbn_value_int == 2:
            print("Green is selected")
        else:  # value == 3
            print("Blue is selected")            
    # ----------- end of class definition

# -------------------------------------------- main program starts here
MyDemoClass()   # create an anonymous instance of the class

# place font = "Helvetica 12" in the check button constructor
# change it to "Helvetica 12 bold"
# do the same for the radio buttons afterwards
