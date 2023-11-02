# Rational.py
# demonstrates operator overloading

class Rational():

    def __init__(self, num = 0, den = 1):

        '''creates a new Rational object
        pre: num and den are integers
        post: creates the Rational object num / den'''

        m = num
        n = den
        while n != 0:
            m, n = n, m%n
        # m is the gcd of num and den
        
        self.num = num // m
        self.den = den // m


    def __mul__(self, other):

        '''* operator
        pre: self and other are Rational objects
        post: returns Rational product: self * other'''

        num = self.num * other.num
        den = self.den * other.den
        return Rational(num, den)

    def __add__(self, other):

        num = self.num*other.den + other.num*self.den
        den = self.den*other.den
        return Rational(num, den)

                
    def __str__(self):

        '''return string for printing
        pre: self is Rational object
        post: returns a string representation self'''
        
        return str(self.num) + '/' + str(self.den)
