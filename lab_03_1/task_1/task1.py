import math


class Rational:
    def __init__(self, numerator_1=1, denominator_1=1, numerator_2=1, denominator_2=1):
        self.numerator_1 = numerator_1 // math.gcd(numerator_1, denominator_1)
        self.denominator_1 = denominator_1 // math.gcd(numerator_1, denominator_1)
        self.numerator_2 = numerator_2 // math.gcd(numerator_2, denominator_2)
        self.denominator_2 = denominator_2 // math.gcd(numerator_2, denominator_2)

    def suma(self):
        lcm = math.lcm(self.denominator_1, self.denominator_2)
        pre_numerator = self.numerator_1 * (lcm / self.denominator_1) + self.numerator_2 * (lcm / self.denominator_2)
        pre_denominator = lcm
        numerator = int(pre_numerator // math.gcd(int(pre_numerator), int(pre_denominator)))
        denominator = int(pre_denominator // math.gcd(int(pre_numerator), int(pre_denominator)))
        return f"{numerator}/{denominator}"

    def subtraction(self):
        lcm = math.lcm(self.denominator_1, self.denominator_2)
        pre_numerator = self.numerator_1 * (lcm / self.denominator_1) - self.numerator_2 * (lcm / self.denominator_2)
        pre_denominator = lcm
        numerator = int(pre_numerator // math.gcd(int(pre_numerator), int(pre_denominator)))
        denominator = int(pre_denominator // math.gcd(int(pre_numerator), int(pre_denominator)))
        return f"{numerator}/{denominator}"

    def multiplication(self):
        pre_numerator = self.numerator_1 * self.numerator_2
        pre_denominator = self.denominator_1 * self.denominator_2
        numerator = int(pre_numerator // math.gcd(int(pre_numerator), int(pre_denominator)))
        denominator = int(pre_denominator // math.gcd(int(pre_numerator), int(pre_denominator)))
        return f"{numerator}/{denominator}"

    def division(self):
        pre_numerator = self.numerator_1 * self.denominator_2
        pre_denominator = self.denominator_1 * self.numerator_2
        numerator = int(pre_numerator // math.gcd(int(pre_numerator), int(pre_denominator)))
        denominator = int(pre_denominator // math.gcd(int(pre_numerator), int(pre_denominator)))
        return f"{numerator}/{denominator}"

    def comparison(self):
        if self.numerator_1 / self.denominator_1 > self.numerator_2 / self.denominator_2:
            return f"Number {self.numerator_1}/{self.denominator_1} > {self.numerator_2}/{self.denominator_2}"
        elif self.numerator_1 / self.denominator_1 < self.numerator_2 / self.denominator_2:
            return f"Number {self.numerator_1}/{self.denominator_1} < {self.numerator_2}/{self.denominator_2}"
        elif self.numerator_1 / self.denominator_1 == self.numerator_2 / self.denominator_2:
            return f"Number {self.numerator_1}/{self.denominator_1} = {self.numerator_2}/{self.denominator_2}"
        else:
            return "Error :("


n_1 = input("Enter the numerator of the first number: ")
d_1 = input("Enter the numerator of the first number: ")
n_2 = input("Enter the numerator of the second number: ")
d_2 = input("Enter the denominator of the second number: ")

test = Rational(1, 2, 3, 4)
print("Result:")
print(f"\tSum of numbers: {test.suma()} ;")
print(f"\tThe difference of numbers: {test.subtraction()} ;")
print(f"\tProduct of numbers: {test.multiplication()} ;")
print(f"\tPart of numbers: {test.division()} ;")
print(f"\tComparison of num bers: {test.comparison()} ;")
