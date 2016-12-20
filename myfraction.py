from decimal import *
import fractions

class Fraction:
    def __init__(self, numerator,denominator, mydecimal):
        self.num = numerator
        self.den = denominator
        if type(mydecimal) is Decimal:
            self.num, self.den = self.convert_decimal_to_fraction(mydecimal)
        elif type(mydecimal) is tuple:
            self.num, self.den = mydecimal
        else:
            raise ValueError("The input must either be a decimal number or a tuple")

    def __repr__(self):
        divi = fractions.gcd(self.num, self.den)
        numer = self.num/divi
        denom = self.den/divi
        qr=divmod(numer,denom)
        whole_number =qr[0]
        remainder =qr[1]
        if remainder > 0:
            return '%s %s/%s' % (whole_number, remainder, denom)
        else:
            return '%s' % (whole_number)

    def convert_decimal_to_fraction(self, mydecimal):
        d = -mydecimal.as_tuple().exponent
        den = 10**d
        num = mydecimal*den
        return Fraction(num,den)

    def __add__(self, other):
        num =self.num *other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __div__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other):
        a = self.den * other.den
        b = self.num * (a / self.den)
        c = other.num * (a / other.den)
        return b == c

    def __ne__(self, other):
        a = self.den * other.den
        b = self.num * (a / self.den)
        c = other.num * (a / other.den)
        return b != c

    def __gt__(self, other):
        a =self.den * other.den
        b = self.num * (a/self.den)
        c = other.num * (a/other.den)
        return b > c

f=Fraction(0,0,Decimal('0.24'))
print f.convert_decimal_to_fraction()