# PURPOSE: Write a GUI program that calculates the Body Mass Index
# of a human being given input by the user. The BMI is calculated
# by dividing the weight (in kilograms) by the square of the height
# (in meters) of the person. The user should be able to enter the
# weight and height either in both metric, or US common units.
#
# Hint: Kilogram is 2.2 pounds. A meter is 39.5 inches.
# Name: Kaivan Taylor
# Professor Seaman - CSC 201 Computer Science I

from tkinter import *

#---------------------------class BMI_Calculator------------------------------#

class BMI_Calculator:

    def __init__(self):
        window = Tk()
        window.title("BMI Calculator")    
             
        # Input Label and Entry (Row 1, 2) w/ formatting.
        Label(window, text = "Height: ").grid(row=1, column=1)
        self._height_obj = StringVar() # Height Object
        Entry(window, textvariable = self._height_obj).grid(row=1,column=2)

        Label(window, text = "Weight: ").grid(row=2, column=1)
        self._weight_obj = StringVar() # Weight Object
        Entry(window, textvariable = self._weight_obj).grid(row=2,column=2)

        # Input Radiobuttons (Row 3) w/ formatting.
        self._radio_button_response_obj = IntVar() # Radiobutton variable
        
        rb_orange   = Radiobutton(window, text = "Metric Units (m./kg.)", bg = "orange", \
                              variable = self._radio_button_response_obj,\
                              value = 1) # Selection 1 
        
        rb_green = Radiobutton(window, text = "U.S. Units (in./lb.)", bg = "red", \
                              variable = self._radio_button_response_obj,\
                              value = 2) # Selection 2

        rb_orange.grid(row = 3, column = 1)
        rb_green.grid(row = 3, column = 2)
        
        # Input Button for Computing BMI
        Button(window, text = "Compute", command = self.compute_bmi).\
                grid(row = 4, column = 2)

        # Output Label (Row 4) w/ formatting.
        Label(window, text = "BMI Index (%): ").grid(row=5, column=1)
        self._BMI_obj = StringVar() # Body Mass Index Object
        Label(window, textvariable = self._BMI_obj,\
                       bg = "yellow").grid(row=5, column=2)

        window.mainloop() # Creates a loop

            
    def compute_bmi(self):
        try:
            # Get all objects from two entries, and radiobutton
            unformat_height = float(self._height_obj.get())
            unformat_weight = float(self._weight_obj.get())
            rb_value = self._radio_button_response_obj.get()
            #print(unformat_height, unformat_weight, rb_value)
            
            if (unformat_height or unformat_weight) >= 0: # Positive weight and height.
                
                if rb_value == 1: # Metric Units
                    format_height = unformat_height **2
                    format_weight = unformat_weight

                    calculated_bmi = format_weight / format_height
                    self._BMI_obj.set(format(calculated_bmi, "10.2f")) # Format for two decimals.
                else:
                    format_height = unformat_height / 39.3701 # Actual meter to in. conversion
                    format_weight = unformat_weight / 2.20462 # Actual kg. to lb. conversion

                    format_height = format_height **2

                    calculated_bmi = format_weight / format_height
                    self._BMI_obj.set(format(calculated_bmi, "10.2f")) # Format for two decimals.
            else:
                # If the given height and weight is negative.
                self._BMI_obj.set(format("VALUE ERROR")) 
                
        except ValueError:
            self._BMI_obj.set(format("VALUE ERROR")) # Error if not float or integer.
            
#---------------------------MAIN------------------------------------------#
BMI_Calculator()
