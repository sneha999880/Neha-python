class Calculator:
    def calculate(self, a, b, c=None):
        if c is None:
            return a % b
        else:
            return (a ** b) ** c
calc = Calculator()
modulus_result = calc.calculate(10, 3)
print(f"Modulus of 10 and 3: {modulus_result}")
power_result = calc.calculate(2, 2, 2)
print(f"Power of 2, 2 and 2: {power_result}")
