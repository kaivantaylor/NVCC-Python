# Rational numbers Part A

def gcd(bigger, smaller):
    '''compute the greatest common divisor of two positive integers'''
    if not bigger > smaller :
        bigger, smaller = smaller, bigger
    while smaller != 0:
        remainder = bigger % smaller
        #print('gcd calc, big:{}, small:{}, rem:{}'.format(bigger, smaller, remainder))
        bigger, smaller = smaller, remainder
    return bigger

def lcm(a, b):
    '''calculate the least common multiple of two positive integers'''
    return (a*b)//gcd(a,b)


class Rational(object):
    '''Rational with numerator and denominator. Denominator defaults to 1'''

    def __init__(self, numer, denom = 1):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer)  + '/'  +  str(self.denom)

    def __repr__(self):
        ''' Used in the interpreter. Call __str__ for now'''
        return self.__str__()

    def __add__(self, param_Rational):
        '''Add two Rationals'''
        the_lcm = lcm(self.denom, param_Rational.denom)
        # multiply each numerator by the lcm, then add
        numerator_sum = the_lcm*self.numer/self.denom + \
                    the_lcm*param_Rational.numer/param_Rational.denom
        return Rational( int(numerator_sum), the_lcm )

# ------------------------------ MAIN --------------------
r1 = Rational(1,2)
print(r1)

r2 = Rational(3,4)
print(r2)

print( gcd(18, 48))
print( gcd(48, 18))

print( lcm(48, 18) )

r3 = Rational(7, 18)
r4 = Rational(5, 48)
r5 = r3 + r4
print(r5)
