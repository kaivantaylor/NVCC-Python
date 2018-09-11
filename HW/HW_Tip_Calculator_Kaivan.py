# PURPOSE: Write a GUI program that calculates the tips and total
# to pay at a resturaunt. The user should enter the amount of the
# bill without the tip. Then, be given choices as to the percent
# to tip. Values of 10%, 15%, 18%, or 20% by radio buttons. When
# the user clicks a radio button, the tip is calculated which is
# shown to the user, added to the bill for the total to be paid.
# The total is displayed as well. Use Alt-PrintScreen to provide
# window images of each test case.
# CSC 201 - Computer Science I
# Professor Seaman
# Name: Kaivan Taylor

from tkinter import * # Import all of tkinters libraries

#-----------------------CLASS tip_calculator-------------------------#
 
class tip_calculator:

    def __init__(self):
        window = Tk()
        window.title("Kaivan's Tip Calculator") # Title for formatting
        
        # Radio buttons w/ Variables
        self._radio_button_response_obj = IntVar() # Radio button Variable
        rb_red   = Radiobutton(window, text = "10%", bg = "red", \
                              variable = self._radio_button_response_obj,\
                              value = 1, command = self.process_radiobutton)
        rb_green = Radiobutton(window, text = "15%", bg = "green", \
                              variable = self._radio_button_response_obj,\
                              value = 2, command = self.process_radiobutton)
        rb_blue  = Radiobutton(window, text = "18%", bg = "blue", \
                              variable = self._radio_button_response_obj,\
                              value = 3, command = self.process_radiobutton)
        rb_yellow = Radiobutton(window, text = "20%", bg = "yellow", \
                              variable = self._radio_button_response_obj,\

                              value = 4, command = self.process_radiobutton)
        # Radio Button w/ Formatting
        rb_red.grid(row = 2, column = 1)
        rb_green.grid(row = 2, column = 2)
        rb_blue.grid(row=2, column=3, padx= 20)
        rb_yellow.grid(row=2, column=4, padx= 20)

        # Labels w/ Formatting
        Label(window, text = "Cost before Tip:").grid( row=1, column=1)
        Label(window, text = "Tip:").grid( row=3, column=1)
        Label(window, text = "Grand Total:").grid( row=4, column=1)        

        # Entry w/ Formatting
        self.cost_obj = StringVar() # Cost before Tip Object
        Entry(window, textvariable = self.cost_obj).grid(row=1,column=2)

        # Output Variable
        self._tip_obj = StringVar() # Tip Amount Object
        Label(window, textvariable = self._tip_obj,\
                       bg = "yellow").grid(row=3, column=2)
        self._total_obj = StringVar() # Grand Total Object
        Label(window, textvariable = self._total_obj,\
                       bg = "yellow").grid(row=4, column=2)
        
        window.mainloop()

    def process_radiobutton(self):

        # Raises ValueError if cost_flt & rb_value_flt is not convertable to float
        try:
            # Transfer info from GUI to backend
            rb_value_flt = self._radio_button_response_obj.get()
            cost_flt = self.cost_obj.get()

            # Convert variables to float values
            rb_value_flt = float(rb_value_flt)
            cost_flt = float(cost_flt)

            if cost_flt >= 0: # If the value is negative, print an error
                            
                if rb_value_flt == 1:
                    calculated_tip = cost_flt * .10
                    self._tip_obj.set(format(calculated_tip,"10.2f"))

                elif rb_value_flt == 2:
                    calculated_tip = cost_flt * .15
                    self._tip_obj.set(format(calculated_tip,"10.2f"))

                elif rb_value_flt == 3:
                    calculated_tip = cost_flt * .18
                    self._tip_obj.set(format(calculated_tip,"10.2f"))
                    
                else:
                    calculated_tip = cost_flt * .20
                    self._tip_obj.set(format(calculated_tip,"10.2f"))

                grand_total = calculated_tip + cost_flt
                self._total_obj.set(format(grand_total,"10.2f"))

            else:
                self._tip_obj.set("ERROR")
                self._total_obj.set("USE POSITIVE NUMBERS")

        except ValueError:
            self._tip_obj.set("ERROR")
            self._total_obj.set("USE ONLY NUMBERS")

#------------------------------MAIN----------------------------------#
tip_calculator()
