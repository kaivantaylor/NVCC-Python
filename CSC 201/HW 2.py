# PURPOSE: Write a short program that will...
# 1) Prompt the user for a number
# 2) Print out whether the number is a perfect square
# 3) Prompt the user for another number if the input was not a perfect square
# ** Must be a short program and should utilize material learned only in current readings/class.
# Class: CSC 201 Computer Science I
# Name: Kaivan Taylor
# Date: 1/23/2018

import math # Use of math module for square roots from Chapter 1/2.

user_input = input("Hello sir/madam, please enter a positive non-decimal number!: ")
user_input_int = int(user_input) # Ask user for input and convert to an integer data type.

while True: # Create a loop to first determine whether the number is positive or negative.
    if user_input_int > 0:
        result = math.sqrt(user_input_int)
        int_result = int(result) # Change from result float to an integer to round number.
        final = int_result**2 # Reverse the process of the taking the square root.
        if user_input_int == final: # Compare the final and initial user input number.
            print("\n") # Extra line for readability.
            print(final,"is a perfect square")
            break
        else:
            print("\n")
            print(user_input_int,"is not a perfect square") # If the numbers is not matching,
            #it is not a perfect square.
            user_input = input("Please enter another number!: ")# Prompt user to re-enter value.
            user_input_int = int(user_input)
            continue
    else:
        user_input = input("\nPlease enter a positive number!: ") # If the number is less than 0,
        # the number is negative.
        user_input_int = int(user_input)
        continue
        
