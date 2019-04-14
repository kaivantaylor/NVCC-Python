# PURPOSE: Code used to read the circumference of a cirlce and output the radius
# of a circle
# Intro to Comp. Science
# Author: Kaivan Taylor 9/26/17

import math

circumference_int = int(input("Enter circumference:"))
radius_float = ((circumference_int)/(2*math.pi))
radius_str = str(radius_float)
print("The radius is: ", radius_str)

