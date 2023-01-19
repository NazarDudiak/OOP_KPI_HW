import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator // math.gcd(numerator, denominator)
        self.denominator = denominator // math.gcd(numerator, denominator)

    def fractional_form(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def floating_point(self):
        return f"{self.numerator / self.denominator:.3}"
