# PURPOSE: Design a class called color. The fields of the class are three decimals for
# Red, Green, and Blue components in the range 0, or 1. The value 0 indicates Black and
# 1 is White. Add checks to ensure that values are always in the given range. Provide
# addition and subtraction operators for the color class. Include saturation for subtraction
# and addition; if any components goes less than 0, or greater than 1, assign them 0 or 1,
# respectively.
# Name: Kaivan Taylor
# CSC 201 - Computer Science I

#-------------------------------Class Color----------------------------------#
class Color(object):

    def __init__(self, r, g, b):

        try:
            if r < 0: # Saturation for less than zero.
                r = 0
            if r > 1: # Saturation for more than one.
                r = 1

            if g < 0: 
                g = 0 # If less than zero, it will default to 0.
            if g > 1:
                g = 1 # If more than one, it will default to 1.

            if b < 0:
                b = 0
            if b > 1:
                b = 1

            self.r = float(r) # (r, g, b) will be converted to float.
            self.g = float(g) # An error will be raised if it is not int,
            self.b = float(b) # or float from the the parameters of __init__.
                
        except TypeError: # Raise TypeError if the value is not int, or float.
            print("TypeError in __init__")
            raise(TypeError)

    def __str__(self): # Return r, g, b with float formatting
        # (3 spaces to the left and 2 to the right).
        return "{:3.2f} {:3.2f} {:3.2f}".format(self.r, self.g, self.b)

    def __repr__(self): # When the variable is called, call __str__() which will
        # return a formatted floats.
        return self.__str__()

    def __add__(self, color): # Return the color class with (r, g, b)
        # added from both self and color.
        return Color(self.r + color.r, self.g + color.g, self.b + color.b)
    
    def __sub__(self, color): # Return the color class with (r, g, b)
        # subtracted from both self and color.
        return Color(self.r - color.r, self.g - color.g, self.b - color.b)

    def __eq__(self, color):
        epsil = 0.00000000000000001
        if type(color) == Color: # Use of abs and epsil (epsilon) for values virtually near zero.
            
            if abs(self.r - color.r) < epsil and abs(self.g - color.g) < epsil \
                and abs(self.b - color.b) < epsil: # If the values of the first and second parameters
                # for r, g, b subtract and epsilon is greater. Return true.
                return True     
            else: # The sum of values from r, g, b are greater than epsilon.
                return False
        else: # The type is wrong, return False.
            return False
        
#---------------------------------MAIN + TEST ---------------------------------------#

assert Color(1,1,1) # Test for regular colors
assert Color(0,0,0) # Test for regular colors
assert Color(2,2,2) == Color(1,1,1) # Test for saturation above 1
assert Color(-1,-1,-1) == Color(0,0,0) # Teset for saturation below 0
assert Color(1,1,1) - Color(.5,.5,.5) == Color(.5,.5,.5) # Test for addition
assert Color(0.5,0.5,0.5) - Color(0.3,0.3,0.3) == Color(0.2,0.2,0.2) # Test for subtraction

