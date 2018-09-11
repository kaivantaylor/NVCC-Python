# Rational numbers: Part B

def gcd(bigger, smaller):
    '''compute the greatest common divisor of two positive integers'''

    if not bigger > smaller :
        bigger, smaller = smaller, bigger
    while smaller != 0:
        remainder = bigger % smaller
        bigger, smaller = smaller, remainder
    return bigger

def lcm(a, b):
    '''calculate the least common multiple of two positive integers'''
    return (a*b)//gcd(a,b)


class Rational(object):
    '''Rational with numerator and denominator. Denominator defaults to 1'''

    def __init__(self, numer, denom = 1):
        #print('in constructor')
        self.numer = numer
        self.denom = denom

    def __str__(self):
        '''String representation for printing'''
        return str(self.numer)  + '/'  +  str(self.denom)

    def __repr__(self):
        ''' Used in the interpreter. Call __str__ for now'''
        return self.__str__()

    def __add__(self, param_Rational):
        '''Add two Rationals'''
        if type(param_Rational) == int:
            param_Rational = Rational(param_Rational)
        if type(param_Rational) == Rational:
            the_lcm = lcm(self.denom, param_Rational.denom)
            # multiply each numerator by the lcm, then add
            numerator_sum = the_lcm*self.numer/self.denom + \
                        the_lcm*param_Rational.numer/param_Rational.denom
            return Rational( int(numerator_sum), the_lcm )
        else:
            print("Wrong type in addition method.")
            raise(TypeError)

    def __radd__(self, param):
        "Reverse add"""
        return self.__add__(param)
        
    def __sub__(self, param_Rational):
        '''Subtract two Rationals'''
        the_lcm = lcm(self.denom, param_Rational.denom)
        # multiply each numerator by the lcm, then add
        numerator_sum = the_lcm*self.numer/self.denom - \
                    the_lcm*param_Rational.numer/param_Rational.denom
        return Rational( int(numerator_sum), the_lcm )

    def reduce_rational(self):
        '''Return the reduced fraction value as a Rational'''
        # find the gcd and divide numerator and denominator by it
        the_gcd = gcd(self.numer, self.denom)
        return Rational( self.numer//the_gcd, self.denom//the_gcd)

    def __eq__(self, param_Rational):
        '''Compare two Rationals for equality and return a Boolean'''
        reduced_self  = self.reduce_rational()
        reduced_param = param_Rational.reduce_rational()
        return reduced_self.numer == reduced_param.numer and\
               reduced_self.denom == reduced_param.denom
        
# ------------------------------ MAIN --------------------
#r1 = Rational(1,2)
#print(r1)
#r2 = Rational(3,4)
#print(r2)
#print( gcd(18, 48))
#print( gcd(48, 18))
#print( lcm(48, 18) )
#r3 = Rational(7, 18)
#r4 = Rational(5, 48)
#r5 = r3 + r4
#print(r5)
# ---------------------------------the above was tested in part A

# ------------------------------ tests for gcd and equality opoerator
#r6 = Rational(12,18)
#print(r6.reduce_rational())
#r7 = Rational(18,12)
#print(r7.reduce_rational())
r_2_3 = Rational(2,3)
if r_2_3 == r_2_3 :
    pass
else:
    print("error in equality method")
r_3_4 = Rational(3,4)
if r_2_3 == r_3_4 :
    print("error in equality method")
# --------------------------------------- Test for Addition
r_17_12 = Rational(17,12)
assert r_2_3 + r_3_4 == r_17_12, "Error in addition method"

r_1_12 = Rational(1, 12)
assert r_3_4 - r_2_3 == r_1_12,  "Error in subtraction method"

r_12_5 = Rational(12,5)
r_2_5  = Rational(2,5)
assert r_2_5 + 2 == r_12_5, "Error in addition method involving integer on right"
assert 2 + r_2_5 == r_12_5, "Error in addition method involving integer on left"
# ---------------------------------------- Tests for Subtraction
assert r_3_4 - r_2_3 == r_1_12, "Error in addition method"
