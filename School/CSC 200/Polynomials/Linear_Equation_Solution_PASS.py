# PURPOSE: Solve the general linear equation
# ax + b = c, given a , b & c from the user.
# If a is too small, tell user, and quit program.
# Date: October 2, 2017
# Author: in-class exercise.

EPSILON = 0.000001 # a constant to test for small number

# Get the three coefficients a , b , & c from the user.
a_str = input("Enter Coefficient a: ")
b_str = input("Enter Coefficient b: ")
c_str = input("Enter Coefficient c: ")

#convert the three coefficients to floats.
a_float = float(a_str)
b_float = float(b_str)
c_float = float(c_str)

# If a = 0, then let the user know & stop the program.
if abs(a_float) < EPSILON:
    print("Coefficient 'a' is too small. Program aborted")
else: #otherwise go ahead and compute the solution
    difference = (c_float - b_float)
    x_float = (difference/a_float)
    print("Solution is ", x_float)

