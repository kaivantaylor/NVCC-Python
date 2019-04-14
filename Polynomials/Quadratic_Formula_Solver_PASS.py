# PURPOSE: Write a computer program to solve the general quadratic equation
# ax^2 + bx + c = 0 for real number solutions.
# Date: October 3, 2017
# Author: Kaivan Taylor
# Introduction to Computer Science CSC 200

import math # imports math functionalities into Python.
import time # imports time functionalties into Python.

def quad():
    
    while True: # main program

        EPSILON = 0.000001 # A constant used to test for a small number close that is extremely close zero

        # Get the three coefficient values and assign to a, b, & c
        a_str = input("Enter a number for Coefficient A: ")
        b_str = input("Enter a number for Coefficient B: ")
        c_str = input("Enter a number for Coefficient C: ")

        # Use isalpha to determine whether or not input from user is a number or a letter. Converts str (a, b, & c) to True if a character
        # and False if anything else.
        a = a_str.isalpha()
        b = b_str.isalpha()
        c = c_str.isalpha()
        
        if a_str == "0":
            print("\nFor the equation:", a_str, "*X^2+", b_str, "*X+",c_str, "= 0")
            print("The equation is not quadratic; it is a linear.")
            print("This program cannot solve linear equations \nGoodbye!")
            time.sleep(10.0)
            break
        elif a or b or c == True: # If the user input is a character, prompt user to re-enter coefficients
            print("\nPlease only use numbers!")
            continue
        elif a_str == '': # If the user leaves coefficient a blank, prompt user to re-enter coefficient "A".
            print("\nPlease do not leave input blank!")
            continue
        elif b_str == '': # If the user leaves coefficient a blank, prompt user to re-enter coefficient "B".
            print("\nPlease do not leave input blank!")
            continue
        elif c_str == '': # If the user leaves coefficient a blank, prompt user to re-enter coefficient "C".
            print("\nPlease do not leave input blank!")
            continue
        else:
            # Convert coefficient strings to a float.
            a_float = float(a_str)
            b_float = float(b_str)
            c_float = float(c_str)

        # Print out coefficients a, b, & c for confirmation with spacing for neatness.
        print("\n")
        print("Coefficient A: ", a_float)
        print("Coefficient B: ", b_float)
        print("Coefficient C: ", c_float)

        # Calculate the discriminant.
        discriminant = ((b_float**2)-(4*a_float*c_float))

        # Print out discriminant with spacing for neatness.
        print("\n")
        print("Discriminant:", discriminant)

        # Calculate the number of solutions using the discriminant.
        if discriminant > EPSILON:
            print("For the equation:", a_float, "*X^2+", b_float, "*X+",c_float, "= 0")
            print("There are exactly two real solutions.")
            x1 = (-b_float + math.sqrt(discriminant)) / (2*a_float)
            x2 = (-b_float - math.sqrt(discriminant)) / (2*a_float)
            print("\n")
            print("X = ", x1,",", x2)
        elif discriminant == 0:
            print("For the equation:", a_float, "*X^2+"
                  , b_float, "*X",c_float, "= 0")
            print("There is exactly one solution.")
            x1 = (-b_float + math.sqrt(discriminant)) / (2*a_float)
            print("\n")
            print("X = ", x1)
        else:
            print("For the equation:", a_float, "*X^2+", b_float, "*X+",c_float, "= 0")
            print("There are no real solutions.")

        # Use a loop in order to ask user if the program wants to be re-run from the beginning    
        while True:
            answer = input('\nRun again? (y/n): ')
            if answer in ('y', 'n'): # If input by user is not 'y', or 'n' the loop will reiterate the "Run Again" string.
                break
            print( 'Invalid input.')
        if answer == 'y':
            continue
        else:
            print("\n")
            print("Goodbye!")
            time.sleep(2.0) # After inputting "n," the timer will count for two seconds before exiting the program.
            break
            
