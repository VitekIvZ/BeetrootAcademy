#task3lesson17.py


"""
Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для 
дробів (+, -, /, *) з належною перевіркою й обробкою помилок. 
Потрібно додати магічні методи для математичних операцій та операції порівняння між 
об'єктами класу Fraction

 

class Fraction:
    pass

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4) 
"""


from math import gcd

class Fraction:
    def __init__(self, numerator, denominator): #Конструктор `__init__` приймає чисельник і знаменник, перевіряє, чи знаменник не дорівнює нулю, і викликає метод `_reduce` для скорочення дробу
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    def _reduce(self): #Метод `_reduce` використовує функцію `gcd` для знаходження найбільшого спільного дільника і скорочення дробу.
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        return NotImplemented

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    z = x + y
    print(z)  
    assert z == Fraction(3, 4)

    z = x - y
    print(z)  
    assert z == Fraction(1, 4)

    z = x * y
    print(z)  
    assert z == Fraction(1, 8)

    z = x / y
    print(z)  
    assert z == Fraction(2, 1)

    print(x < y)  
    print(x <= y) 
    print(x == y)  
    print(x > y)  
    print(x >= y)  
