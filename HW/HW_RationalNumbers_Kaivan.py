 # PURPOSE: Augment the Rational number class to include multiplication
# and division. Include the ability to accomodate operands of type int.
# Name: Kaivan Taylor
# Class: CSC 200 - Introducion to Computer Science I
# Professor Seaman
# Date: 3/31/2018

#------------------------Greatest Common Denominator Method---------------------#
def gcd(big,small):
    '''Takes the biggest number and smallest number and calculates the GCM.'''

    if not big > small:
        big, small = small, big

    while small != 0:
        remainder = big % small
        big, small = small, remainder

    return big

#--------------------------Least Common Multiple Method-------------------------#
def lcm(a,b):
    '''Calculate the least common multiple of two integers.'''

    return (a*b) // gcd(a,b)

#--------------------------------Rational class---------------------------------#
class Rational(object):
    ''' Method that converts given numerator and denominator into rational format.
    Denominator defaults to 1 if no other value is provided.'''

    def __init__(self, numerator, denominator = 1):

        if (numerator and denominator) < 0:
            self.numerator = numerator * -1
            self.denominator = denominator * -1
            
        else:
            self.numerator = numerator
            self.denominator = denominator

        #print("in __init__")

    def __str__(self):
        ''' Reformat anything passed into str with a '/' in the middle of
        the numerator and denominator'''
        
        #print("in __str__")
        
        return str(self.numerator) + "/" + str(self.denominator)
    
    def __repr__(self):
        ''' Returns the value of a given variable. Call __str__'''

        #print("in __repr__")
        
        return self.__str__()
    
#-------------------Formatting after +,-,*,/ in Rational Class-------------------#
    def reduce_rational(self):
        ''' Return the fraction in reduced form.'''

        gcd_Rational = gcd(self.numerator, self.denominator)

        return Rational(self.numerator // gcd_Rational, self.denominator // gcd_Rational)
    
    def __eq__(self, param_Rational):
        '''Compare two rationals given for equality and return a Boolean.'''

        reduced_self = self.reduce_rational()
        reduced_param = param_Rational.reduce_rational()

        #print("in __eq__")
        
        return reduced_self.numerator == reduced_param.numerator and\
               reduced_self.denominator == reduced_param.denominator

#----------------------Addition Method in Rational Class------------------------#
    def __add__(self, param_Rational):
        ''' Adds two rationals. Takes any integer form an turns into a rational form.'''

        if type(param_Rational) == int: # Used for if input is an integer. e.g. '1'
            param_Rational = Rational(param_Rational)

        if type(param_Rational) == Rational:
            
            lcm_Rational = lcm(self.denominator, param_Rational.denominator)
            # Multiply by the least common multiple, then add.
            numerator_sum = lcm_Rational * self.numerator / self.denominator + \
                            lcm_Rational * param_Rational.numerator / param_Rational.denominator

            return Rational(int(numerator_sum), lcm_Rational)
        
        else:
            print("Wrong type in Addition method!")
            raise(TypeError)
    def __radd__(self, param):
        '''Reverse add if the traditional add method for int has second value of
        different type.'''
    
        return self.__add__(param)

#---------------------Subtraction Method in Rational Class-----------------------#
    def __sub__(self, param_Rational):
        ''' Subtract two rationals.'''

        if type(param_Rational) == int: # Used for if input is an integer. e.g. '1'
            param_Rational = Rational(param_Rational)
                
        if type(param_Rational) == Rational:

            lcm_Rational = lcm(self.denominator, param_Rational.denominator)
            # Multiply each numerator by lcm and add.
            numerator_sum = lcm_Rational * self.numerator / self.denominator - \
                            lcm_Rational * param_Rational.numerator / param_Rational.denominator

            return Rational.reduce_rational(Rational(int(numerator_sum), lcm_Rational))

        else:
            print("Wrong type for Subtraction method!")
            raise(TypeError)
        
    def __rsub__(self,param):
        '''Reverse sub if the traditional sub method for int has second value of
        different type.'''

        if type(param) == (int or Rational):
            return self.__sub__(param) * -1
        else:
            print("Wrong type for Subtraction method!")
            raise(TypeError)

#---------------------Multiplication Method in Rational Class--------------------#
    def __mul__(self, param_Rational):
        '''Multiply the two rationals.'''

        if type(param_Rational) == int:
            param_Rational = Rational(param_Rational)

        if type(param_Rational) == Rational:
            
            # Multiply across between the two numerators and two denominators.
            numerator_sum = self.numerator * param_Rational.numerator
            denominator_sum = self.denominator * param_Rational.denominator
            Rational_sum = Rational(numerator_sum, denominator_sum)        
        
            return Rational.reduce_rational(Rational_sum)

        else:
            print("Wrong type for Multiplication method!")
            raise(TypeError)
        
    def __rmul__(self, param):

        if type(param) == (int or Rational):
            return self.__mul__(param)

        else:
            print("Wrong type for Mutltiplication method!")
            raise(TypeError)

#-----------------------Division Method in Rational Class------------------------#
    def __truediv__(self, param_Rational):

        if type(param_Rational) == int:
            param_Rational = Rational(param_Rational)
            
        if type(param_Rational) == Rational:
            new_Rational_numerator = param_Rational.denominator
            new_Rational_denominator = param_Rational.numerator
            param_Rational = Rational(new_Rational_numerator, new_Rational_denominator)
            
        else:
            print("Wrong type for Division method!")
            raise(TypeError)

        if type(self and param_Rational) == Rational:
            numerator_Rational = self.numerator * param_Rational.numerator
            denominator_Rational = self.denominator * param_Rational.denominator
            Rational_sum = Rational(numerator_Rational, denominator_Rational)

            return Rational.reduce_rational(Rational_sum)
        
    def __rtruediv__(self, param):

        if type(param) == int:        
            holder_variable = self
            self = Rational(param)
            param = holder_variable

            return self.__truediv__(param)
        
        else:
            print("Wrong type for Division method!")
            raise(TypeError)

#------------------------------M A I N-------------------------------------------#

#------------Test Variables------------
r_4_12 = Rational(4,12)
r_5_10 = Rational(5,10)
r_n3_7 = Rational(-3,7)
r_4_n6 = Rational(4,-6)
r_n5_n15 = Rational(-5,-15)

# ----- Test for __init__, __str__, __repr__ in Rational class ------
assert Rational.reduce_rational(r_4_12) == Rational(1,3)
assert Rational.reduce_rational(r_5_10) == Rational(1,2)
assert Rational.reduce_rational(r_n3_7) == Rational(-3,7)
assert Rational.reduce_rational(r_4_n6) == Rational(-2,3)
assert Rational.reduce_rational(r_n5_n15) == Rational(1,3)

# -------- Test for reduce rational method -------
assert Rational.reduce_rational(r_4_12) == Rational(1,3), "Error in reduce rational method"
assert Rational.reduce_rational(r_5_10) == Rational(1,2), "Error in reduce rational method"
assert Rational.reduce_rational(r_n3_7) == Rational(-3,7), "Error in reduce rational method"
assert Rational.reduce_rational(r_4_n6) == Rational(-2,3), "Error in reduce rational method"
assert Rational.reduce_rational(r_n5_n15) == Rational(1,3), "Error in reduce rational method"


# ---------- Test for gcd, lcm operator ---------
assert gcd(5,10) == 5, "Error in gcd operator"
assert gcd(10,-5) == -5, "Error in gcd operator"
assert gcd(-6,-12) == -6, "Error in gcd operator"
assert gcd(-1,10) == -1, "Error in gcd operator"

assert lcm(5,10) == 10, "Error in lcm operator"
assert lcm(10,-5) == 10, "Error in lcm operator"
assert lcm(-6,-12) == -12, "Error in lcm operator"
assert lcm(-1,10 )== 10, "Error in lcm operator"


# -------- Test for equality operator ---------- 

assert r_n3_7 == r_n3_7, "Error in Equality Operator"

# ------ Test for Addition operator --------

# ==== Int/Rational, Rational/Int, Rational/Rational ====
assert 1 + r_4_12 == Rational(16,12), "Error in addition operator"
assert r_5_10 + 1 == Rational(15,10), "Error in addition operator"
assert r_4_12 + r_n3_7 == Rational(-8,84), "Error in addition operator"

 
# ==== Float in + method ====
#assert 1.2 + r_4_12, "+ Method Works, Float not accepted"
#assert r_4_n6 + 1.2, "+ Method Works, Float not accepted"

# ------ Test for Subtraction operator --------

# ==== Int/Rational, Rational/Int, Rational/Rational ====
assert 1 - r_4_12 == Rational(2,3), "Error in subtraction operator"
assert r_5_10 - 1 == Rational(-1,2), "Error in subtraction operator"
assert r_4_12 - r_n3_7 == Rational(16,21), "Error in subtraction operator"

# ==== Float in - method ====
#assert 1.2 - r_4_12, "- Method Works, Float not accepted"
#assert r_4_n6 - 1.2, "- Method Works, Float not accepted"

# ------- Test for Multiplication method -----------

# ==== Int/Rational, Rational/Int, Rational/Rational ====
assert r_5_10 * r_4_12 == Rational(1,6), "Error in multiplication operator"
assert r_4_n6 * 1 == Rational(-2,3), "Error in multiplication operator"
assert 1 * r_n5_n15 == Rational(1,3), "Error in multiplication operator"

# ==== Negative int in * method ====
assert -1 * r_n5_n15 == Rational(-1,3), "Error in multiplication operator"
assert r_4_n6 * -1 == Rational(2,3), "Error in multiplication operator"

# ==== Float in * method ====
# assert 1.2 * r_n5_n15, "* Method Works, Float not accepted"
# assert r_n5_n15 * 1.2, "* Method Works, Float not accepted"

# ------- Test for Division method -----------

# ==== Int/Rational, Rational/Int, Rational/Rational ====
assert r_5_10 / r_4_12 == Rational(3,2), "Error in division operator"
assert r_4_n6 / 1 == Rational(-2,3), "Error in division operator"
assert 1 / r_n5_n15 == Rational(3,1), "Error in division operator"

# ==== Negative int in / method ====
assert -1 / r_n5_n15 == Rational(-3,1), "Error in division operator"
assert r_4_n6 / -1 == Rational(2,3), "Error in division operator"

# ==== Float in / method ====
# assert 1.2 / r_n5_n15, "/ Method Works, Float not accepted"
# assert 1.2 / r_n5_n15, "/ Method Works, Float not accepted"

