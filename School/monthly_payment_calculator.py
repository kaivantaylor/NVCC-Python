""" File: monthly_payment_calculator.py
Purpose: Given P, r, t calculate the monthly payment, R

MAYBE: If using Anaconda: before you run this, type: gui tk
in the iPython console."""

#import tkinter as tk
from tkinter import *

class PaymentCalculator:   # no inheritance from Python's object
    def __init__(self):
        root = Tk()      # create the main window93
        root.title("Monthly Payment Calculator")
     
        # create 4 anonymous lables
        Label(root, text = "Principal:").grid(  row = 1, column = 1)
        Label(root, text = "Rate (%):").grid(   row = 2, column = 1)
        Label(root, text = "Time (yrs):").grid( row = 3, column = 1)
        #Label(root, text = "   ").grid( row = 4, column = 1)        
        Label(root, text = "Monthly Pmt:").grid(row = 5, column = 1)        
    
        # input variables --------------------------
        self.principal_obj     = StringVar()
        self.interest_rate_obj = StringVar()
        self.num_years_obj     = StringVar()
        
        Entry(root, textvariable = self.principal_obj).grid(row = 1,column = 2)
        Entry(root, textvariable = self.interest_rate_obj).grid(row=2,column=2)
        Entry(root, textvariable = self.num_years_obj).grid(row = 3, column =2)
       
        # output variable
        self.monthly_payment_obj = StringVar()
        Label(root, textvariable = self.monthly_payment_obj,\
                       bg = "yellow").grid(row=5, column=2)
        
        # command button to trigger the computation
        Button(root, text = "Compute", command = self.compute_payment).\
                grid(row = 4, column = 2)
        
        root.mainloop()
        
    def compute_payment(self):
        # get the data from the GUI 
        principal_flt   = float(self.principal_obj.get() )
        annual_rate_flt = float(self.interest_rate_obj.get() )
        num_years_flt   = float(self.num_years_obj.get())
        
        #print(principal_flt, annual_rate_flt, num_years_flt)
        monthly_payment = \
            self.ujuuuu_payment(principal_flt, \
                                    annual_rate_flt, \
                                    num_years_flt)
        self.monthly_payment_obj.set( format(monthly_payment, "10.2f")  )
    
    def compute_monthly_payment(self, P, r, t):
        i = r/12
        num = P*i
        den = 1 - (1 + i)**(-12*t)
        R = num/den
        return R

# ==================================== main starts here
PaymentCalculator()  # create an anonymous instance



